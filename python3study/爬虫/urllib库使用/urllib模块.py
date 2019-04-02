#!/usr/bin/env
#coding=utf-8

import urllib.request

file=urllib.request.urlopen("http://www.baidu.com")
data=file.read()
dataline=file.readline()
print (data,dataline)
findle=open("/home/yangchao/桌面/桌面/pacong/2.html","wb")
findle.write(data)
findle.close()
filename=urllib.request.urlretrieve("http://edu.51cto.com",filename="/home/yangchao/桌面/桌面/pacong/2.html")
