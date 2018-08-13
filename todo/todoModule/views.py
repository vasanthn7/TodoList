# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
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
        print form
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

class Deleted(TemplateView):
    template_name = 'todoModule/deleted.html'

    def get(self, request):
        todolists = TodoList.objects.filter(user=request.user)
        args = {'todolists':todolists}
        return render(request, self.template_name, args)

    # def post(self, request):
    #     form = TodoForm(request.POST)
    #     if form.is_valid():
    #         tempform = form.save(commit=False)
    #         tempform.user = request.user
    #         tempform.creation_date = datetime.datetime.now()
    #         tempform.status = "pending"
    #         tempform.save()
    #
    #         title = form.cleaned_data['title']
    #         content = form.cleaned_data['content']
    #         due_date = form.cleaned_data['due_date']
    #         form = TodoForm()
    #
    #     todolists = TodoList.objects.filter(user=request.user)
    #     args = {'form': form,'todolists':todolists}
    #     return render(request, self.template_name, args)


def statusdone(request, pk):
    todo = TodoList.objects.get(id = pk)
    todo.status = "completed"
    todo.save()

    return redirect('/login/profile')

def softdelete(request, pk):
    todo = TodoList.objects.get(id = pk)
    todo.deleted_on = datetime.datetime.now()
    todo.save()

    return redirect('/login/profile')

def restore(request, pk):
    todo = TodoList.objects.get(id = pk)
    todo.deleted_on = None
    todo.save()

    return redirect('/login/profile/deleted')

def permdelete(request, pk):
    todo = TodoList.objects.get(id = pk)
    todo.delete()

    return redirect('/login/profile/deleted')
