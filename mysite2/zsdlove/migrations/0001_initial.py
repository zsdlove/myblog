# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-01 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employeeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emploee_id', models.CharField(max_length=32)),
                ('emploee_name', models.CharField(max_length=32)),
            ],
        ),
    ]
