from django.http import JsonResponse


HTTP_OK = 'ok'
HTTP_ERROR = 'error'


def SuccessResponse(data=None):
    return JsonResponse({'status': HTTP_OK}) \
        if data is None else JsonResponse({'status': HTTP_OK, 'data': data})


def ParamInvalidResponse():
    return JsonResponse({
        'status': HTTP_ERROR,
        'message': 'request param invalid'
    })


def ObjectNotExistResponse():
    return JsonResponse({
        'status': HTTP_ERROR,
        'message': 'object not exist'
    })


def PermissionDeniedResponse():
    return JsonResponse({
        'status': HTTP_ERROR,
        'message': 'permission denied'
    })


def get_client_info(request):
    """return: ip, browser, os, device
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    from user_agents import parse

    ua_string = request.META['HTTP_USER_AGENT']
    user_agent = parse(ua_string)

    browser = '{0}({1})'.format(
        user_agent.browser.family, user_agent.browser.version_string)
    os = '{0}({1})'.format(user_agent.os.family, user_agent.os.version_string)
    device = '{0}-{1}-{2}'.format(
        user_agent.device.family, user_agent.device.brand, user_agent.device.model)

    return ip, browser, os, device
