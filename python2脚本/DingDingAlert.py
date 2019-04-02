#!/usr/bin/python
# -*- coding: utf-8 -*-
#zabbix上使用钉钉告警机器人，调用api脚本
import requests
import json
import sys
import os

headers = {'Content-Type': 'application/json;charset=utf-8'}
#定义json http头部信息
api_url = "https://oapi.dingtalk.com/robot/send?access_token=019cd25ef1b8cee2fbbf7c16429687ac5cd66803d214408470e3a0b5454834e4"
#这里的url是钉钉机器人的api url

def msg(text):                                   #定义函数msg,参数为txt
    json_text= {                                 #定义json_text字典内容
     "msgtype": "text",
        "text": {
            "content": text
        },
    }
    print requests.post(api_url,json.dumps(json_text),headers=headers).content  #将字典信息序列化为json格式发送

if __name__ == '__main__':                    #主函数
    text = sys.argv[1]                        #传入zabbix定义动作参数，已经在zabbix告警动作中配置
    msg(text)                                 #调用msg (text)函数
