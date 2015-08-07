# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0020_auto_20150807_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(max_length=100, verbose_name='用户ID', blank=True, default='8921b4e2c0884b9f9d68b73cb3e264a2'),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(max_length=100, verbose_name='用户登陆标识', blank=True, default='4fa0a4973f764287af6d2e486d581260'),
        ),
    ]
