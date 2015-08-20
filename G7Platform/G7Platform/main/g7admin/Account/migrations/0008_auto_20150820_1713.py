# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0007_auto_20150820_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='nickname',
            field=models.CharField(default='71fba09a7bd546d89b9dd7eedb8c5fa2', verbose_name='昵称', blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(default='700054249fad44d5b96c39edcba92272', verbose_name='用户ID', blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(default='b7a7a187a4df476eaef6cfc933b9ee82', verbose_name='用户登陆标识', blank=True, max_length=100),
        ),
    ]
