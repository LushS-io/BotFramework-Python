# urls.py

from django.conf.urls import url

# bring in the views from GoogleCal_App
from GoogleCal_App import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^control/', views.control, name='control')
]
