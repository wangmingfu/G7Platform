# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0004_auto_20150720_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(blank=True, default='4a9f7fddd898478b9d37fde1396f247c', verbose_name='用户ID', max_length=100),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(blank=True, default='4583d0d7dc7b4186b203872872e1f378', verbose_name='用户登陆标识', max_length=100),
        ),
    ]
