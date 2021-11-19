# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    path('bill_image_view', views.bill_image_view, name='bill_image_view'),
    path('success', views.success, name='success'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)