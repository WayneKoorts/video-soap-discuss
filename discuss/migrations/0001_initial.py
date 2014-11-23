# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, unique=True)),
                ('createdTimestamp', models.DateTimeField(auto_now_add=True)),
                ('viewCount', models.PositiveIntegerField()),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('createdTimestamp', models.DateTimeField(auto_now_add=True)),
                ('modifiedTimestamp', models.DateTimeField(auto_now=True)),
                ('postType', models.PositiveIntegerField(choices=[(0, 'Video'), (1, 'Audio'), (2, 'Text')], blank=True)),
                ('mediaUrl', models.URLField()),
                ('text', models.TextField()),
                ('discussion', models.ForeignKey(related_name='posts', to='discuss.Discussion')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RelatedLink',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('post', models.ForeignKey(to='discuss.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('createdTimestamp', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transcription',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('lastEditedBy', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('post', models.OneToOneField(blank=True, to='discuss.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='discussion',
            name='subject',
            field=models.ForeignKey(related_name='discussions', to='discuss.Subject'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='discussion',
            name='tags',
            field=models.ManyToManyField(to='discuss.Tag'),
            preserve_default=True,
        ),
    ]
