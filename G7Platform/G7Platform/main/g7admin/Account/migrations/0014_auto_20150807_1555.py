# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0013_auto_20150807_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(verbose_name='用户ID', blank=True, default='a373dffe21b64b4d97ed67f7f3b57f0f', max_length=100),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(verbose_name='用户登陆标识', blank=True, default='65006cf767eb42689c9e3496a7ec17c8', max_length=100),
        ),
    ]
