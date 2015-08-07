# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0035_auto_20150807_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(default='0c9a98fdaa0f4baf9274ae0f5399582b', blank=True, verbose_name='用户ID', max_length=100),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(default='f4344768ee7349b7a3348cce862460d9', blank=True, verbose_name='用户登陆标识', max_length=100),
        ),
    ]
