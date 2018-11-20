import os
import json
import yaml
import shutil
import frontmatter

from datetime import datetime
from django.views.decorators.http import require_POST
from utils.logger import logger
from utils.http_tools import SuccessResponse, ParamInvalidResponse, \
    PermissionDeniedResponse
from utils.env import server_config, backup_config
from blog.models import Category, Article, Comment


def require_admin(handler):
    """ all datamgr api need right token, prevent
    1. bad guy call on purpose
    2. self misoperation
    """

    def wrapper(request):
        token = request.GET.get('token')
        if token is None or token != server_config.token:
            return PermissionDeniedResponse()
        else:
            return handler(request)

    return wrapper


@require_POST
@require_admin
def import_jekyll_content(request):
    try:
        data = json.loads(request.body)
        dst_dir = data['dst_dir']
    except (KeyError, json.JSONDecodeError):
        logger.warning('param invalid|%s', request.body.decode('utf-8'))
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


def backup_blog(root_dir):
    # category
    category_path = os.path.join(root_dir, 'category.yml')
    category_qs = Category.objects.all()
    category_list = []
    for category in category_qs:
        category_list.append({
            'name': category.name,
            'slug': category.slug,
        })
    with open(category_path, 'w') as f:
        yaml.dump(category_list, f,
                  default_flow_style=False,
                  encoding='utf-8', allow_unicode=True)
        logger.debug('backup category|%s', category_path)

    # blog
    post_root = os.path.join(root_dir, 'posts')
    os.mkdir(post_root)

    article_qs = Article.objects.all()
    for article in article_qs:
        post = frontmatter.Post(content=article.content)
        post['category_name'] = article.category.name
        post['category_slug'] = article.category.slug
        post['title'] = article.title
        post['slug'] = article.slug
        post['cover_img'] = article.cover_img
        post['img_copyright'] = article.img_copyright
        post['abstract'] = article.abstract
        post['publish_dt'] = article.publish_dt
        post['update_dt'] = article.update_dt
        post['draft'] = article.draft

        file_name = '%s-%s.md' % (article.publish_dt.date(), article.slug)
        article_path = os.path.join(post_root, file_name)
        with open(article_path, 'wb') as f:
            frontmatter.dump(post, f)

        logger.debug('backup article|%s', article_path)

    # comment
    comment_path = os.path.join(root_dir, 'comment.yml')
    comment_qs = Comment.objects.all()
    comment_list = []
    for comment in comment_qs:
        comment_list.append({
            'article_slug': comment.article.slug,
            'username': comment.username,
            'website': comment.website,
            'publish_dt': comment.publish_dt,
            'show': comment.show,
            'ipv4': comment.ipv4,
            'browser': comment.browser,
            'os': comment.os,
        })
    with open(comment_path, 'w') as f:
        yaml.dump(category_list, f,
                  default_flow_style=False,
                  encoding='utf-8', allow_unicode=True)
        logger.debug('backup category|%s', category_path)


@require_admin
def backup_all(request):
    """backup all content to config backup path
    note: backup will clear old dir data !!!

    - blog/:
       post/
       category.yml
    """
    root_dir = backup_config.path

    # remove and create, make sure empty
    shutil.rmtree(root_dir)
    os.makedirs(root_dir)

    backup_blog(root_dir)

    return SuccessResponse()
