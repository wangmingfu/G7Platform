# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0036_auto_20150807_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(max_length=100, verbose_name='用户ID', blank=True, default='e876c088cc3543f688fd382382a32b5f'),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(max_length=100, verbose_name='用户登陆标识', blank=True, default='6389ca50c611448c822b4d8b7f91fb49'),
        ),
    ]
