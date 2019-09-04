#!/usr/bin/env
# coding=utf-8
# 模拟http头部
import urllib.request
url = "http://blog.csdn.net/weiwei_pig/article/details/51178226"
headers = ("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64 ) "
           "AppleWebKit/537.36 (KHTML,like Gecko) "
           "Chrom /38.0.2125.122 Safari/537.36 SE 2.x MetaSr 1.0")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read()
fhandle = open("E:/pacong/3.html", "wb")
fhandle.write(data)
fhandle.close()
