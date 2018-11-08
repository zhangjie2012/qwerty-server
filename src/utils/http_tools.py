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
