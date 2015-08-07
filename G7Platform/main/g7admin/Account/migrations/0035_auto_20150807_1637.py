# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0034_auto_20150807_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(max_length=100, default='540ff1c8190e4cbfbcef103ee3ba63ce', blank=True, verbose_name='用户ID'),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(max_length=100, default='0d0f054b244349689ee1f8b0614d6764', blank=True, verbose_name='用户登陆标识'),
        ),
    ]
