# ReactApp/urls.py

from django.conf.urls import url

# bring in the views from GoogleCal_App
from ReactApp import views

urlpatterns = [
    url(r'^$', views.web_index, name='web_index'),
    url(r'^contact/', views.contact_page, name='contact_page'),
]
