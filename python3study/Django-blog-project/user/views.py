from django.shortcuts import render
# 不用模板
# Create your views here.
import logging
FORMAT ="%(asctime)s % (threadName)s % (thread)d % (message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)

from django.http import JsonResponse, HttpRequest, HttpResponse,HttpResponseBadRequest
import json
import simplejson

def  checkemail(reuqest):
    #判断email
    return HttpResponse()
 

def reg(request: HttpRequest):
    print(request, '~~~~~~~')
    #print(type(request))
    #print(request.GET)
    #print(request.POST)
    #print(request.body,'~~~~~')
    #print(json.loads(request.body.decode()),'~~~~')
    try:
        payload=simplejson.loads(request.body)
        #payload=json.loads(reques.body.decode())
        email=payload['email']
        #获取POST提交的JSON信息，email与数据库信息对比

        name= payload['name']
        password=payload['password']
        print(email,name,password)

        return HttpResponse("welcome to yangchao's blog")

    except Exception as e:
        logging.info(e)
        return HttpResponseBadRequest()
    

    
