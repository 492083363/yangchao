#!/bin/env python
#coding=utf-8
#使用代理
def use_proxy(proxy,url):
    import urllib.request
    proxy=urllib.request.ProxyHandler({'http':proxy_addr})
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data=urllib.request.urlopen(url).read().decode('utf-8')
    return data
proxy_addr="116.209.54.125:9999"     #https://www.xicidaili.com/去查询免费代理ip
data=use_proxy(proxy_addr,"http://www.baidu.com")
print(len(data))
'''
说明：
首先建立一个名为use_proxy的自定义函数，该函数主要实现使用代理服务器来爬去某个URL网页的功能
在函数中，设置两个形式参数，第一个参数代表服务器的地址，第二个形式参数代表要爬去的网页的地址

'''
