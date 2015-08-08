# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0047_auto_20150807_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(verbose_name='用户ID', default='d207976a21ab4a90aa8543b786e88cb3', blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(verbose_name='用户登陆标识', default='58727b47e9c2482497aa467015fb9116', blank=True, max_length=100),
        ),
    ]
