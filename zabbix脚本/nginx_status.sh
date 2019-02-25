#!/bin/bash
#zabbix监控nginx状态脚本，启用nginx_status模块使用
#开启zabbix自定义监控
# Set Variables
HOST=127.0.0.1
PORT="80"

if [ $# -eq "0" ];then 
    echo "Usage:$0(active|reading|writing|waiting|accepts|handled|requests|ping)" 
fi 

# Functions to return nginx stats
function active {
  /usr/bin/curl "http://$HOST:$PORT/nginx-status" 2>/dev/null| grep 'Active' | awk '{print $NF}'
  }
function reading {
  /usr/bin/curl "http://$HOST:$PORT/nginx-status" 2>/dev/null| grep 'Reading' | awk '{print $2}'
  }
function writing {
  /usr/bin/curl "http://$HOST:$PORT/nginx-status" 2>/dev/null| grep 'Writing' | awk '{print $4}'
  }
function waiting {
  /usr/bin/curl "http://$HOST:$PORT/nginx-status" 2>/dev/null| grep 'Waiting' | awk '{print $6}'
  }
function accepts {
  /usr/bin/curl "http://$HOST:$PORT/nginx-status" 2>/dev/null| awk NR==3 | awk '{print $1}'
  }
function handled {
  /usr/bin/curl "http://$HOST:$PORT/nginx-status" 2>/dev/null| awk NR==3 | awk '{print $2}'
  }
function requests {
  /usr/bin/curl "http://$HOST:$PORT/nginx-status" 2>/dev/null| awk NR==3 | awk '{print $3}'
  }
function ping {
    /sbin/pidof nginx | wc -l 
}
# Run the requested function
$1
