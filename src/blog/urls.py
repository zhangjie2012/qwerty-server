from django.urls import path, include
from . import views

v1_urlpatterns = [
    path('query_blogs', views.query_blogs),
    path('query_blog_detail', views.query_blog_detail),
    path('query_archive_blogs', views.query_archive_blogs),
    path('query_blog_categories', views.query_blog_categories),
    path('add_comment', views.add_comment),
]

urlpatterns = [
    path('api/v1/', include(v1_urlpatterns))
]
