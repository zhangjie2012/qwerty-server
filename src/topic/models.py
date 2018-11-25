from django.db import models


class Tag(models.Model):
    name = models.CharField('name', max_length=100, unique=True)
    slug = models.CharField('slug', max_length=100, unique=True,
                            help_text='suggest: lower-case|-|0-9')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Topic(models.Model):
    title = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag, blank=True)

    create_dt = models.DateTimeField('create datetime', auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', auto_now=True)

    archive = models.BooleanField(
        'archived topic',
        default=False,
        help_text='archived topic means this\'s close topic, will not update'
    )

    def tags_admin_label(self):
        return ','.join(list(self.tags.values_list('name', flat=True)))

    def tags_dict(self):
        return list(self.tags.values('name', 'slug'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'
        ordering = ('archive', '-update_dt')


class Comment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    content = models.TextField(help_text='markdown')
    article = models.ForeignKey(
        'blog.article',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text='ideally, every topic will convert to article, then archive it',
        related_name='rel_article',
    )
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
