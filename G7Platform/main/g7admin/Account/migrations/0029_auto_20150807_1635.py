# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0028_auto_20150807_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(verbose_name='用户ID', blank=True, max_length=100, default='5f7429c6572a4f339536ee70453164ad'),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(verbose_name='用户登陆标识', blank=True, max_length=100, default='8342d1596dc542758b8ecba104a26a34'),
        ),
    ]
