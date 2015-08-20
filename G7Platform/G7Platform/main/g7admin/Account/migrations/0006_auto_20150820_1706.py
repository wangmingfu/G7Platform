# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0005_auto_20150820_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(max_length=100, blank=True, default='69d6746f2e904c63bc49f663bcf0690e', verbose_name='用户ID'),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(max_length=100, blank=True, default='2c32c830adeb42d0ac40c3a339721078', verbose_name='用户登陆标识'),
        ),
    ]
