from django.views.decorators.http import require_GET

from utils import env
from utils.logger import logger
from utils.http_tools import SuccessResponse


@require_GET
def query_site_info(request):
    logger.debug('query site info|%s', env.get_site_info())
    return SuccessResponse({
        'site_info': env.get_site_info(),
    })
