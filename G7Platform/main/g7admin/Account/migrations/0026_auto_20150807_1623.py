# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0025_auto_20150807_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(verbose_name='用户ID', default='cab1a023c3de4be7a63f32a1ec915996', blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(verbose_name='用户登陆标识', default='de2dbc9229344173af051deef776246e', blank=True, max_length=100),
        ),
    ]
