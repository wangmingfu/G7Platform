# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0009_auto_20150807_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(default='bacb17a562934f44a6f033746332bc15', blank=True, verbose_name='用户ID', max_length=100),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(default='201e229d084a409f80be2441c410cbb8', blank=True, verbose_name='用户登陆标识', max_length=100),
        ),
    ]
