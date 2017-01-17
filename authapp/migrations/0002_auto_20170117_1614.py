# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(unique=True, max_length=255, verbose_name='이메일'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=50, verbose_name='이름'),
        ),
    ]
