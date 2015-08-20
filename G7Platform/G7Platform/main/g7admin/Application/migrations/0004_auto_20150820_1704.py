# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0003_g7project_bunldeid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7project',
            name='bunldeID',
            field=models.CharField(unique=True, max_length=200, default='', verbose_name='标识符(BundleID)'),
        ),
    ]
