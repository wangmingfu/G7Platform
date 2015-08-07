# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0012_auto_20150807_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(verbose_name='用户ID', blank=True, max_length=100, default='b3d18049176b40ba813c1ba79e22a1fa'),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(verbose_name='用户登陆标识', blank=True, max_length=100, default='c6f545f9f6ef43dca3a9938eda787785'),
        ),
    ]
