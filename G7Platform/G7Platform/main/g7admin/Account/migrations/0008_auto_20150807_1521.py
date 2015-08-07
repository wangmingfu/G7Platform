# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0007_auto_20150807_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(blank=True, default='ece414f2cd6f4e5abc3d3309550123ed', verbose_name='用户ID', max_length=100),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(blank=True, default='e0a9e35424fa4458969dc7769eddff74', verbose_name='用户登陆标识', max_length=100),
        ),
    ]
