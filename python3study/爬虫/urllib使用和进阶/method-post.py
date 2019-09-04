#POST
#http://httpbin.org      testing website
from urllib.request import Request,urlopen
from urllib.parse import urlencode
import simplejson

request=Request('http://httpbin.org/post')
request.add_header(
    'User-agent',
    'Mozilla/5.0 (Windows NT 6.1; WOW64 )" AppleWebKit/537.36 (KHTML,like Gecko) Chrom /38.0.2125.122 Safari/537.36 SE 2.x MetaSr 1.0'
)
data=urlencode({'name':'杨超,@=/&*','age':6})

print(data)

#response=urlopen(request,data=data.encode())   #POST方法。Form提交数据

#with response:
#   print(response.read())


with urlopen(request,data=data.encode()) as response:
    text =response.read()
    d=simplejson.loads(text)        #使用json格式
    print(d)
    print(type(d))

