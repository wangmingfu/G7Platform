# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0045_auto_20150807_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(blank=True, verbose_name='用户ID', default='b30acca2c9044fee87991d131fe8b7ff', max_length=100),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(blank=True, verbose_name='用户登陆标识', default='f2cdc24397a54a479c4d5c52a0745a28', max_length=100),
        ),
    ]
