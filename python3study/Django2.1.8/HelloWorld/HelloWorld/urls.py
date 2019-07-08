#!/bin/python
#coding=utf-8
from django.urls import path
from . import view
urlpatterns=[
    path('hello/',view.hello),
]
