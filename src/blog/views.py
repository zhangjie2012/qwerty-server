import os
import json
import frontmatter

from datetime import datetime
from django.views.decorators.http import require_POST
from utils.logger import logger
from utils.http_tools import SuccessResponse, ParamInvalidResponse
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
