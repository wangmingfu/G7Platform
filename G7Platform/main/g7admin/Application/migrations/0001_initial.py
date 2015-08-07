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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('apptype', models.IntegerField(verbose_name='类型', choices=[(0, '应用程序'), (1, '客户端框架'), (2, '服务端框架'), (3, '插件'), (4, '开源项目'), (5, '开发工具')], default=0)),
                ('appstatus', models.IntegerField(verbose_name='状态', choices=[(0, '新建'), (1, '策划中'), (2, '设计中'), (3, '开发中'), (4, '测试中'), (5, '提审中'), (6, '审核中'), (7, '回归中'), (8, '发布')], default=0)),
                ('platform', models.IntegerField(verbose_name='目标平台', blank=True, choices=[(0, '通用'), (1, 'iOS'), (2, 'Android'), (999, '其他')], default=0)),
                ('product_id', models.IntegerField(verbose_name='产品id', default=0)),
                ('product_type', models.IntegerField(verbose_name='产品类型', blank=True, null=True, choices=[(0, '未知(ids默认为0)'), (1, 'iPhone/iTouch版本'), (2, 'HD版本，仅适用iPad/iPad2'), (3, '通用版本，适用iOS系列')], default=0)),
                ('channel', models.IntegerField(verbose_name='频道', default=0)),
                ('inner_version', models.IntegerField(verbose_name='内部版本', default=0)),
                ('name', models.CharField(verbose_name='名字', max_length=150)),
                ('appid', models.CharField(verbose_name='标识码', blank=True, max_length=100, unique=True, default='')),
                ('file', models.FileField(verbose_name='文件', blank=True, null=True, upload_to='application/package')),
                ('version', models.CharField(verbose_name='版本', blank=True, max_length=150, default='0.0')),
                ('icon', models.ImageField(verbose_name='图标', blank=True, upload_to='application/icon/', default='/media/application/icon/default_icon.png')),
                ('create_at', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('modified_at', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('identifier', models.CharField(verbose_name='标识符(BundleID)', blank=True, max_length=200, null=True, default='')),
                ('description', models.TextField(verbose_name='说明', blank=True, null=True, default='')),
                ('frameworks', models.ManyToManyField(verbose_name='使用到的框架', blank=True, to='Application.G7Application', related_name='applications')),
            ],
            options={
                'verbose_name': '应用',
                'verbose_name_plural': '应用',
            },
        ),
        migrations.CreateModel(
            name='G7Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='名称', max_length=150, unique=True, default='')),
                ('descriptin', models.TextField(verbose_name='产品简介', blank=True, null=True, default='')),
                ('icon', models.ImageField(verbose_name='图标', upload_to='project/icon/', default='/media/project/icon/default_icon.png')),
                ('identifier', models.CharField(verbose_name='标识码', blank=True, max_length=100, unique=True, default='')),
                ('create_at', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('modified_at', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('applications', models.ManyToManyField(verbose_name='应用', blank=True, to='Application.G7Application', related_name='projects')),
                ('members', models.ManyToManyField(verbose_name='成员', blank=True, to=settings.AUTH_USER_MODEL, db_constraint=False, related_name='projects')),
                ('owner', models.ForeignKey(verbose_name='拥有人', db_constraint=False, to=settings.AUTH_USER_MODEL, related_name='+')),
            ],
            options={
                'verbose_name': '产品',
                'verbose_name_plural': '产品',
            },
        ),
    ]
