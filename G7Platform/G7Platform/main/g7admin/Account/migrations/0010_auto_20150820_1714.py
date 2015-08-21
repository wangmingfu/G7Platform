# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0009_auto_20150820_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='clientid',
            field=models.CharField(max_length=100, verbose_name='客户端id', blank=True, default='e5abb7cc62464d649bea96a9949b912e'),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='nickname',
            field=models.CharField(max_length=255, verbose_name='昵称', blank=True, default='2152fc8aa8444f6e82879b242392aa13'),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(max_length=100, verbose_name='用户ID', blank=True, default='3c0ded8ae7d340a49cf84d89a4282180'),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(max_length=100, verbose_name='用户登陆标识', blank=True, default='134f46e2b66f40d38ca92e8e548da2e7'),
        ),
    ]
