from django.db.models import Count

from utils.restful import RESTful
from utils.logger import logger
from utils.http_tools import SuccessResponse, ObjectNotExistResponse

from .models import Snippet


class SnippetsHandler(RESTful):
    def get(self, request):
        snippet_qs = Snippet.objects.order_by('-update_dt')
        snippet_list = []
        for snippet in snippet_qs:
            snippet_list.append(snippet.to_simple_dict())

        logger.debug('query snippets|%s', len(snippet_list))
        return SuccessResponse(snippet_list)


class SnippetHandler(RESTful):
    def get(self, request, id):
        try:
            snippet = Snippet.objects.get(id=id)
        except Snippet.DoesNotExist:
            logger.warning('snippet not exist|%d', id)
            return ObjectNotExistResponse()

        logger.debug('query snippet|%d', id)
        return SuccessResponse(snippet.to_dict())


class SnippetTagsHandler(RESTful):
    def get(self, request):
        tags = Snippet.objects.values('pl_tag').annotate(
            count=Count('pl_tag')).order_by('pl_tag').distinct()
        logger.debug('query tag|%s', len(tags))
        return SuccessResponse(list(tags))
