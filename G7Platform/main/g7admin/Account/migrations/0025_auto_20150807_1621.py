# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0024_auto_20150807_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(blank=True, verbose_name='用户ID', default='a0410d3867654ff384eca4b4f47a926a', max_length=100),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(blank=True, verbose_name='用户登陆标识', default='a04ff51558e44b2697323292b1134d18', max_length=100),
        ),
    ]
