# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.

class TodoList(models.Model):
    STATUS_CHOICES = {
        ("pending", "Pending"),
        ("completed", "Completed")
    }
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    due_date = models.DateTimeField() #Set parameters
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    deleted_on = models.DateTimeField(default=None)
    sub_task_of = models.ForeignKey("TodoList", on_delete=models.CASCADE, null=True, default=None)

    class Meta:
        ordering = ["due_date"]

    def __str__(self):
        return self.title
