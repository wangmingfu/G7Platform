# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0008_auto_20150820_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='nickname',
            field=models.CharField(max_length=255, default='b1200797ce0540729046925242301f6e', blank=True, verbose_name='昵称'),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(max_length=100, default='4b4b37c1296c43869be9940a356d8e76', blank=True, verbose_name='用户ID'),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(max_length=100, default='6b9462f6d3104a328a01780b420dcd38', blank=True, verbose_name='用户登陆标识'),
        ),
    ]
