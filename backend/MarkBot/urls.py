"""MarkBot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Import from django configeration urls ... url and include
from django.conf.urls import (url, include)

# Import app views
from GoogleCal_App import views
from ReactApp import views

urlpatterns = [
    # matching any pattern give the index view
    url(r'^$', views.web_index, name="web_index"),

    # for endpoint ending with r'^google/' include the...
    # "mini urls from GoogleCal_App urls.py file"
    url(r'^bot/', include('GoogleCal_App.urls')),
    url(r'^home/', include('ReactApp.urls')),
    path('admin/', admin.site.urls),

]
