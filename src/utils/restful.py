import time
import math

from utils.logger import logger
from utils.http_tools import ErrorResponse


def time_passed(timestamp):
    return int(math.floor((time.time() - timestamp) * 1000))  # millisecond


class RESTful:
    """ make Django like a restful-api framework

    resource handler inherit this class and implement corresponding handle method
      if sub-class not implement called `method` use default handler
    """

    def __call__(self, req, *args, **kwargs):
        start_ts = time.time()

        if req.method == 'GET':
            rsp = self.get(req, *args, **kwargs)
        elif req.method == 'POST':
            rsp = self.post(req, *args, **kwargs)
        elif req.method == 'PUT':
            rsp = self.put(req, *args, **kwargs)
        elif req.method == 'DELETE':
            rsp = self.delete(req, *args, **kwargs)
        else:
            rsp = self.match_missing(req, *args, **kwargs)

        logger.debug('hander metrics(ms)|%s|%s|%d', req.path, req.method, time_passed(start_ts))

        return rsp

    def match_missing(self, req):
        return ErrorResponse('not match handler function, method={0}'.format(req.method))

    def get(self, req, *args, **kwargs):
        return self.match_missing(req)

    def post(self, req, *args, **kwargs):
        return self.match_missing(req)

    def put(self, req, *args, **kwargs):
        return self.match_missing(req)

    def delete(self, req, *args, **kwargs):
        return self.match_missing(req)
