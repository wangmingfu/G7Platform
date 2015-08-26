# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='G7Application',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('product_id', models.IntegerField(default=0, verbose_name='产品id')),
                ('product_type', models.IntegerField(default=0, choices=[(0, '未知(ids默认为0)'), (1, 'iPhone/iTouch版本'), (2, 'HD版本，仅适用iPad/iPad2'), (3, '通用版本，适用iOS系列')], null=True, blank=True, verbose_name='产品类型')),
                ('channel', models.IntegerField(default=0, verbose_name='频道')),
                ('inner_version', models.IntegerField(default=0, verbose_name='内部版本')),
                ('name', models.CharField(max_length=150, verbose_name='名字')),
                ('appid', models.CharField(default='', verbose_name='标识码', blank=True, max_length=100, unique=True)),
                ('file', models.FileField(null=True, blank=True, upload_to='application/package', verbose_name='文件')),
                ('version', models.CharField(default='0.0', blank=True, max_length=150, verbose_name='版本')),
                ('icon', models.ImageField(default='application/icon/default_icon.png', blank=True, upload_to='application/icon/', verbose_name='图标')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('bundleID', models.CharField(default='', null=True, blank=True, max_length=200, verbose_name='标识符(BundleID)')),
                ('description', models.TextField(default='', null=True, blank=True, verbose_name='说明')),
                ('build_version', models.CharField(default='0', max_length=200, verbose_name='编译版本')),
                ('frameworks', models.ManyToManyField(related_name='applications', to='Application.G7Application', blank=True, verbose_name='使用到的框架')),
            ],
            options={
                'verbose_name_plural': '应用',
                'verbose_name': '应用',
            },
        ),
        migrations.CreateModel(
            name='G7Project',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('platform', models.IntegerField(default=0, choices=[(0, '通用'), (1, 'iOS'), (2, 'Android'), (999, '其他')], blank=True, verbose_name='目标平台')),
                ('project_type', models.IntegerField(default=0, choices=[(0, '应用程序'), (1, '客户端框架'), (2, '服务端框架'), (3, '插件'), (4, '开源项目'), (5, '开发工具')], verbose_name='类型')),
                ('project_status', models.IntegerField(default=0, choices=[(0, '新建'), (1, '策划中'), (2, '设计中'), (3, '开发中'), (4, '测试中'), (5, '提审中'), (6, '审核中'), (7, '回归中'), (8, '发布')], verbose_name='状态')),
                ('project_id', models.IntegerField(default=0, verbose_name='产品id')),
                ('latest_version', models.CharField(default='0.0', null=True, blank=True, max_length=200, verbose_name='最新版本')),
                ('latest_inner_version', models.IntegerField(default=0, null=True, blank=True, verbose_name='最新内部版本')),
                ('latest_build_version', models.CharField(default=0, null=True, blank=True, max_length=200, verbose_name='最新编译版本')),
                ('name', models.CharField(default='', max_length=150, verbose_name='名称')),
                ('descriptin', models.TextField(default='', null=True, blank=True, verbose_name='产品简介')),
                ('icon', models.ImageField(default='project/icon/default_icon.png', upload_to='project/icon/', verbose_name='图标')),
                ('identifier', models.CharField(default='', verbose_name='标识码', blank=True, max_length=100, unique=True)),
                ('bundleID', models.CharField(default='', verbose_name='标识符(BundleID)', max_length=200, unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('applications', models.ManyToManyField(related_name='projects', to='Application.G7Application', blank=True, verbose_name='应用')),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='projects', db_constraint=False, blank=True, verbose_name='成员')),
                ('owner', models.ForeignKey(blank=True, verbose_name='拥有人', db_constraint=False, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '产品',
                'verbose_name': '产品',
            },
        ),
    ]
