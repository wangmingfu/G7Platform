# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0004_auto_20150820_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='g7project',
            name='product_id',
            field=models.IntegerField(default=0, verbose_name='产品id'),
        ),
    ]
