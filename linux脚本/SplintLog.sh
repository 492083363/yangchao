#!/bin/bash
# 日志切割归档，按照大小切割（100M）,1.log变1.log.1,1.log.1变1.log2....

logdir=/data/logs/

#衡量1.log大小
size=`du -sk$logdir/1.log |awk {print $1}`

#如果1.log小于100M，则退出脚本

if [$size -lt 10240 ]
then 
    exit 0
fi

#定义函数，如果一个文件存在，则删除
fuction e_dr()
{
    if [ -f $1 ]
    then
        rm -f $1
    fi
 }
 
 cd $logdir
 #如果1.log.1存在，则先把它压缩为1.log.1.zg 这样下面的for循环才会出错
 fi [ -f 1.log.1 ]
 then
     gzip 1.log.1
 fi
 
 #由于1.log.1已经被压缩为1.log.gz，所以可以直接讲1.log改名为1.log.1
 
 mv 1.log 1.log.1
 
 #从7到2 倒序循环
 
 for i in `seq 7 -1 2`
 do
     #$i2比$i小1
     i2=$[$[i-1]
     
     #首先半段1.log.7.gz是否存在，若在在则删除
     edf 1.log.$i.gz
     
     #当1.log.6.gz存在，则把1.log.6.gz改名为1.log.7.gz，依次类推
     if [ -f 1.log.$i2.gz ]
     then
         mv 1.log.$i2.gz 1.log.#i.gz
     fi
     
  done
  
  #开启计划任务，按照日志大小进行切割，需要每分钟执行一次
  
