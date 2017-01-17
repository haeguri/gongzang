# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=markdownx.models.MarkdownxField(),
        ),
    ]
