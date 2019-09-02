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
from django.urls import path, re_path ,include


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('user/',include('user.urls'))


    #include函数参数写 （应用.路由模块），该函数就会动态导入指定的包的模块，从哦块中读取urlpatterns，返回三元祖
   #url函数的第二参乎如果不是可调用对象，如果是元组或者列比哦奥，则会从路径出去已匹配的部分，将生于部分与引用的路由模块的urlpatterns进行匹配


]
