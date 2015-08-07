# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0011_auto_20150807_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(verbose_name='用户ID', max_length=100, default='a91da699d7f14426a10e35c0165b2d48', blank=True),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(verbose_name='用户登陆标识', max_length=100, default='03c138dd1d63482a9e5ec02a7da11dea', blank=True),
        ),
    ]
