# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Bill
from .models import Item

# Register your models here.
admin.site.register(Bill)
admin.site.register(Item)


