# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0005_auto_20150721_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(max_length=100, default='6ee4a58fe705461681c5d416ee53b0a9', blank=True, verbose_name='用户ID'),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(max_length=100, default='59dd14c199b142dea30886d428dea73b', blank=True, verbose_name='用户登陆标识'),
        ),
    ]
