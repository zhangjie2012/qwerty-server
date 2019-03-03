import json
import mistune

from datetime import datetime
from collections import defaultdict
from libgravatar import Gravatar
from django.views.decorators.http import require_GET, require_POST
from django.core.paginator import Paginator

from utils.logger import logger
from utils.http_tools import SuccessResponse, \
    ParamInvalidResponse, ObjectNotExistResponse, get_client_info
from .models import Category, Article, Comment


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

    comment_qs = article.comment_set.filter(show=True).values(
        'username', 'avatar', 'website', 'content', 'publish_dt'
    ).order_by('publish_dt')
    comment_list = []
    for comment in comment_qs:
        comment_list.append({
            'username': comment['username'],
            'avatar': comment['avatar'],
            'website': comment['website'],
            'publish_dt': comment['publish_dt'],
            'content': mistune.markdown(comment['content'])
        })

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
        'comment_list': comment_list,
    }

    logger.debug('query blog detail|%s|%s|%d',
                 slug, article.title, len(comment_list))

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


@require_GET
def query_blog_categories(request):
    category_qs = Category.objects.all()

    data = []
    for category in category_qs:
        article_qs = category.article_set.exclude(draft=True).values(
            'title', 'slug', 'publish_dt')
        data.append({
            'category': {
                'name': category.name,
                'slug': category.slug,
            },
            'articles': list(article_qs),
        })

    logger.debug('query blog categories')

    return SuccessResponse(data)


@require_POST
def add_comment(request):
    try:
        body = json.loads(request.body)
        slug = body['slug']
        username = body['username']
        email = body['email']
        website = body['website']
        content = body['comment']

        ip, browser, os, _ = get_client_info(request)
    except (KeyError, json.JSONDecodeError):
        logger.warning('param invalid|%s', request.body.decode('utf-8'))
        return ParamInvalidResponse()

    try:
        article = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
        logger.warning('article not exist|%s', slug)
        return ObjectNotExistResponse()

    comment = Comment.objects.create(
        article=article,
        username=username,
        email=email,
        avatar=Gravatar(email).get_image(),
        website=website,
        content=content,
        publish_dt=datetime.now(),
        ipv4=ip,
        browser=browser,
        os=os
    )

    logger.info('add comment|%s|%s|%s', article.slug, article.title, comment.username)

    return SuccessResponse()
