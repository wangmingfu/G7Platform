# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0003_auto_20150710_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(blank=True, max_length=100, default='f6aab266a45b45e6bcd2e60e46734770', verbose_name='用户ID'),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(blank=True, max_length=100, default='122dd9002a944bb5a9044a309730848e', verbose_name='用户登陆标识'),
        ),
    ]
