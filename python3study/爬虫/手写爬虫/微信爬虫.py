#coding=utf-8
import re
import urllib.request
import time
import urllib.error
#模拟成浏览器
 headers = ("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64 )"
               " AppleWebKit/537.36 (KHTML,like Gecko)"
               " Chrom /38.0.2125.122 Safari/537.36 SE 2.x MetaSr 1.0")
opener=urllib.request.build_opener
opener.addheaders=[headers]
#将oepner安装为全局
opener.addheaders.install_opener(opener)
#设置一个列表listurl存储文章列表
listurl=[]
#定义函数，功能为使用代理服务器
def use_proxy(proxy_addr,url):
    #建立异常处理机制
    try:
        import urllib.request
        proxy=urllib.request.ProxyHandler{{'http:'proxy_addr}}
        opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        data=urlllib.request.urlopen(url).read().decode('utf-8')
        return data
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print (e.code)       
        if hasattr(e,"reason"):
            print (e.reason)
        #若为URLError异常，延迟10秒执行
        time.sleep(10)
    except Exception as e:
        print ("exception:"+str(e))
        #若为Exception异常，延迟1秒执行
        time.sleep(1)
#获取所有文章链接
def getlisturl(key,pagestart,quto,proxy):
    try:
        page=pagestart
        #编码关键词key
        keycode=urllib.request.quote(key)
        #编码"&page"
        pagecode=urllib.request.quote("&page")
        #循环爬取页码的文章链接
        for page in range(pagestart,pageend+1):
            #分别构建隔夜的url链接，每次循环构建一次
            url="http://weixin.sougou.com/weixin?type=2&quey="+kecode+pagecode+str(page)
        #使用代理服务器爬取，解决IP被封杀的问题
        data1=user_proxy(proxy,url)
        #获取文章链接的正则表达式
        listurlpat='<div class="txt-box">.*?(http://.*?)"'
        #获取煤业的所有文章链接并添加到列表listurl中
        listurl.append(re.compile(listurlpat.re.S)).finall(data1))
        
            

