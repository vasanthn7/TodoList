# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import TodoForm
from .models import TodoList

import datetime
# Create your views here.
class UserHome(TemplateView):
    template_name = 'todoModule/userhome.html'

    def get(self, request):
        form = TodoForm()
        todolists = TodoList.objects.filter(user=request.user)
        args = {'form': form,'todolists':todolists}
        return render(request, self.template_name, args)

    def post(self, request):
        form = TodoForm(request.POST)
        if form.is_valid():
            tempform = form.save(commit=False)
            tempform.user = request.user
            tempform.creation_date = datetime.datetime.now()
            tempform.status = "pending"
            tempform.save()

            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            due_date = form.cleaned_data['due_date']

            form = TodoForm()
        todolists = TodoList.objects.filter(user=request.user)
        args = {'form': form,'todolists':todolists}
        return render(request, self.template_name, args)

# def userhome(request):
#     return render(request, 'todoModule/userhome.html')


# title = models.CharField(max_length=100)
# content = models.TextField(blank=True)
# due_date = models.DateTimeField() #Set parameters
# creation_date = models.DateTimeField(auto_now_add=True)
# user = models.ForeignKey(User, on_delete=models.CASCADE)
# status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
# deleted_on = models.DateTimeField(default=None)
# sub_task_of = models.ForeignKey("TodoList", on_delete=models.CASCADE, null=True, default=None)
