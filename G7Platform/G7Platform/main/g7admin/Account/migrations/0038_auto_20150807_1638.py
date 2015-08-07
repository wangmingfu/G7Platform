# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0037_auto_20150807_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(blank=True, verbose_name='用户ID', default='49e455a3df54402ab3a05254ec0df29d', max_length=100),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(blank=True, verbose_name='用户登陆标识', default='214d9610059f4d37a9b375e20924c5df', max_length=100),
        ),
    ]
