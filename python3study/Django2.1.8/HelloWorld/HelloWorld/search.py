#!/bin/python
# coding=utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response

# form


def search_form(request):
    return render_to_response('search_form.html')

# recivie the request


def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        message = 'your searching is ' + request.GET['q']
    else:
        message = 'you commit a null form'
    return HttpResponse(message)
