# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0003_auto_20150820_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(max_length=100, default='af064384b19443eea1fabacaa31f416e', verbose_name='用户ID', blank=True),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(max_length=100, default='7e9e098709f34c99b7b92f5ef3978359', verbose_name='用户登陆标识', blank=True),
        ),
    ]
