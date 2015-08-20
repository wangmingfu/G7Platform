# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0002_auto_20150820_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='g7project',
            name='bunldeID',
            field=models.CharField(verbose_name='标识符(BundleID)', default='', max_length=200, unique=True, blank=True, null=True),
        ),
    ]
