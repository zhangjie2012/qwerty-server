from django.urls import path, include
from . import views

v1_urlpatterns = [
    path('query_topics', views.query_topics),
    path('query_topic_comments', views.query_topic_comments),
]

urlpatterns = [
    path('api/v1/', include(v1_urlpatterns))
]
