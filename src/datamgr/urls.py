from django.urls import path
from . import views

urlpatterns = [
    path('import_jekyll_content', views.import_jekyll_content),
]
