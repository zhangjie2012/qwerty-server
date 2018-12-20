from django.db import models


class Category(models.Model):
    name = models.CharField('name', max_length=100, unique=True)
    slug = models.CharField('slug', max_length=100, unique=True,
                            help_text='suggest: lower-case|-|0-9')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Article(models.Model):
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True,
                            help_text='suggest: lower-case|-|0-9')

    # article cover image
    cover_img = models.CharField('cover image', max_length=1000, blank=True,
                                 help_text='your article cover image')
    img_copyright = models.CharField('copyright', max_length=100, blank=True,
                                     help_text='image copyright notice')

    abstract = models.TextField(blank=True,
                                help_text='article abstract: txt not markdown')
    content = models.TextField(help_text='markdown')

    # notes: can not use `auto_now` or `auto_now_add`,
    #   we want user can manual set its value
    #   sometimes, we don't hope the date is real date
    publish_dt = models.DateTimeField('publish date', db_index=True)
    update_dt = models.DateTimeField('update date', db_index=True)

    draft = models.BooleanField(default=False, db_index=True,
                                help_text='draft article will hidden')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-publish_dt']


class Comment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE)

    username = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    avatar = models.URLField(default='https://www.gravatar.com/avatar/00000000000000000000000000000000')
    website = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    publish_dt = models.DateTimeField(auto_now_add=True)

    show = models.BooleanField(default=False)

    ipv4 = models.CharField(max_length=15, blank=True)
    browser = models.CharField(max_length=100, blank=True)
    os = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-publish_dt']
