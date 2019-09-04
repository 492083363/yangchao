# 连接bing搜索网站，获取一个搜索的URL http://cn.bing.com/search?q=杨超
#POST
# 需求
# 编写车光绪完成对关键字的bing的搜索，将返回的结果保存到一个网页文件中

from urllib.request import urlopen, Request
from urllib. parse import urlencode

keyword = input('>>请输入搜索关键字')
data = urlencode({
    'q': keyword
})

base_url = 'http://cn.bing.com/search'

url = '{}?{}'.format(base_url, data)
print(url)

# 伪装
ua = 'Mozilla/5.0 (Windows NT 6.1; WOW64 )" AppleWebKit/537.36 (KHTML,like Gecko) Chrom /38.0.2125.122 Safari/537.36 SE 2.x MetaSr 1.0'

request = Request(url, headers={
    'User-agent': ua
})

response = urlopen(request)
with response:
    with open('/home/yangchao/桌面/pachong/bing.html', 'wb+') as f:
        f.write(response.read())
        f.flush()

print('success')
