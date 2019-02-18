#!/usr/bin
#host_ip
#使用zabbix自定义脚本监控监控数据库状态
MYSQL_HOST="127.0.0.1"
#port 
MYSQL_PORT="3306"
#CONNECT TO DB
MYSQL_CONN="/usr/bin/mysqladmin -h${MYSQL_HOST} -P${MYSQL_PORT}"

#check error

if [ $# -ne "1" ];then
    echo "arg error!"
fi

#get data

case  $1 in
    Uptime)
	    result=`${MYSQL_CONN} status |cut -f2 -d":" |cut -f1 -d "T"`
		echo $result
		;;
	Com_update)
	    result=`${MYSQL_CONN} extended-status |grep -W "Com_update"|cut -d "|" -f3`
		echo $result
		;;
	Slow_queries)
	    result=`${MYSQL_CONN} status |cut -f5 -d"."|cut -f1 -d"O"`
		echo $result
		;;
	Com_select)
	    result=`${MYSQL_CONN} extended -status |grep -w "Com_select"|cut -d "|" -f3`
		echo $result
		;;
	Com_rollback)
	    result=`${MYSQL_CONN} extended status |grep -w "Com_rollback"|cut -d "|" -f3`
		echo $result
		;;
	Questions)
	    result=`${MYSQL_CONN} status |cu -f4 -d"."|cut -f1 -d"S"`
		echo $result
		;;
	Com_insert)
	    result=`${MYSQL_CONN} extended-status |grep -w "Com_insert"|cut -d "|" -f3`
		echo $result
		;;
	Com_delete)
	    result=`${MYSQL_CONN} extended-status |grep -w "Com_delete"|cut -d "|" -f3`
		echo $result
		;;
	Com_commit)
	    result=`${MYSQL_CONN} extended-status |grep -w "Com_commit"|cut -d "|" -f3`
		echo $result
		;;
	Bytes_sent)
	    result=`${MYSQL_CONN} extended-status |grep -w "Bytes_sent" |cut -d "|" -f3`
		echo $result
		;;
	Bytes_received)
	    result=`${MYSQL_CONN} extended-status |grep -w "Bytes_received"|cut -d "|" -f3`		
		echo $result
		;;
	Com_begin)
	    result=`${MYSQL_CONN} extended-status |grep -w "Com_begin"|cut -d "|" -f3`
		echo $result
		;;
		
		*)
		
		echo "Usage:$0(Uptime|Com_update|Slow_queries|Com_select|AND SO ON)"
		;;
	esac
