from django.urls import path, include
from . import views

v1_urlpatterns = [
    path('query_blogs', views.query_blogs),
]

urlpatterns = [
    path('__import_jekyll_content', views.import_jekyll_content),
    path('api/v1/', include(v1_urlpatterns))
]
