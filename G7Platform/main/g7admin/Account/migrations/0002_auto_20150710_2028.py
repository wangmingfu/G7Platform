# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(verbose_name='用户ID', max_length=100, blank=True, default='6411b244565d4cdb8e3d15eca4f4cad6'),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(verbose_name='用户登陆标识', max_length=100, blank=True, default='a5ab5aac48434562abc9f2ad4a86d731'),
        ),
    ]
