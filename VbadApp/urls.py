from typing import ValuesView
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from VbadApp import views

urlpatterns = [
    path("",views.home, name='VbadApp'),
    # path("about",views.about, name='about'),
    path("test",views.index, name='index'),
    path("result",views.result, name='result'),
    path("teacherpanel",views.teacherpanel, name='teacherpanel'),
    path("testno",views.testno, name='testno'),
    path("createtest",views.createTest, name='createTest'),
]
