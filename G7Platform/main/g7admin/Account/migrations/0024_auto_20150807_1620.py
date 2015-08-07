# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0023_auto_20150807_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(default='44e161f9c4a34b51b2bbdb6313130770', blank=True, verbose_name='用户ID', max_length=100),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(default='39c946d4485e4f26b80e842a339e5be9', blank=True, verbose_name='用户登陆标识', max_length=100),
        ),
    ]
