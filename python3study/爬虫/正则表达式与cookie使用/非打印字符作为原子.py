#!/bin/env python
#coding=utf-8

import re
pattern="\n"                #\n匹配换行符，\t匹配制表符
string='''http://yum.iqianyue.com
http://baidu.com'''             #此处有换行
result1=re.search(pattern,string)
print(result1)

