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
import time
from django.db.models import Q

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
def delete_bill(request, pk):
    bill = Bill.objects.get(id=pk)
    if request.method == 'POST':  # If method is POST,
        bill.delete()  # delete the cat.
        return redirect('/')  # Finally, redirect to the homepage.

    return render(request, 'add-bill.html', {'bill': bill})




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

            instance.save()
            LabelFile = ""
            IMG_PATH = instance.Bill_picture.path
            url = 'https://app.nanonets.com/api/v2/OCR/Model/' + model_id + '/LabelFile/?async=true'

            data = {'file': open(IMG_PATH, 'rb')}

            response = requests.post(url, auth=requests.auth.HTTPBasicAuth(API_KEY, ''), files=data)
            js = json.loads(response.text)
            image_id = 0
            for i in js['result']:
                image_id = (i['id'])
            url = f'https://app.nanonets.com/api/v2/Inferences/Model/{model_id}/ImageLevelInferences/{image_id}'
            response = requests.request('GET', url, auth=requests.auth.HTTPBasicAuth(API_KEY, ''))
            js = json.loads(response.text)

            while(js['message']=="Image is being processed. Please try again later"):
                time.sleep(1)
                response = requests.request('GET', url, auth=requests.auth.HTTPBasicAuth(API_KEY, ''))
                js = json.loads(response.text)



            print(js)

            if(instance.Shop_name== None or instance.Shop_name== 0):
                print("Lol")
                for i in js['result'][0]['prediction']:
                    if i['label'] == "seller_name":
                        instance.Shop_name = i['ocr_text']
            if(instance.Shop_address== None):
                for i in js['result'][0]['prediction']:
                    if i['label'] == "seller_address":
                        instance.Shop_address = i['ocr_text']

            if(instance.Telephone_no== None):
                for i in js['result'][0]['prediction']:
                    if i['label'] == "seller_phone":
                        instance.Telephone_no = i['ocr_text']

            if (instance.Bill_amount == None):
                for i in js['result'][0]['prediction']:
                    if i['label'] == "invoice_amount":
                        instance.Bill_amount = float(i['ocr_text'])

            instance.save()
            img_obj = form.instance

            return render(request, 'home/add-bill.html', {'form': form, 'img_obj': img_obj,'segment': 'bill_image_view' })

    else:
        form = BillForm()
        print("jj")
        form.username = request.user.username
    return render(request, 'home/add-bill.html', {'form': form, 'segment': 'bill_image_view'})
    #return HttpResponse(html_template.render({'form': form}, request))




@login_required(login_url="/login/")
def result(request):
    query = request.GET.get('search_query')
    all_Bills = Bill.objects.filter(Q(Shop_name__icontains=query) | Q(Shop_address__icontains=query) | Q(Telephone_no__icontains=query) | Q(Bill_amount__icontains=query)   )

    all_Items = Item.objects.all()
    context = {
        'all_Bills': all_Bills,
        'all_Items': all_Items,
    }

    try:

        load_template = 'ui-tables.html'

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
