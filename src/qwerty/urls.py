"""qwerty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('__adm/', admin.site.urls),
    path('health_check', views.health_check),

    path('site', views.Site()),
    path('user', views.User()),

    path('blog/', include('blog.urls')),
    path('snippet/', include('snippet.urls')),
    path('topic/', include('topic.urls')),
    path('microblog/', include('microblog.urls')),
    path('resume/', include('resume.urls')),
]
