# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0016_auto_20150807_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7user',
            name='userid',
            field=models.CharField(max_length=100, blank=True, default='be2c37a8c9b64094ac43b24710f6df4c', verbose_name='用户ID'),
        ),
        migrations.AlterField(
            model_name='g7user',
            name='usignature',
            field=models.CharField(max_length=100, blank=True, default='6c263327d6f34305af5056c54ce47cae', verbose_name='用户登陆标识'),
        ),
    ]
