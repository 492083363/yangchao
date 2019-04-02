#!/usr/bin/env python3
#conding=utf-8
#python version=3.6

#通过ssh 保存交换机配置脚本

import paramiko

device_list = ['192.168.99.2']
device_username = 'admin'
device_password = ''

command = 'dis cu'

for each_device in device_list:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)
    client.connect(each_device,
                   port = 22,
                   username=device_username,
                   password=device_password,
                   allow_agent=False,
                   look_for_keys=False)
    stdin,stdout,stderr = client.exec_command(command)
    my_file = open(each_device,'w')
    for each_line in stdout.readlines():
        my_file.write(each_line)
    my_file.close()
