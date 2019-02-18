#!/bin/sh
#备份zabbix数据库
DUMP=/usr/bin/mysqldump
OUT_DIR=/backup/mysql_backup
LINUX_USER=root
DB_NAME=zabbix
DB_USER=root
DB_PASS=123456
cd $OUT_DIR
DATE=`date +%Y%m%d`
OUT_SQL="$DATE.sql"
TAR_SQL="data_bak_$DATE.tar.gz"
$DUMP -u $DB_USER -p$DB_PASS $DB_NAME --default-character-set=utf8 --opt -Q -R --skip-lock-tables --master-data=1 > $OUT_SQL
tar -czf $TAR_SQL ./$OUT_SQL
rm $OUT_SQL
find /backup/mysql_backup/ -name 'data_bak*' -ctime +10 -exec rm -f {} \;
