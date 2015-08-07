# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0031_auto_20150807_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(verbose_name='用户ID', default='ee75506096674ddb8b0a7b0cc0ed4ebd', blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(verbose_name='用户登陆标识', default='82b22bfa1849439fb7bef0c94e1f6ff5', blank=True, max_length=100),
        ),
    ]
