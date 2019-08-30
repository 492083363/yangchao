"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path


from django.http import HttpResponse, HttpRequest, JsonResponse

from django.template import loader ,RequestContext

#模板
from django.shortcuts import render 


def index(request):
    #视图函数：请求进步返回响应
    print(request)
    print(type(request))

    #tp1 = loader.get_template('index.html')
    #context = RequestContext (request,{'content':'www.yangchao.com'})
    # return HttpResponset(tp1.render(context))
    d=dict(zip('abcde',range(1,6)))
    print (d)
    #return render(request,'index.html',{'user':'yangchao'}) #html  str
    #return HttpResponse('hello yangchao')
    return render(request,'index.html',{'d':d})   #html str
    


def index_jason(request:HttpRequest):
    #视图函数：请求进步返回响应,使用jason格式
    #d={'user':'hello yangchao'}
    #d['method']=request.method
    #d['path']=request.path
    #d['path_info']=request.path_info
    #d['GETparams']=request.GET
    #return JsonResponse(d) 
    return JsonResponse({'user':'yangchao'})#jsaon str
    


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', index),
    path('index_jason',index_jason)
    #re_path(r'^index/$', index),           正则匹配
    #re_path(r'^$', index),

]
