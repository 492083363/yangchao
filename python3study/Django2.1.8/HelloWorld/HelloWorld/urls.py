#!/bin/python
#coding=utf-8
from django.urls import *
from . import view,django_db
urlpatterns=[
    path('hello/',view.hello),
    path('django_db/',django_db.django_db),
]
