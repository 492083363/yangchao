#!/usr/bin/env python
#conding=utf-8
#python_verison=2.7.14
#zabbix_version=4.0
import requests

url = 'http://10.6.100.12/zabbix/api_jsonrpc.php'       # zabbix_api的url
header = {"Content-Type":"application/json"}            #定义http头部信息


def login():                                          #定义login()函数
    data = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": "Admin",
            "password": "Chucloud123$"
        },
        "id": 1,
        "auth":None
        }
    req = requests.post(url,json=data,headers=header)
    auth_token=req.json()
    return auth_token
print login()

