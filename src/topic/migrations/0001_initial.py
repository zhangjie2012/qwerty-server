# Generated by Django 2.1.3 on 2018-11-24 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0002_auto_20181122_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(help_text='markdown')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='create datetime')),
                ('article', models.ForeignKey(blank=True, help_text='ideally, every topic will convert to article, then archive it', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rel_article', to='blog.Article')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'ordering': ['create_dt'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('slug', models.CharField(help_text='suggest: lower-case|-|0-9', max_length=100, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='create datetime')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='update datetime')),
                ('archive', models.BooleanField(default=False, help_text="archived topic means this's close topic, will not update", verbose_name='archived topic')),
                ('tags', models.ManyToManyField(to='topic.Tag')),
            ],
            options={
                'verbose_name': 'Topic',
                'verbose_name_plural': 'Topics',
                'ordering': ['-archive', '-update_dt'],
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topic.Topic'),
        ),
    ]
