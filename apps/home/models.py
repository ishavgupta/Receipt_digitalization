# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.




class Bill(models.Model):
    username = models.CharField(max_length=250, null=True, blank=True)
    Shop_name = models.CharField(max_length=250, null=True, blank=True)
    Date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    Shop_address = models.CharField(max_length=250,  null=True, blank=True)
    Telephone_no = models.CharField(max_length=250,null=True, blank=True)
    Total_items = models.IntegerField( null=True, blank=True)
    Bill_amount = models.FloatField( null=True, blank=True)
    Bill_picture = models.ImageField(upload_to='')
    def __str__(self):
        return self.username


#    Bill_no = models.IntegerField(max_length=1000)

class Item(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    Item_name = models.CharField(max_length=50)
    Item_price = models.IntegerField()
    Item_warrenty_years = models.IntegerField()
  #  Item_warrenty_date = models.DateTimeField() # need not include in Bills table

    def __str__(self):
        return self.Item_name

