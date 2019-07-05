#coding=utf-8
import json
#Python字典类型转换为JSON 对象
data={
    'no':1,
    'name':'baidu',
    'url':'http://www.baidu.com'
}
json_str=json.dumps(data)
print ("Python原始数据：",repr(data))
print ("JSON对象：",json_str)

