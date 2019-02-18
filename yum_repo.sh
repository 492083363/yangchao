#!/bin/bash
#change yum source
#name=yum_repo.sh

echo "========start============="
cd /etc/yum.repos.d/


echo "====backup repo==========="
mv CentOS-Base.repo CentOS-Base.repo.bak


echo "=create CentOS-Base.repo=="

touch CentOS-Base.repo
cat > CentOS-Base.repo << EOF
# CentOS-Base.repo
[base]
name=CentOS-$releasever - Base - 172.31.101.100
failovermethod=priority
baseurl=http://172.31.101.100/centos/7/os/x86_64/
gpgcheck=0

#released updates
[updates]
name=CentOS-$releasever - Updates - 172.31.101.100
failovermethod=priority
baseurl=http://172.31.101.100/centos/7/updates/x86_64/
gpgcheck=0

#additional packages that may be useful
[extras]
name=CentOS-$releasever - Extras - 172.31.101.100
failovermethod=priority
baseurl=http://172.31.101.100/centos/7/extras/x86_64/
gpgcheck=0

#additional packages that extend functionality of existing packages
[epel]
name=CentOS-$releasever - epel - 172.31.101.100
failovermethod=priority
baseurl=http://172.31.101.100/epel/7/x86_64/
gpgcheck=0



[zabbix]
name=CentOS-$releasever - zabbix - 172.31.101.100
failovermethod=priority
baseurl=http://172.31.101.100/zabbix/
gpgcheck=0

EOF

echo "====upgrade yum============"
yum clean all
yum makecache
yum update -y

echo "====dowload tools========="
yum install -y net-tools vim wget

cd ~

echo "=========finish============"
