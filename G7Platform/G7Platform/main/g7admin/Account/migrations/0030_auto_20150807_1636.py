# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0029_auto_20150807_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(blank=True, max_length=100, verbose_name='用户ID', default='451016da56cd448f8b0353ce3b715b17'),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(blank=True, max_length=100, verbose_name='用户登陆标识', default='604c64a0eccc4ef3970ae6dc59134cc5'),
        ),
    ]
