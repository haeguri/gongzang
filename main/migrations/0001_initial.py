# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='제목', max_length=50)),
                ('body', models.TextField(verbose_name='본문')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(related_name='articles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
