# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0019_auto_20150807_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(max_length=100, default='faf2e02eae5247429cb6442a9106b963', verbose_name='用户ID', blank=True),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(max_length=100, default='9f93fc3dd80943dc998750109c5236d1', verbose_name='用户登陆标识', blank=True),
        ),
    ]
