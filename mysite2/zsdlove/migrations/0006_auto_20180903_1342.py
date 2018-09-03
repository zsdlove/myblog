# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-03 05:42
from __future__ import unicode_literals

import DjangoUeditor.models
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('zsdlove', '0005_auto_20180903_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=DjangoUeditor.models.UEditorField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='public_notice',
            name='notice_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 3, 5, 42, 52, 364026, tzinfo=utc), verbose_name='创建时间'),
        ),
    ]