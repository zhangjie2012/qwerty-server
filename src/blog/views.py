import os
import json
import frontmatter
import mistune

from datetime import datetime
from collections import defaultdict, OrderedDict
from django.views.decorators.http import require_GET, require_POST
from django.core.paginator import Paginator

from utils.logger import logger
from utils.http_tools import SuccessResponse, ParamInvalidResponse, ObjectNotExistResponse
from .models import Category, Article


@require_POST
def import_jekyll_content(request):
    try:
        data = json.loads(request.body)
        dst_dir = data['dst_dir']
    except (KeyError, json.JSONDecodeError):
        logger.warning('param invalid|%s', request.body)
        return ParamInvalidResponse()

    def get_file_paths(dst_dir):
        file_paths = []
        for root, _, files in os.walk(dst_dir):
            for file_ in files:
                file_paths.append(os.path.join(root, file_))
        return file_paths

    def parse_post(path):
        """return
        title, category, slug, content, publish_dt
        """
        file_name = os.path.splitext(os.path.basename(path))[0]
        dt_str, slug = file_name[0:10], file_name[11:]
        publish_dt = datetime.strptime(dt_str, '%Y-%m-%d')

        s = open(path, 'r')
        post = frontmatter.load(s)
        title, content = post['title'], post.content

        if 'category' in post.keys():
            category = post['category']

        if 'categories' in post.keys():
            if isinstance(post['categories'], list):
                category = post['categories'][0]
            else:
                category = post['categories']

        if 'date' in post.keys():
            if isinstance(post['date'], datetime):
                publish_dt = post['date']
            else:
                publish_dt = datetime.strptime(post['date'], '%Y-%m-%d %H:%M:%S')

        return title, category, slug, content, publish_dt

    paths = get_file_paths(dst_dir)
    for path in paths:
        title, category, slug, content, publish_dt = parse_post(path)

        # get or create `Category`
        category_obj, created = Category.objects.get_or_create(
            name=category,
            defaults={
                'name': category,
                'slug': category,
            }
        )
        if created:
            logger.info('create category|%s', category_obj.name)

        # create `Article`
        article, created = Article.objects.get_or_create(
            slug=slug,
            defaults={
                'category': category_obj,
                'title': title,
                'slug': slug,
                'content': content,
                'publish_dt': publish_dt,
                'update_dt': publish_dt,
            }
        )
        if created:
            logger.info('create article|%s|%s', article.title, article.slug)

    return SuccessResponse()


@require_GET
def query_blogs(request):
    page = int(request.GET.get('page', 1))
    per_count = int(request.GET.get('per_count', 10))

    # param error auto fix
    page = 1 if page < 1 else page
    per_count = 10 if per_count < 1 else per_count

    article_qs = Article.objects.exclude(draft=True).values(
        'category__name', 'category__slug',
        'title', 'slug', 'abstract', 'publish_dt'
    )
    paginator = Paginator(article_qs, per_count)
    page_article = paginator.get_page(page)

    article_list = []
    for article in page_article.object_list:
        article_list.append({
            'category': {
                'name': article['category__name'],
                'slug': article['category__slug'],
            },
            'title': article['title'],
            'slug': article['slug'],
            'abstract': article['abstract'],
            'publish_dt': article['publish_dt'],
        })

    logger.debug('query blogs|%d|%d|%d', page, per_count, len(article_list))

    return SuccessResponse({
        'article_list': article_list,
        'current_page_num': page_article.number,
        'total_pages': paginator.num_pages,
    })


@require_GET
def query_blog_detail(request):
    try:
        slug = request.GET['slug']
    except KeyError:
        logger.warning('param slug not exist')
        return ParamInvalidResponse()

    try:
        article = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
        logger.warning('slug article not exist|%s', slug)
        return ObjectNotExistResponse()

    data = {
        'category': {
            'name': article.category.name,
            'slug': article.category.slug,
        },
        'title': article.title,
        'cover_img': article.cover_img,
        'img_copyright': article.img_copyright,
        'abstract': article.abstract,
        'content': mistune.markdown(article.content),
        'publish_dt': article.publish_dt,
        'update_dt': article.update_dt,
    }

    logger.debug('query blog detail|%s|%s', slug, article.title)

    return SuccessResponse(data)


@require_GET
def query_archive_blogs(request):
    article_qs = Article.objects.exclude(
        draft=True).values('title', 'slug', 'publish_dt')

    # archive by year
    year_2_articles = defaultdict(list)
    for article in article_qs:
        year = article['publish_dt'].year
        year_2_articles[year].append(article)

    # be order
    data = []
    for year, articles in year_2_articles.items():
        data.append({
            'year': year,
            'articles': articles,
        })

    logger.debug('query archive blogs')

    return SuccessResponse(data)
