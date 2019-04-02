# coding=utf-8
import urllib.request
import http.cookiejar
url = "http://news.163.com/16/0825/09/BVA8A9U500014SEH.html"
cjar = http.cookiejar.CookieJar()
proxy = urllib.request.ProxyHandler({'http': "192.168.3.60:8888"})
opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler, urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(opener)
data = urllib.request.urlopen(url).read()
fhandle = open("/home/yangchao/桌面/桌面/pacong/part9/1.html", "wb")
fhandle.write(data)
fhandle.close()
