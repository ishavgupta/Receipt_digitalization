# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User


# Create your models here.




class Bill(models.Model):
    #user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    username = models.CharField(max_length=250, default = 0)
    Shop_name = models.CharField(max_length=250, default=0)
    Date = models.DateTimeField(auto_now_add=True)
    Shop_address = models.CharField(max_length=250, default=0)
    Telephone_no = models.CharField(max_length=250, default=0)
    Total_items = models.IntegerField(default=0)
    Bill_amount = models.IntegerField(default=0)
    Bill_picture = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.Shop_name


#    Bill_no = models.IntegerField(max_length=1000)

class Item(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    Item_name = models.CharField(max_length=50)
    Item_price = models.IntegerField()
    Item_warrenty_years = models.IntegerField()
  #  Item_warrenty_date = models.DateTimeField() # need not include in Bills table

    def __str__(self):
        return self.Item_name

