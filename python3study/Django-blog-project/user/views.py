#注册代码v1
from django.http import JsonResponse, HttpRequest, HttpResponse, HttpResponseBadRequest
from .models import USER
from django.db.models.query import QuerySet
import simplejson
import json
from django.shortcuts import render

# 不用模板
# Create your views here.
import logging
FORMAT = "%%(asctime)s %% (threadName)s %% (thread)d %% (message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)

def checkemail(reuqest):
    # 判断email
    return HttpResponse()


def reg(request: HttpRequest):
    print(request, '~~~~~~~')
    # print(type(request))
    # print(request.GET)
    # print(request.POST)
    # print(request.body,'~~~~~')
    # print(json.loads(request.body.decode()),'~~~~')
    try:
        try:
            qs=USER.objects.filter().all()
            #qs = USER.objects.filter(pk=2).get() 
            #print (qs.query)
            #user=USER.objects.filter(email=email).get() 期待查询集只有一行，否则抛出异常
            #user=USER.objects.get(email=email) 返回不是茶续集，而是一个USER实例，否则抛出异常
            #user=USER.objects.get(id=1) 更多的查询使用主建，也可以使用pk=1
            #user=USER.objects.first() 使用limit 1查询，茶道返回一个实例，查不到返回None
            #user=USER.objecys.filter(pk=3,emial=email).first() and条件
            qs.filter().first()
            print(qs)
        except Exception as e:
            print(e)
        finally:
            print('~'*30)

        payload = simplejson.loads(request.body)
        # payload=json.loads(reques.body.decode())
        email = payload['email']
        # 获取POST提交的JSON信息，email与数据库信息对比
        qs = USER.objects.filter(email=email)  # 数据库管理器
        print(qs)  # 列表
        #print(qs.query, '~~~~~~~~~~~~~~~~~~~~~~~~~~~')  # 查询集
        if qs:  # 该email已经存在了
            return HttpResponseBadRequest()
        # else:
        #   print('-'*30)

        name = payload['name']
        password = payload['password']
        print(email, name, password)

        user = USER()
        user.email = email
        user.name = name
        user.password = password

        try:
            #user.save()
            return JsonResponse({'user':user.id}) #如果正常，返回json数据
        except Exception as e :
            raise 

        return HttpResponse("welcome to yangchao's blog")

    except Exception as e:      #任何异常抛出异常
        logging.info(e)
        return HttpResponseBadRequest()
