# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0008_auto_20150807_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(verbose_name='用户ID', blank=True, max_length=100, default='5d15935dbf814885924a3bfbfd9665f2'),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(verbose_name='用户登陆标识', blank=True, max_length=100, default='26480844ff964edda0ed2e2704413afd'),
        ),
    ]
