
from django.urls import path, re_path
from apps.home import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    path('bill_image_view', views.bill_image_view, name='bill_image_view'),
    # Matches any html file
    re_path(r'^.*\.html', views.pages, name='pages'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


