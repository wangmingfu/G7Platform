# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='G7Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='name', max_length=80, unique=True)),
                ('date_of_birth', models.DateField(verbose_name='群组建立日期', auto_now=True)),
            ],
            options={
                'verbose_name': '群组',
                'verbose_name_plural': '群组',
            },
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='G7User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('date_of_birth', models.DateField(verbose_name='账户生成日期', auto_now=True)),
                ('is_active', models.BooleanField(verbose_name='账户是否激活', default=True)),
                ('is_admin', models.BooleanField(verbose_name='是否是管理员', default=False)),
                ('userid', models.CharField(verbose_name='用户ID', blank=True, max_length=100, default='ba7f623e32144afda6993e9565a367c9')),
                ('email', models.EmailField(verbose_name='邮箱', max_length=255, unique=True)),
                ('username', models.CharField(verbose_name='用户名', max_length=255, unique=True, default='')),
                ('sex', models.CharField(verbose_name='性别', blank=True, max_length=15, choices=[('man', '男'), ('female', '女'), ('unknown', '未知')], default='man')),
                ('thumb', models.ImageField(verbose_name='头像', upload_to='user/thumbnails', default='/media/user/thumbnails/default_thumb.png')),
                ('age', models.IntegerField(verbose_name='年龄', default=0)),
                ('expires_time', models.DateTimeField(verbose_name='登陆过期时间', null=True, auto_now_add=True)),
                ('usignature', models.CharField(verbose_name='用户登陆标识', blank=True, max_length=100, default='3e25d5eb78b34af0892176d88f300747')),
                ('nickname', models.CharField(verbose_name='昵称', blank=True, max_length=255, default='')),
                ('clientid', models.CharField(verbose_name='客户端id', blank=True, max_length=100, default='')),
                ('realname', models.CharField(verbose_name='真实姓名', max_length=255, default='')),
                ('job', models.CharField(verbose_name='职业', max_length=100, default='')),
                ('mobile', models.CharField(verbose_name='电话号码', blank=True, max_length=50, null=True, default='')),
                ('description', models.TextField(verbose_name='简介', blank=True, null=True, default='')),
                ('groups', models.ManyToManyField(verbose_name='群组', blank=True, to='Account.G7Group', related_name='members')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
        ),
        migrations.AddField(
            model_name='g7group',
            name='creator',
            field=models.ForeignKey(verbose_name='群组创建者', db_constraint=False, related_query_name='g7group1', to=settings.AUTH_USER_MODEL, related_name='g7group1_set'),
        ),
        migrations.AddField(
            model_name='g7group',
            name='permissions',
            field=models.ManyToManyField(verbose_name='permissions', blank=True, to='auth.Permission'),
        ),
    ]
