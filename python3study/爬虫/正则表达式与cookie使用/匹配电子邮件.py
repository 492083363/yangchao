#!/bin/env python
#coding=utf-8

import re
pattern="\w+([.+-]\W*@\w+([.-]\w+.\w+([.-]\w+)*"    #匹配电子邮件的正则表达式
string="<a herf='http://www.baidu.com'>百度首页</a><br><a href='mailto:c-e+o@iqi-anyue.com.cn'>电子邮件地址</a>"
result=re.search(pattern,string)
print(result)
