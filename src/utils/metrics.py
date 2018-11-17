import os
import time
from prometheus_client import Histogram, CollectorRegistry, Counter, generate_latest

pid = os.getpid()
registry = CollectorRegistry()
api_histogram = Histogram(
    'qwerty_api_latency_seconds',
    'querty api time spent processing request',
    ['processid', 'method', 'api_name'],
    registry=registry
)
article_counter = Counter(
    'article_visit_counter',
    'user visiter article counter',
    ['processid', 'slug', 'client_ip'],
    registry=registry
)


def api_metric(func):

    def wrapper(*args, **kwargs):

        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        method, api_name = args[0].method, func.__name__
        api_histogram.labels(pid, method, api_name).observe(end-start)
        return result

    return wrapper


def article_visite_metric(slug, client_ip):
    article_counter.labels(pid, slug, client_ip).inc()


def handler(request):
    from django.http import HttpResponse
    text = generate_latest(registry)
    return HttpResponse(text, content_type="text/plain")
