from django.contrib import admin
from .models import Snippet


@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'pl_tag', 'publish_dt', 'update_dt')
    fields = ('title', 'desc', 'code', 'pl_tag')
    search_fields = ('id', 'name', 'pl_tag')
    list_per_page = 25
