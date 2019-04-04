#!/bin/bash
#监控磁盘IO使用率，并找出磁盘磁盘使用率高的那个进程

#盘但是否安装iostat
if ! which iostat &>/dev/null
then
    yum install -y systat
fi

#判断是否安装iotop命令
if ! which iotop &>/dev/null
then
    yum install -y iotop
fi

#定义记录日志
logdir=/tmp/iolog
[ -d $logdir ]  || mkdir $logdir

#定义日至名字
dt=`date +%F`
#定义获取IO的函数，趣5次平均值
get_io()
{
    iostat -dx 1 5 > $logdir/iostat.log
    sum=0

    #提取最后一列的%util值循环便利然后相加
    for ut in `grep "^$1" $logdir/iostat.log|awk '{print $NF}'|cut -d. -f1`
    do 
        sum=$[ $sum + $ut ]
    done
    echo $[$sum/5]
}

while true
do
    #获取所有设备，对所有设备名遍立
    for d in `iostat -dx|egrep -v '^$|Device:|CPU\}'|awk '{print $1}'`
    do
        io=`get_io $d`
        #如果IO使用率大于等于80
        if  [[ $io -ge 80 ]];then
            #向日治理记录时间，iostat和iotop信息
            date >> $logdir/$dt
            cat $logdir/iostat.log >>$logdir/$dt
            iotop -obn2 >>$logdir/$dt
            echo '#####################' >> $logdir/$dt
        fi
    #休眠10秒，继续以上步骤
    done
    sleep 10
done