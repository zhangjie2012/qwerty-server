from utils.restful import RESTful
from utils.logger import logger
from utils.http_tools import SuccessResponse, ObjectNotExistResponse

from .models import Snippet


class SnippetsHandler(RESTful):
    def get(self, request):
        snippet_qs = Snippet.objects.order_by('-update_dt')
        snippet_list = []
        for snippet in snippet_qs:
            snippet_list.append(snippet.to_dict())

        logger.debug('query snippets')
        return SuccessResponse(snippet_list)


class SnippetHandler(RESTful):
    def get(self, request, id):
        try:
            snippet = Snippet.objects.get(id=id)
        except Snippet.DoesNotExist:
            logger.warning('snippet not exist|%d', id)
            return ObjectNotExistResponse()

        logger.debug('query snippet|%d', id)
        return SuccessResponse(snippet)
