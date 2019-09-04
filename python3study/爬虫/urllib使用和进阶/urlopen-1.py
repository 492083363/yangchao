from urllib.request import urlopen,Request

# 打开一个url返回一个响应对象，类文件对象
# 下面的连接访问后会有跳转
url='http://www.bing.com'
ua = 'Mozilla/5.0 (Windows NT 6.1; WOW64 )" AppleWebKit/537.36 (KHTML,like Gecko) Chrom /38.0.2125.122 Safari/537.36 SE 2.x MetaSr 1.0'
req=Request(url,headers={
    'User-agent':ua
})
#req.add_header('User-agent',ua)

#response = urlopen('http://www.bing.com',timeout=5)
response = urlopen(req,timeout=5)

print(response.closed)              #GET方法
with response:
    print(1, type(response))    #http.client.HTTPResponse类文件对象
    print(2, response.status, response.reason)  #状态
    print(3, response.geturl())   #返回真正的url
    print(4, response.info())      #headers
  #  print(5, response.read())     #读取返回的内容

print(response.closed)
