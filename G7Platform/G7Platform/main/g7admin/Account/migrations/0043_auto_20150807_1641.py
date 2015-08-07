# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0042_auto_20150807_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(default='d05bcd75ae414ce693150957e85601d6', blank=True, max_length=100, verbose_name='用户ID'),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(default='ac0a0bed0bf443e988d29cfa6eff0dd2', blank=True, max_length=100, verbose_name='用户登陆标识'),
        ),
    ]
