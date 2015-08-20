# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_auto_20150820_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(max_length=100, default='70c06798ad6a487cb3c3dffcf9950687', verbose_name='用户ID', blank=True),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(max_length=100, default='15bbb628739142eebd70efa4f1398227', verbose_name='用户登陆标识', blank=True),
        ),
    ]
