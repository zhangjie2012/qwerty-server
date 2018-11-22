from django.contrib import admin
from .models import MicroBlog


class MicroBlogAdmin(admin.ModelAdmin):
    list_display = ('content', 'publish_dt')
    fields = ('cover_img', 'content')


admin.site.register(MicroBlog, MicroBlogAdmin)
