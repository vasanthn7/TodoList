# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
# Create your models here.

class TodoList(models.Model):
    STATUS_CHOICES = {
        ("pending", "Pending"),
        ("completed", "Completed")
    }
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    due_date = models.DateField(blank=False, default=None)
    due_time = models.TimeField(blank=False, default=None) #Set parameters
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    deleted_on = models.DateTimeField(default=None, null=True)
    sub_task_of = models.ForeignKey("TodoList", on_delete=models.CASCADE, null=True, default=None)

    class Meta:
        ordering = ["due_date" ,"due_time"]

    def __str__(self):
        return self.title

class Alert(models.Model):
    Time = models.DateTimeField(default=None)
    message_id = models.ForeignKey("TodoList", on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.Time
