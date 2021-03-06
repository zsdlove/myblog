# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-02 16:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('zsdlove', '0003_friend_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='public_notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice_id', models.CharField(max_length=5, verbose_name='公告序号')),
                ('notice_content', models.CharField(max_length=200, verbose_name='公告内容')),
                ('notice_time', models.DateTimeField(default=datetime.datetime(2018, 9, 2, 16, 8, 26, 350548, tzinfo=utc), verbose_name='创建时间')),
            ],
        ),
    ]
