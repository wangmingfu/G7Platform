# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0030_auto_20150807_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(max_length=100, verbose_name='用户ID', blank=True, default='7727beb2f38b4b368bb4747c5c257a45'),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(max_length=100, verbose_name='用户登陆标识', blank=True, default='f8bf31d3cbd141fbb63ee86086458f17'),
        ),
    ]
