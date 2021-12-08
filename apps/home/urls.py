
from django.urls import path, re_path
from apps.home import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.delete_bill, name='delete_bill'),

    path('bill_image_view', views.bill_image_view, name='bill_image_view'),
    path('result', views.result, name='result'),
    # Matches any html file
    re_path(r'^.*\.html', views.pages, name='pages'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


