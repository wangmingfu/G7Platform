# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='g7application',
            name='appstatus',
        ),
        migrations.RemoveField(
            model_name='g7application',
            name='apptype',
        ),
        migrations.RemoveField(
            model_name='g7application',
            name='platform',
        ),
        migrations.AddField(
            model_name='g7project',
            name='latest_build_version',
            field=models.IntegerField(verbose_name='最新编译版本', default=0),
        ),
        migrations.AddField(
            model_name='g7project',
            name='latest_inner_version',
            field=models.IntegerField(verbose_name='最新内部版本', default=0),
        ),
        migrations.AddField(
            model_name='g7project',
            name='latest_version',
            field=models.CharField(max_length=200, verbose_name='最新版本', default='0.0'),
        ),
        migrations.AddField(
            model_name='g7project',
            name='platform',
            field=models.IntegerField(blank=True, verbose_name='目标平台', choices=[(0, '通用'), (1, 'iOS'), (2, 'Android'), (999, '其他')], default=0),
        ),
        migrations.AddField(
            model_name='g7project',
            name='product_status',
            field=models.IntegerField(verbose_name='状态', choices=[(0, '新建'), (1, '策划中'), (2, '设计中'), (3, '开发中'), (4, '测试中'), (5, '提审中'), (6, '审核中'), (7, '回归中'), (8, '发布')], default=0),
        ),
        migrations.AddField(
            model_name='g7project',
            name='product_type',
            field=models.IntegerField(verbose_name='类型', choices=[(0, '应用程序'), (1, '客户端框架'), (2, '服务端框架'), (3, '插件'), (4, '开源项目'), (5, '开发工具')], default=0),
        ),
    ]
