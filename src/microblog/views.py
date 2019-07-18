import mistune

from django.core.paginator import Paginator

from utils.logger import logger
from utils.env import user_config
from utils.http_tools import SuccessResponse, ParamInvalidResponse, ObjectNotExistResponse
from utils.restful import RESTful

from .models import MicroBlog


class MicroBlogs(RESTful):
    def get(self, request):
        page = int(request.GET.get('page', 1))
        per_count = int(request.GET.get('per_count', 25))

        page = 1 if page < 1 else page
        per_count = 10 if per_count < 1 else per_count

        microblog_qs = MicroBlog.objects.all()

        paginator = Paginator(microblog_qs, per_count)
        page_microblog = paginator.get_page(page)

        microblog_list = []
        for microblog in page_microblog.object_list:
            microblog_list.append({
                'id': microblog.id,
                'cover_img': microblog.cover_img,
                'content': mistune.markdown(microblog.content),
                'publish_dt': microblog.publish_dt,
            })

        logger.debug('query microblogs|%s|%s|%s', page, per_count, len(microblog_list))

        return SuccessResponse({
            'avatar': user_config.avatar,
            'microblog_list': microblog_list,
            'current_page_num': page_microblog.number,
            'total_pages': paginator.num_pages,
            'total_count': paginator.count,
        })


class MicroBlogHandler(RESTful):
    def get(self, request, id):
        id_ = id
        try:
            microblog = MicroBlog.objects.get(id=id_)
        except MicroBlog.DoesNotExist:
            logger.warning('microblog not exist|%d', id_)
            return ObjectNotExistResponse()

        logger.debug('query microblog|%d', id_)

        return SuccessResponse({
            'id': microblog.id,
            'cover_img': microblog.cover_img,
            'content': microblog.content,
            'publish_dt': microblog.publish_dt,
        })
