# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import TemplateView
from django.db.models import Q

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
            due_time = form.cleaned_data['due_time']
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

def datefilter(request, pk):
    todolists = TodoList.objects.filter(user=request.user)
    form = TodoForm()
    print "date filter value " + pk
    pk = int(pk)
    # print type(pk)
    # print "________________________________________________"
    # print todolists[0].due_date.date()
    # print type(todolists[0].due_date.date())
    # print "_____________"
    # print datetime.date.today()
    # print type(datetime.date.today())
    # print "________________________________________________"
    if pk == 1:
        args = {'form': form,'todolists':todolists}

    elif pk == 2:
        todolists = todolists.filter(due_date = datetime.date.today())

    elif pk == 3:
        startdate = datetime.date.today()
        enddate = datetime.date.today() + datetime.timedelta(days=7)
        todolists = todolists.filter(due_date__range=(startdate, enddate))

    elif pk == 4:
        startdate = datetime.date.today() + datetime.timedelta(days=7)
        enddate = datetime.date.today() + datetime.timedelta(days=14)
        todolists = todolists.filter(due_date__range=(startdate, enddate))

    elif pk == 5:
        todolists = todolists.filter(Q(due_date__lt = datetime.date.today()) | (Q(due_date = datetime.date.today()) & Q(due_time__lt = datetime.datetime.now().time())))

    args = {'form': form,'todolists':todolists}
    return render(request, 'todoModule/userhome.html', args)

def searchtitle(request):
    text = request.POST['search']
    todolists = TodoList.objects.filter(user=request.user)
    todolists = todolists.filter(title__icontains=text)
    form = TodoForm()
    args = {'form': form,'todolists':todolists}
    return render(request, 'todoModule/userhome.html', args)
