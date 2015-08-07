# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0040_auto_20150807_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(verbose_name='用户ID', max_length=100, default='fab8ff0a091a4abc8bba571d5562bfdc', blank=True),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(verbose_name='用户登陆标识', max_length=100, default='4820f476bf344288ac6b0ede086b3e89', blank=True),
        ),
    ]
