# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0022_auto_20150807_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(default='9252d4d1fabe413991d239887fff001d', max_length=100, verbose_name='用户ID', blank=True),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(default='bf1d0a8455854ef0b1cf2ddd9684bbc3', max_length=100, verbose_name='用户登陆标识', blank=True),
        ),
    ]
