# 网页使用utf-8编码
# https://www.baidu.com/s？wd=中
# 上面的url的比编码后，如下
# https://www.baidu.com/s?wd=%E4%B8%%AD

from urllib import parse
u = parse.urlencode({'wd': '中'}) #编码
url = 'https://www.baidu.com/s?{}'.format(u)
print(url)

print('中'.encode('utf-8'))

print(parse.unquote(u)) #解码
print(parse.unquote(url))
