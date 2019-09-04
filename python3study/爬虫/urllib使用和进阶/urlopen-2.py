
from urllib.parse import urlencode
from urllib.request import urlopen,Request
import simplejson
ua = 'Mozilla/5.0 (Windows NT 6.1; WOW64 )" AppleWebKit/537.36 (KHTML,like Gecko) Chrom /38.0.2125.122 Safari/537.36 SE 2.x MetaSr 1.0'
jurl = 'https://movie.douban.com/j/search_subjects'
d={
    'type':'move',
    'tag':'热门',
    'page_limit':10,
    'page_start':10l
}

req=Request('{}?{}'.format(jurl,urlencode(d)),headers={
    'User-agent':ua
})

with urlopen(req) as res:
    print(simplejson.loads(res.read()))
