# Generated by Django 2.1.3 on 2018-11-07 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.CharField(help_text='suggest: lower-case, -, 0-9', max_length=100, unique=True)),
                ('cover_img', models.CharField(blank=True, help_text='your article cover image', max_length=1000)),
                ('img_copyright', models.CharField(blank=True, help_text='image copyright notice', max_length=100)),
                ('abstract', models.TextField(blank=True, help_text='article abstract: txt not markdown')),
                ('content', models.TextField(help_text='markdown')),
                ('publish_dt', models.DateTimeField(db_index=True)),
                ('update_dt', models.DateTimeField(db_index=True)),
                ('draft', models.BooleanField(db_index=True, default=False, help_text='draft article will hidden')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
                'ordering': ['-publish_dt'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('slug', models.CharField(max_length=100, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('website', models.CharField(blank=True, max_length=100)),
                ('content', models.TextField()),
                ('publish_dt', models.DateTimeField(auto_now_add=True)),
                ('show', models.BooleanField(default=False)),
                ('ipv4', models.CharField(blank=True, max_length=15)),
                ('browser', models.CharField(blank=True, max_length=100)),
                ('os', models.CharField(blank=True, max_length=100)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Article')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'ordering': ['-publish_dt'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.Category'),
        ),
    ]