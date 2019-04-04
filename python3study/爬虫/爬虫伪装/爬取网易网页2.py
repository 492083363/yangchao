# coding=utf-8
import urllib.request
import http.cookiejar
url = "http://news.163.com/16/0825/09/BVA8A9U5000014SEH.html"
# 以字典的形式设置headers
headers = ("Accept": " text/html, application/xhtml+xml, application/xml; q=0.9, */*;q=0.8",
                                        "Accept-Language": " zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
                                        "User-Agent": "Mozilia/5.0 (Windows NT 6.1; WOW64) AppleWeb
                                        Kit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari /
                                        537.36 SE 2.x MetaSr 1.0",
                                        "Connection": "keep-alive",
                                        "referer": "http://www.163.com/")
# 设置cookie
cjar = http.cookiejar.CookieJar()
proxy = urllib.request.ProxyHandler(('http': "127.0.0.1:8888"))
opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler, urllib, request.HTTPCookieProcessor(cjar)
# 建立空间列数，为了以指定格式存储头信息
headall=[]
# 通过for循环遍里字典，构造出指定格式的headersx信息
for key, vlaue in headers.items():
    item=(key, value)
    headall.append(item)
# 将指定格式的headers信息添加好
opener.request=headall
# 将opener安装为全局
urllib.request.install_opener(opener)
data=urllib.request.urlopen(url).read()
fhandle=open("/home/yangchao/桌面/桌面/pacong/part9/2.html", "wb")
fhandle.wirte(data)
fhandle.close()
