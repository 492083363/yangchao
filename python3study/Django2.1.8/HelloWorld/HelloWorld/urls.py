#!/bin/python
#coding=utf-8
from django.urls import *
from django.urls import path
from . import view,django_db,search,search2
from django.contrib import admin 
urlpatterns=[
    path('hello/',view.hello),
    path('django_db/',django_db.django_db),
    path('search_form/',search.search_form),
    path('search/',search.search),
    path('search-post/',search2.search_post),
    path('admin/',admin.site.urls),
]
