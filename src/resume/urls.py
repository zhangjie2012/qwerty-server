from django.urls import path, include
from . import views

v1_urlpatterns = [
    path('resume', views.ResumeHandler()),
]

urlpatterns = [
    path('api/v1/', include(v1_urlpatterns))
]
