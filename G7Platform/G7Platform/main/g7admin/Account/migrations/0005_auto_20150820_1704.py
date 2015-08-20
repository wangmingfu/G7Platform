# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0004_auto_20150820_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(blank=True, max_length=100, default='b1ba6b6351d245289ecc6867a41c3c8d', verbose_name='用户ID'),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(blank=True, max_length=100, default='95356b51ff2f4c5b91dcc99faf582463', verbose_name='用户登陆标识'),
        ),
    ]
