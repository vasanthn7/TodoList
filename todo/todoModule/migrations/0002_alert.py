# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-11 00:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todoModule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Time', models.DateTimeField(default=None)),
                ('message_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todoModule.TodoList')),
            ],
        ),
    ]
