# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0026_auto_20150807_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(default='dc502da3f9ea473584a503073d59e4d7', max_length=100, blank=True, verbose_name='用户ID'),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(default='4feeed5042f74a3caa70d911093def3b', max_length=100, blank=True, verbose_name='用户登陆标识'),
        ),
    ]
