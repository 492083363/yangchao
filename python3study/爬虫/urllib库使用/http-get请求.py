#!/usr/env python
#coding=utf-8
#实现用爬虫自动地再百度上查询关键字为hello的结构
'''
不支持中文编码
import urllib.request
keywd="羊草"
url="http://www.baidu.com/s?wd="+keywd
req=urllib.request.Request(url)             #构建对象
data=urllib.request.urlopen(req).read()     #打开对象
fhandle=open("E:/pacong/2.html","wb")
fhandle.write(data)
fhandle.close()

'''

import urllib.request
url="http://www.baidu.com/s?wd="
keywd="羊草"
key_code=urllib.request.quote(keywd)   #使用关键词部分进行编码，编码之后再构造完成的url
url_all=url+key_code
req=urllib.request.Request(url_all)
data=urllib.request.urlopen(req).read()
fh=open("/home/yangchao/桌面/桌面/pacong/6.html","wb")
fh.write(data)
fh.close()


