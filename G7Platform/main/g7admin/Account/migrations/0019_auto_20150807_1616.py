# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0018_auto_20150807_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(default='2701031151d8421eb413fdaa4bf9467c', blank=True, max_length=100, verbose_name='用户ID'),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(default='9b0dcaa2b84c4989973f84945bd1f30f', blank=True, max_length=100, verbose_name='用户登陆标识'),
        ),
    ]
