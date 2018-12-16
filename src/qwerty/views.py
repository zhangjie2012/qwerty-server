from django.views.decorators.http import require_GET

from utils.env import site_config, user_config
# from utils.logger import logger
from utils.http_tools import SuccessResponse


@require_GET
def health_check(request):
    return SuccessResponse()


@require_GET
def query_site_info(request):
    # logger.debug('query site info|%s', site_config.to_dict())
    return SuccessResponse({
        'site_info': site_config.to_dict()
    })


@require_GET
def query_user_info(request):
    return SuccessResponse({
        'user': user_config.to_dict(),
    })
