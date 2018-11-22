from django.urls import path, include
from . import views

v1_urlpatterns = [
    path('query_microblogs', views.query_microblogs),
    path('query_microblog', views.query_microblog),
]

urlpatterns = [
    path('api/v1/', include(v1_urlpatterns))
]
