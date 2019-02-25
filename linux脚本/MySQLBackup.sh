#!/bin/bash
#该脚本用来备份本机数据库
#使用rsync同步到172.31.101.100服务器上

mysqldump="/usr/local/mysql/bin/mysqldump"
backupuser="root"
password="abc@123"
backupdir="/data/backup"
remote_dir="rsync://172.31.101.100/mysqlbackup"
date1=`date +%F`
date2=`date +%d`

#定义日志,以下所有操作记录到日志中
exec &> /tmp/mysql_backup.log

echo "mysql backup begin at 'date'"

#对所有的数据库进行遍历
for db in db1 db2 db3 db4 db5     #数据库名称
do
    $mysqldum -u$backupuser -p$password $db >$backupdir/$db-$date1.sql
done

#对1天前的所有sql文件压缩
find $backupdir/ -type f -name ".sql" -mtime +1|xargs gzip

# 查找一周以前的老文件并删除
find #backupdir /-type -f -mtime +7 |xargs rm

#把当天的备份文件同步到远程
for db in db1 db2 db3 db4 db5
do
    rsync -a $backupdir /$db-$d1.sql $remote_dir/$db-$date2.sql
done

echo "mysql backup end at `date`"
    
