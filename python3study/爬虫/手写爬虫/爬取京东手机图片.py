#!/bin/env python
#coding=utf-8
'''
爬取过程：
首先通过urllib.request.urlopen(url).read()读取对应网页的全部源代码，然后根据正则表达式进行一次信息过滤，过滤完成后，
再第一次过滤的结果的基础上，根据正则表达式进行第二次过滤，提取该网页上所有目标图片的连接，并将这些链接地址存储到一个列表中，
然后遍历该列表，分别将对应链接通过urllib.request.urlretrieve（imageurl,filename=imagename)存储到本地。为了避免
程序中途异常崩溃，可以建立异常处理，若不能爬取某个图片，则会通过x+=1自动跳到下一个图片
通过for循环将该分类下的所有的网页都爬取一边，链接可以构造为htl="hhtp://list.jd.com/list?cat=997,653,655&page="+str(i)

'''
import re    #引入正则表达式模块
import urllib.request
def craw(url,page):
    html1=urllib.request.urlopen(url).read()    #爬取相应网页,读取对应网页的源代码
    html1=str(html1)                            #转化为字符串
    pat1='<div id="plist".+? <div class="page clearfix">'
    result1=re.compile(pat1).findall(html1)
    resu1t1=result1[0]
    result2=str(result1)
    #print (str(html1))
    #result1=str(html1)
    pat2='<img width="220" height="220" data-img="1" data-lazy-img="//(.+?\.jpg)">' # 正则表达式匹配图片
    imagelist=re.compile(pat2).findall(result2)
    x=1
    for imageurl in imagelist:
        imagename="E:/pacong/part6/img1/"+str(page)+str(x)+".jpg"
        imageurl="http://"+imageurl
        try:
            urllib.request.urlretrieve(imageurl,filename=imagename)
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                x+=1
            if hasattr(e,"reason"):
                x+=1
            x+=1
for i in range(1,79):
    url="https://list.jd.com/list.html?cat=9987,653,655&page="+str(i)
    craw(url,i)


