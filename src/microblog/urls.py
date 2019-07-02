from django.urls import path, include
from . import views

v1_urlpatterns = [
    path('microblogs', views.MicroBlogs()),
    path('microblogs/<int:id>', views.MicroBlogHandler())
]

urlpatterns = [
    path('api/v1/', include(v1_urlpatterns))
]
