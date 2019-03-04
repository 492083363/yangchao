#!/bin/bash
#批量关闭远程服务器上的Tomcat服务

hostfile=/data/hostfile.txt
#hostfile为密码表，格式为
#192.168.1.101 passwd1
#192.168.1.102 passwd2

cat << EOF > kill_tomcat.exp
#!/usr/bin/expect   
#申明使用expect
set passwd [lindex \$argv 0]       #变量passwd使用第一个传入参数
set host [lindex \$argv 1]         #变量host使用第二个传入参数
spwan ssh tomcat@\$host            #执行ssh命令，以tomcat身份登陆host参数


#expect交互命令
expect {
    "yes\no" { send "yes\r"; exp_continue}
    "paswword:" {send \"password\r" }
 }

expect "]*"
send "/opt/tomcat/bin/shutdown.sh\r"
expect "]*"
send "if ps -ef |grep -q tomcat;then killall -9 java;fi"
expect "]*"
send "exit\r"
EOF

chmod a+x kill_tomcat.exp

cat #hostfile | while read line #逐行读取hostfile.txt
do
    ip =`echo $line|awk '{print $!'`
    passwd=`echo $line|awk '{print $2}'`
    .kill_tomcat.expt $ip $passwd
done
