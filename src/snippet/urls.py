from django.urls import path, include
from . import views

v1_urlpatterns = [
    path('snippets', views.SnippetsHandler()),
    path('snippets/<int:id>', views.SnippetHandler())
]

urlpatterns = [
    path('api/v1/', include(v1_urlpatterns))
]
