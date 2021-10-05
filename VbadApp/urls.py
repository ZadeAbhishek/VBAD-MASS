from typing import ValuesView
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from VbadApp import views

urlpatterns = [
    path("",views.home, name='VbadApp'),
    path("about",views.about, name='about'),
    path("test",views.index, name='index')
    
]
