from django.urls import path, include
from . import views

v1_urlpatterns = [
    path('query_resume', views.query_resume),
]

urlpatterns = [
    path('api/v1/', include(v1_urlpatterns))
]
