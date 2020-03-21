# urls.py

from django.conf.urls import url

# bring in the views from GoogleCal_App
from GoogleCal_App import views

urlpatterns = [
    url(r'^$', views.app_index, name='app_index'),
    url(r'^welcome/', views.bot, name='welcome'),
    url(r'^config/', views.dash, name='dash')
]
