from django.views.decorators.http import require_GET

from utils.env import site_config, user_config
from utils.restful import RESTful
# from utils.logger import logger
from utils.http_tools import SuccessResponse


@require_GET
def health_check(request):
    return SuccessResponse()


class Site(RESTful):
    def get(self, req):
        # logger.debug('query site info|%s', site_config.to_dict())
        return SuccessResponse(site_config.to_dict())


class User(RESTful):
    def get(self, req):
        return SuccessResponse(user_config.to_dict())
