# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0006_auto_20150820_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(default='b60f2bdf086e491080bd7e75736ed323', max_length=100, verbose_name='用户ID', blank=True),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(default='83b85554a55d4922956018c0468a8124', max_length=100, verbose_name='用户登陆标识', blank=True),
        ),
    ]
