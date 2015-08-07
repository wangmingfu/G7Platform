# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0033_auto_20150807_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(max_length=100, verbose_name='用户ID', default='f78d6b5768f44cc3bcf6619d15023a66', blank=True),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(max_length=100, verbose_name='用户登陆标识', default='b3b3a1889f944ebea878352462b85825', blank=True),
        ),
    ]
