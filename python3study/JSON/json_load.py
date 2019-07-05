#!/bin/python
import json
# Python字典类型转换为JSON对象

data1 = {
    'no': 1,
    'name': 'baidu',
    'url': 'http://www.baidu.com'
}
json_str = json.dumps(data1)
print("Python原始数据：", repr(data1))
print("JSON对象：", json_str)

# 将json对象转换为Python字典
data2 = json.loads(json_str)
print("data2['name']:", data2['name'])
print("data2['url']:", data2['url'])
