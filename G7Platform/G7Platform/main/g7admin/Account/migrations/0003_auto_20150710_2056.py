# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_auto_20150710_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(default='d77bcc644e6b4526a2a8dd01c82cfa0a', blank=True, max_length=100, verbose_name='用户ID'),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(default='9d83da6c60c044e4945abc302284cfc3', blank=True, max_length=100, verbose_name='用户登陆标识'),
        ),
    ]
