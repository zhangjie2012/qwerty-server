from django.contrib import admin
from .models import Tag, Topic, Comment


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'color')
    fields = ('name', 'slug', 'color')
    search_fields = ['name', 'slug']
    list_per_page = 25


admin.site.register(Tag, TagAdmin)


class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'tags_admin_label', 'archive', 'pin', 'update_dt')
    fields = ('title', 'tags', 'archive', 'pin')
    search_fields = ['id', 'title']
    list_per_page = 25


admin.site.register(Topic, TopicAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic', 'article', 'create_dt')
    fields = ('topic', 'content', 'article')
    search_fields = ['id', 'topic__title']
    list_per_page = 25


admin.site.register(Comment, CommentAdmin)
