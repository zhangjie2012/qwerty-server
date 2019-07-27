import mistune

from django.db import models

hljs_link = 'https://github.com/conorhastings/react-syntax-highlighter/blob/master/AVAILABLE_LANGUAGES_PRISM.MD'


class Snippet(models.Model):
    title = models.CharField('title', max_length=100)
    desc = models.TextField('desc', blank=True, help_text='support markdown')
    code = models.TextField('code', help_text='pure code')
    pl_tag = models.CharField('programming language tag', max_length=20, help_text=hljs_link, db_index=True)
    publish_dt = models.DateTimeField('publish date', db_index=True, auto_now_add=True)
    update_dt = models.DateTimeField('update date', db_index=True, auto_now=True)

    def __str__(self):
        return self.title

    def to_dist(self):
        return {
            'id': self.id,
            'title': self.title,
            'desc': '' if len(self.desc) == 0 else mistune.markdown(self.desc),
            'code': self.code,
            'pl_tag': self.pl_tag,
            'publish_dt': self.publish_dt,
            'update_dt': self.update_dt,
        }

    class Meta:
        verbose_name = 'Snippet'
        verbose_name_plural = 'Snippets'
        ordering = ('-publish_dt',)
