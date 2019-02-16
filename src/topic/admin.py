from django.contrib import admin
from .models import Topic, Comment


class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'archive', 'pin', 'update_dt')
    fields = ('title', 'archive', 'pin')
    search_fields = ['id', 'title']
    list_per_page = 25


admin.site.register(Topic, TopicAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic', 'create_dt')
    fields = ('topic', 'content')
    search_fields = ['id', 'topic__title']
    list_per_page = 25


admin.site.register(Comment, CommentAdmin)
