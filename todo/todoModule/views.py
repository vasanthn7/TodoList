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

def statusdone(request):
    if request.method == 'POST':
        form = TodoDone(request.POST)
        if form.is_valid():
            # form.save()
            return redirect('/')
        else:
            return HttpResponse("Invalid inputs,retry")

# from __future__ import unicode_literals
#
# from django.shortcuts import render, redirect, HttpResponse
# from UsrMgmtModule.forms import RegistrationForm
#
# # Create your views here.
# def home(request):
#     return render(request, 'UsrMgmtModule/home.html')
#
# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#         else:
#             return HttpResponse("Invalid inputs,retry")
#
#     else:
#         form = RegistrationForm()
#
#         args = {'form': form}
#         return render(request, 'UsrMgmtModule/registration.html', args)

#
# class RegistrationForm(UserCreationForm):
#
#     email = forms.EmailField(required=True)
#
#     class Meta:
#         model = User
#         fields = ('username','first_name','last_name','email','password1','password2')
#         # help_text = {
#         #     'username': None,
#         #     'first_name': None,
#         #     'last_name': None,
#         #     'email': None,
#         #     'password1': None,
#         #     'password2': None,
#         # }
#
#     def save(self, commit=True):
#         user = super(RegistrationForm, self).save(commit=False)
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         user.email = self.cleaned_data['email']
#
#         if commit:
#             user.save()
#
#         return user
