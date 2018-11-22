from django.db import models


class MicroBlog(models.Model):
    cover_img = models.URLField(blank=True)
    content = models.TextField(help_text='text, not markdown')
    publish_dt = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'MicroBlog'
        verbose_name_plural = 'MicroBlogs'
        ordering = ['-publish_dt']
