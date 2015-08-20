# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0005_g7project_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7project',
            name='latest_build_version',
            field=models.IntegerField(null=True, default=0, verbose_name='最新编译版本', blank=True),
        ),
        migrations.AlterField(
            model_name='g7project',
            name='latest_inner_version',
            field=models.IntegerField(null=True, default=0, verbose_name='最新内部版本', blank=True),
        ),
        migrations.AlterField(
            model_name='g7project',
            name='latest_version',
            field=models.CharField(null=True, default='0.0', max_length=200, verbose_name='最新版本', blank=True),
        ),
    ]
