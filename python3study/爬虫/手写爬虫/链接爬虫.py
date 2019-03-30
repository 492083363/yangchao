# coding=utf-8
# 爬取制定页面链接
import re
import urllib.request


def getlink(url):
    # 模拟成浏览器
    headers = ("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64 )"
               " AppleWebKit/537.36 (KHTML,like Gecko)"
               " Chrom /38.0.2125.122 Safari/537.36 SE 2.x MetaSr 1.0")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    # 将opener安装成全局
    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(url)
    data = str(file.read())
    # 根据需求构建好链接表达式
    pat = '(https?://[^\s)*;]+\.(\w|/)*)'  # 确定简单版链接的基本格式为http://xxx.yyy
    link = re.compile(pat).findall(data)
    # 去除重复元素
    link = list(set(link))
    return link


# 要爬取的网页链接
url = "http://blog.csdn.net/"
# 获取对应网页中包含的链接地址
linklist = getlink(url)
# 通过for循环分别遍历输出获取到的链接地址到屏幕上
for link in linklist:
    print(link[0])
