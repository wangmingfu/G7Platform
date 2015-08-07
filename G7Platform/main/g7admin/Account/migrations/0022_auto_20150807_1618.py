# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0021_auto_20150807_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(default='24bd5bcbaa4947fc821e95023a3f658d', verbose_name='用户ID', blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(default='995b4adea2254f92b6bcb02a855d07ab', verbose_name='用户登陆标识', blank=True, max_length=100),
        ),
    ]
