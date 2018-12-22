from django.contrib import admin
from .models import Tag, Topic, Comment


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'color')
    fields = ('name', 'slug', 'color')


admin.site.register(Tag, TagAdmin)


class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'tags_admin_label', 'archive', 'pin', 'update_dt')
    fields = ('title', 'tags', 'archive', 'pin')


admin.site.register(Topic, TopicAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic', 'article', 'create_dt')
    fields = ('topic', 'content', 'article')


admin.site.register(Comment, CommentAdmin)
