from django.urls import path
from . import views

urlpatterns = [
    path('__import_jekyll_content', views.import_jekyll_content)
]
