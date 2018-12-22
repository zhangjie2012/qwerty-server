from django.contrib import admin
from .models import Category, Article, Comment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    fields = ('name', 'slug')
    search_fields = ['name']
    list_per_page = 25


admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'publish_dt', 'update_dt', 'draft')
    search_fields = ['title', 'category__name']
    list_per_page = 25


admin.site.register(Article, ArticleAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'article', 'email', 'publish_dt', 'show', 'ipv4')
    search_fields = ['username', 'article__title', 'email', 'ipv4']


admin.site.register(Comment, CommentAdmin)
