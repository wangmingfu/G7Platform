# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0010_auto_20150820_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='clientid',
            field=models.CharField(default='446935b60a7b433ca7a982dc7bdc948e', verbose_name='客户端id', blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='job',
            field=models.CharField(default='无业游民', verbose_name='职业', max_length=100),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='nickname',
            field=models.CharField(default='b095671104cc41d6b149e887190d13a5', verbose_name='昵称', blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='realname',
            field=models.CharField(default='暂无', verbose_name='真实姓名', max_length=255),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(default='6392cdbf624f4d7494cb96db021e9fad', verbose_name='用户ID', blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(default='d5cba44052c2441ea04fd402ddf52ea7', verbose_name='用户登陆标识', blank=True, max_length=100),
        ),
    ]
