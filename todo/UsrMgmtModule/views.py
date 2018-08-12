# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from UsrMgmtModule.forms import RegistrationForm

# Create your views here.
def home(request):
    return render(request, 'UsrMgmtModule/home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return HttpResponse("Invalid inputs,retry")

    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'UsrMgmtModule/registration.html', args)
