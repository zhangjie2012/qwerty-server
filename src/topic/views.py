from django.views.decorators.http import require_GET

from utils.metrics import api_metric
from utils.http_tools import SuccessResponse
from utils.logger import logger

from .models import Topic


@require_GET
@api_metric
def query_topics(request):
    topic_qs = Topic.objects.all()
    topic_list = []
    for topic in topic_qs:
        topic_list.append({
            'id': topic.id,
            'title': topic.title,
            'tags': topic.tags_dict(),
            'create_dt': topic.create_dt,
            'update_dt': topic.update_dt,
            'archive': topic.archive,
            'comment_count': topic.comment_set.count(),
        })
    logger.debug('query topics|%s', len(topic_list))
    return SuccessResponse(topic_list)
