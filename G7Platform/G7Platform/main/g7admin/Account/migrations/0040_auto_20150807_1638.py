# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0039_auto_20150807_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(blank=True, default='4d0821c7e5d7449a94f81745171de5ca', max_length=100, verbose_name='用户ID'),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(blank=True, default='7071f11087614c71945d2fdb16e9bd88', max_length=100, verbose_name='用户登陆标识'),
        ),
    ]
