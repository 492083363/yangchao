#!/bin/bash
#检查花生壳ddns域名解析是否正确
A=$(nslookup chucloud.giize.com|grep Add|grep -v "#"|cut -d : -f 2)
B=$(wget http://ipecho.net/plain -O - -q ; echo)
if [ ${A} = ${B} ];then
    echo '1'
else
    echo '0'
fi
