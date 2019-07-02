from django.urls import path, include
from . import views

v1_urlpatterns = [
    path('topics', views.Topics()),
    path('comments', views.Comments())
]

urlpatterns = [
    path('api/v1/', include(v1_urlpatterns))
]
