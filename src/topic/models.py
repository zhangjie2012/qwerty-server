from django.db import models


class Topic(models.Model):
    title = models.CharField(max_length=100)

    create_dt = models.DateTimeField('create datetime', auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', auto_now=True)

    pin = models.BooleanField(
        'Pushpin topic',
        default=False,
        help_text='push pin topic will sort at first'
    )

    archive = models.BooleanField(
        'archived topic',
        default=False,
        help_text='archived topic means this\'s close topic, will not update'
    )

    pv = models.IntegerField('page views', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'
        ordering = ('archive', '-pin', 'title')


class Comment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    content = models.TextField(help_text='markdown')
    create_dt = models.DateTimeField('create datetime', auto_now_add=True)

    def __str__(self):
        return self.topic.title

    def save(self, *args, **kwargs):
        self.topic.save()  # update topic `update_dt`
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-create_dt']
