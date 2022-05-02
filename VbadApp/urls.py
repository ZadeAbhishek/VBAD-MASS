from typing import ValuesView
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from VbadApp import views

urlpatterns = [
    path("",views.home, name='VbadApp'),
    # path("about",views.about, name='about'),
    path("test/<str:msg>/<int:id>",views.index, name='index'),
    path("result",views.result, name='result'),
    path("questionpanel",views.questionpanel, name='questionpanel'),
    path("testno/<str:msg>",views.testno, name='testno'),
    path("createtest",views.createTest, name='createTest'),
    path("studentResult/<int:id>",views.studentResult,name='studentResult'),
]
