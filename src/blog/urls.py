from django.urls import path, include
from . import views

v1_urlpatterns = [
    path('blogs', views.Blogs()),
    path('blogs/<str:slug>', views.Blog()),
    path('categories', views.Categories()),
    path('archives', views.Archives()),
    path('comments', views.Comments())
]

urlpatterns = [
    path('api/v1/', include(v1_urlpatterns))
]
