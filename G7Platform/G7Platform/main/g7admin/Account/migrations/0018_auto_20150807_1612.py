# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0017_auto_20150807_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(max_length=100, blank=True, verbose_name='用户ID', default='29f2580e255448b59db831b6120528ef'),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(max_length=100, blank=True, verbose_name='用户登陆标识', default='62da4e2ea70349a28c3685318fbab73d'),
        ),
    ]
