# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0038_auto_20150807_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(blank=True, max_length=100, verbose_name='用户ID', default='c6d68694f32a41918d23287a6947f3b1'),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(blank=True, max_length=100, verbose_name='用户登陆标识', default='f55e006502344438a1c7eb3fa2e10cab'),
        ),
    ]
