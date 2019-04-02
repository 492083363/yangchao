#!/usr/bin/env
#coding=utf-8

import urllib.request

for i in range(1,100):
    try:
        file=urllib.request.urlopen("http://yum.iqianyue.com",timeout=1)  #定义超时时间为1秒
        data=file.read()
        print (len(data))
    except Exception as e:
        print ('出现异常-->'+str(e))
