# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0015_auto_20150807_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(default='6db6b2a5845e458da3ce50418ca3ce84', blank=True, verbose_name='用户ID', max_length=100),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(default='f1332fedf5be4ebe88abda1a2b6488a7', blank=True, verbose_name='用户登陆标识', max_length=100),
        ),
    ]
