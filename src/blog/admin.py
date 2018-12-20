from django.contrib import admin
from .models import Category, Article, Comment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    fields = ('name', 'slug')


admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'publish_dt', 'update_dt', 'draft')


admin.site.register(Article, ArticleAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'article', 'email', 'publish_dt', 'show', 'ipv4')


admin.site.register(Comment, CommentAdmin)
