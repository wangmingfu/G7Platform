# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0041_auto_20150807_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(blank=True, max_length=100, verbose_name='用户ID', default='de7c1b72a32c4f28b35186b16a06d531'),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(blank=True, max_length=100, verbose_name='用户登陆标识', default='e8f3ab6d8367474e9dbd3e6949c4345e'),
        ),
    ]
