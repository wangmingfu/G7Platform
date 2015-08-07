# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0044_auto_20150807_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(blank=True, verbose_name='用户ID', max_length=100, default='c6d7819dc19d4bcbb3ef411f4e135515'),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(blank=True, verbose_name='用户登陆标识', max_length=100, default='a5ebe3b61f6640d8a68cdb0ddb05acf7'),
        ),
    ]
