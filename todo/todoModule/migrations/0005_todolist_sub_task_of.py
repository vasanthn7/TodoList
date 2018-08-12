# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-12 08:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todoModule', '0004_remove_todolist_sub_task_of'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='sub_task_of',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='todoModule.TodoList'),
        ),
    ]
