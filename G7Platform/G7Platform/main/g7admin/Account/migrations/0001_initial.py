# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='G7Group',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=80, verbose_name='name', unique=True)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('date_of_birth', models.DateField(verbose_name='账户生成日期', auto_now=True)),
                ('is_active', models.BooleanField(verbose_name='账户是否激活', default=True)),
                ('is_admin', models.BooleanField(verbose_name='是否是管理员', default=False)),
                ('userid', models.CharField(blank=True, verbose_name='用户ID', default='29f9228000aa4f09bac17f7ff44be82e', max_length=100)),
                ('email', models.EmailField(max_length=255, verbose_name='邮箱', unique=True)),
                ('username', models.CharField(max_length=255, verbose_name='用户名', default='', unique=True)),
                ('sex', models.CharField(blank=True, verbose_name='性别', choices=[('man', '男'), ('female', '女'), ('unknown', '未知')], default='man', max_length=15)),
                ('thumb', models.ImageField(upload_to='user/thumbnails', verbose_name='头像', default='/media/user/thumbnails/default_thumb.png')),
                ('age', models.IntegerField(verbose_name='年龄', default=0)),
                ('expires_time', models.DateTimeField(verbose_name='登陆过期时间', null=True, auto_now_add=True)),
                ('usignature', models.CharField(blank=True, verbose_name='用户登陆标识', default='ba361c61dbae4c41ae00626f85f36008', max_length=100)),
                ('nickname', models.CharField(blank=True, verbose_name='昵称', default='', max_length=255)),
                ('clientid', models.CharField(blank=True, verbose_name='客户端id', default='', max_length=100)),
                ('realname', models.CharField(max_length=255, verbose_name='真实姓名', default='')),
                ('job', models.CharField(max_length=100, verbose_name='职业', default='')),
                ('mobile', models.CharField(blank=True, verbose_name='电话号码', null=True, default='', max_length=50)),
                ('description', models.TextField(blank=True, verbose_name='简介', null=True, default='')),
                ('groups', models.ManyToManyField(blank=True, verbose_name='群组', related_name='members', to='Account.G7Group')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
        ),
        migrations.AddField(
            model_name='g7group',
            name='creator',
            field=models.ForeignKey(verbose_name='群组创建者', related_query_name='g7group1', db_constraint=False, to=settings.AUTH_USER_MODEL, related_name='g7group1_set'),
        ),
        migrations.AddField(
            model_name='g7group',
            name='permissions',
            field=models.ManyToManyField(blank=True, verbose_name='permissions', to='auth.Permission'),
        ),
    ]
