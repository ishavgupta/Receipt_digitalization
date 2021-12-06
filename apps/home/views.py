# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Bill
from .models import Item
import requests
import json
from django.shortcuts import render, redirect
from .forms import *
#from apps.authentication import forms
from django.contrib.auth.models import User


#Nanonets
API_KEY = "geEnRk2-LXvy6-WhzgQjNzQu0YO-6iE7"
model_id = "ca58d7f9-770c-44a8-83fa-f45f8815e668"
url0 = 'https://app.nanonets.com/api/v2/OCR/Model/' + model_id






@login_required(login_url="/login/")
def index(request):
    all_Bills = Bill.objects.all()

    context = {'segment': 'index',
               'all_Bills': all_Bills,
               }

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def bill_image_view(request):

    all_Bills = Bill.objects.filter(username=request.user.username)

    context1 = {'segment': 'index',
               'all_Bills': all_Bills,
               }


    if request.method == 'POST':
        form = BillForm(request.POST, request.FILES)

        if form.is_valid():
            instance=form.save(commit= False)
            instance.username=request.user.username

            instance.save


            instance.save()
            img_obj = form.instance

            return render(request, 'home/page-blank.html', {'form': form, 'img_obj': img_obj,'segment': 'bill_image_view' })

    else:
        form = BillForm()
        print("jj")
        form.username = request.user.username
    return render(request, 'home/page-blank.html', {'form': form, 'segment': 'bill_image_view'})
    #return HttpResponse(html_template.render({'form': form}, request))





@login_required(login_url="/login/")
def success(request):
    return HttpResponse('successfully uploaded')




@login_required(login_url="/login/")
def pages(request):
    all_Bills = Bill.objects.all()
    all_Items = Item.objects.all()
    context = {
        'all_Bills': all_Bills,
        'all_Items': all_Items,
    }

    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
