# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-12 08:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoModule', '0003_auto_20180812_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='sub_task_of',
        ),
    ]