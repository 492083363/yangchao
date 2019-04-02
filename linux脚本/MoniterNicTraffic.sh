#!/bin/bash
#监控网卡流量，当流量为0,重启网卡

#判断系统是否已经安装systat包，改包含有sar命令
if ! rpm -a sysstat &>/dev/null
then
    yum install -y sysstat
fi

#将10秒的网卡流量流量写入到一个临时文件里
sar -n DEV 1 10 |grep 'eth0' > /tmp/eth0_sar.log

#入口网卡流量
net_in=`grep '^Average:' /tmp/eth0_sar.log|awk '{print $5}'`

#出网卡流量
net_out=`grep '^Average:' /tmp/eth0_sar.log|awk '{print $6}'`

#当入口和出口流量同时为0时，说明网卡异常
if [$net_in == "0.00" -a $net_out =="0.00" ]
then
    echo "`date` eth0网卡出现异常，重启网卡。">> /tmp/net.log
    ifdown eth0 &7 ifup eth0
fi
