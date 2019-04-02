#!/bin/env python
#coding=utf-8
import urllib.request
import urllib.parse
#登陆chinaunix论坛
url="http://account.chinaunix.net/login/login"   #博客登陆首页对应POST方法的
postdata=urllib.parse.urlencode({
    "username":"xxxxxx",
    "password":"xxxxxxx"
}).encode('utf-8')                #使用urlencode编码处理后，再设置为utf-8编码
req=urllib.request.Request(url,postdata) #构建Request对象
req.add_header('User-Agent','Mozilla/5.0(Windows NT 6.1; WOW 64) AppleWebKit /537.36(KHTML,like Gecko) '
                            'Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
data=urllib.request.urlopen(req).read() #登陆并爬取相应的网页
fhandle=open("E:/pacong/part5/1.html","wb")
fhandle.write(data) #将内容写入对应文件
fhandle.close()

url2="http://bbs.chinaunix.net"  #设置要爬取的该网站下的其他网页地址
req2=urllib.request.Request(url2,postdata)
req2.add_header('User-Agent','Mozilla/5.0(Windows NT 6.1; WOW 64) AppleWebKit /537.36(KHTML,like Gecko) '
                            'Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
data2=urllib.request.urlopen(req2).read() #爬取该网站下的其他网页
fhandle=open("E:/pacong/part5/2.html","wb")
fhandle.write(data2) #将爬取的其他网页写入对应文件
fhandle.close()



