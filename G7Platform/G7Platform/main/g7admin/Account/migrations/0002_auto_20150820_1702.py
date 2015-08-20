# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(blank=True, verbose_name='用户ID', default='3add998dd7394e98ac11fb7ed9e3c527', max_length=100),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(blank=True, verbose_name='用户登陆标识', default='1953f3e79ebd4e598db242c48126d9bf', max_length=100),
        ),
    ]
