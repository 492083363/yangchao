#coding:utf-8
import json
import urllib2
import pickle
from django.conf import settings
#调用zabbix api测试示例

header = {"Content-Type": "application/json"}
def requestUrl(url,data):
    request = urllib2.Request(url,data)
    for key in header:
        request.add_header(key,header[key])
    response=None
    result_dict={}
    try:
        result = urllib2.urlopen(request)
        response=json.loads(result.read())
    except:
        print "Open url error."
    else:
        result.close()
    
    if response == None:
        pass
    elif response.has_key('error'):
        print response['error']['data']
    else:
        result_dict['return']=response['result']
        result_dict['id']=response['id']
    return result_dict

def login():
    url = settings.ZABBIX_URL+"/api_jsonrpc.php"
    data = json.dumps(
        {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
                   "user": settings.ZABBIX_USERNAME,
                   "password": settings.ZABBIX_PASSWORD
                   },
        "id": 0
        })
    result = requestUrl(url, data)
    return result
    
def logout(sessionid):
    url = settings.ZABBIX_URL+"/api_jsonrpc.php"
    data=json.dumps(
    {
        "jsonrpc": "2.0",
        "method": "user.logout",
        "params": [],
        "id": 1,
        "auth": sessionid
    }
    )
    return requestUrl(url, data)

def getHost(sessionid,groupids=[]):
    url = settings.ZABBIX_URL+"/api_jsonrpc.php"
    if len(groupids)==0:
        params_dict={
                  "output":["hostid","name","host"],
                  "selectInterfaces":["interfaceid","ip"],
        }
    else:
        params_dict={
                  "output":["hostid","name","host"],
                  "selectInterfaces":["interfaceid","ip"],
                  #"selectGroups":[""],
                  "groupids":groupids,
        }
    data=json.dumps(
    {
        "jsonrpc": "2.0",
        "method":"host.get",
        "params":params_dict,
        "auth":sessionid,
        "id":3,
    })
    return requestUrl(url, data)

def genHost(sessionid,ip,groupids):
    url = settings.ZABBIX_URL+"/api_jsonrpc.php"
    groups_list=[]
    for groupid in groupids:
        groups_list.append({"groupid":groupid})
    params_dict={
        "host": ip,
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": ip,
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": groups_list,
        "templates": [
            {
                "templateid": "10114"
            }
        ],
    }
    data=json.dumps(
    {
        "jsonrpc": "2.0",
        "method": "host.create",
        "params": params_dict,
        "auth": sessionid,
        "id" : 3
    })
    return requestUrl(url, data)

def delHost(sessionid,ip):
    url = settings.ZABBIX_URL+"/api_jsonrpc.php"
    hostid=0
    data=json.dumps(
    {
        "jsonrpc": "2.0",
        "method":"host.get",
        "params":{
            "output":["hostid","name","host"],
            "filter": {
                "host": [ip],
            }
        },
        "auth":sessionid,
        "id":3,
    })
    result=requestUrl(url, data)
    if len(result)==0:
        pass
    elif len(result['return'])==0:
        print "%s is not exists." % ip
    else:
        hostid=result['return'][0]['hostid']
        
    if hostid!=0:
        data=json.dumps({
            "jsonrpc": "2.0",
            "method": "host.delete",
            "params": [hostid],
            "auth":sessionid,
            "id":4
        })
        return requestUrl(url, data)
    
def updHostIp(sessionid,oldip,newip):
    url = settings.ZABBIX_URL+"/api_jsonrpc.php"
    #获取hostid
    hostid=0
    data=json.dumps(
    {
        "jsonrpc": "2.0",
        "method":"host.get",
        "params":{
            "output":["hostid","name","host"],
            "filter": {
                "host": [oldip],
            }
        },
        "auth":sessionid,
        "id":3,
    })
    result=requestUrl(url, data)
    if len(result)==0:
        pass
    elif len(result['return'])==0:
        print "Host %s is not exists." % oldip
    else:
        hostid=result['return'][0]['hostid']
        
    #获取interfaceid
    interfaceid=0
    data=json.dumps(
    {
        "jsonrpc": "2.0",
        "method":"hostinterface.get",
        "params":{
            "output":["interfaceid","hostid","ip"],
            "filter": {
                "ip": [oldip],
            }
        },
        "auth":sessionid,
        "id":3,
    })
    result=requestUrl(url, data)
    if len(result)==0:
        pass
    elif len(result['return'])==0:
        print "Interface %s is not exists." % oldip
    else:
        interfaceid=result['return'][0]['interfaceid']
        
    if hostid != 0 and interfaceid != 0:
        data_i=json.dumps({
            "jsonrpc": "2.0",
            "method": "hostinterface.update",
            "params": {
                "interfaceid": interfaceid,
                "ip": newip
            },
            "auth":sessionid,
            "id":5
        })
        result_i=requestUrl(url, data_i)
        
        if len(result_i) != 0:
            data=json.dumps({
                "jsonrpc": "2.0",
                "method": "host.update",
                "params": {
                "hostid": hostid,
                "name":newip,
                "host":newip,
                
                },
                "auth":sessionid,
                "id":5
            })
            return requestUrl(url, data)
        else:
            print "Interface update info:%s" % result_i

if __name__ == "__main__":
    pass


