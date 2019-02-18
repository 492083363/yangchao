/bin/bash
#identity user is a superuser
#script_mane=ops-allinone-nodemo-custnetwork-v3.sh
#使用packstack工具部署allinone环境的opentstack,版本为queen
if [ `id -u` != 0 ];then
	echo "Please Run it using User root"
	exit 10
fi
#env check
	echo "Run environment check......."
	rpm -qa |grep yum-utils &> /dev/null  || yum -y install yum-utils &> /dev/null && echo "environment check complete" ||(echo "no yum-utils package exist,Please install it manual";exit 10)

#enable and disabled Services
echo "Disable and Enable SomeService......."
systemctl disable firewalld &> /dev/null
if [ $? = 0 ];then
	systemctl stop firewalld &> /dev/null
	if [ $? = 0 ];then
		systemctl disable NetworkManager &> /dev/null
		if [ $? = 0 ];then
			systemctl stop NetworkManager &> /dev/null	
			if [ $? = 0 ];then
				systemctl enable network &> /dev/null
				if [ $? = 0 ];then
					 systemctl start network &> /dev/null
					 if [ $? = 0 ];then
						echo "All Service's Status is normal"
					 else
						echo "Start network service failed"
						exit 10
					 fi
				else
					echo "Enable network service failed"
					exit 10
				fi
			else 
				echo "Stop NetworkManager Service failed"
				exit 10
			fi
		else 
			echo "Disabled  NetworkManager Service failed"
			exit 10
		fi
	else
		echo "Stop firewalld Servie failed"
		exit 10 
	fi
else 
	echo "Disabled firewalld failed"
	exit 10
fi
#testing network 
echo "Now Testing your Ineternet Netowrk ......."	
	ping -c 3 8.8.8.8 &> /dev/null  && echo "Network test is complete" ||(echo "Network test is failed,Please make sure your network can connect Internet " ;exit 10)
#yum install openstack queens
echo "Now install openstack queens's software repo......"
	yum install -y centos-release-openstack-queens &> /dev/null  && echo "Install repo complete,Next will enabled this repo"|| (echo "Install repo failed. Please check your network"; exit  10)
#enabled yum repo
echo "enabled yum repo......"
	yum-config-manager --enable openstack-queens &> /dev/null && echo "yum repo enabled ."||(echo "enabled repo failed";exit 10)
#now to update your software  to lastest 
	echo "now to update your software  to lastest......"
	yum update -y &> /dev/null  && echo "Update  complete "||(echo "Update failed";exit 10)
#now to install openstack-packstack tools
echo "now to install openstack-packstack tools....."	
	yum install -y openstack-packstack &> /dev/null && echo  "Install  packstack  complete"||(echo "Install packstack failed";exit 10)
	
#configure external network nic
NICS=$(ip link sh|grep ^[0-9]|cut -d: -f 2|grep -v lo|nl)
echo "$NICS"   > nicinfo.txt
echo -n  -e "Please Select a NIC set uplink for br-ex:\n$NICS\n"
read NUM
NIC=$(cat  nicinfo.txt |sed 's/^[ \t]*//g'|grep ^[$NUM]|awk -F" " '{print $2}')
echo -n -e "Your Select NIC is $NIC ,Please Makesure use it [yes/no]\n"
read N
N1=$(echo $N|tr 'A-Z' 'a-z')
case $N1 in
	yes)
#now start using packstack deploy Allinone Openstack 
echo "now start using packstack deploy Allinone Openstack"
packstack --allinone --provision-demo=n --os-neutron-ovs-bridge-mappings=extnet:br-ex --os-neutron-ovs-bridge-interfaces=br-ex:$NIC --os-neutron-ml2-type-drivers=vxlan,flat,vlan 
	if [ $? = 0 ];then
	echo -n -e "Now,Start to configure your network switch br-ex useing $NIC\n"
        IP=$(ip add sh $NIC|grep -w inet|cut -d' ' -f 6|cut -d'/' -f 1)
        MASK=$(ip add sh $NIC|grep -w inet|cut -d' ' -f 6|cut -d'/' -f 2)
        GW=$(route -n|grep ^0.0.0.0|awk -F' ' '{print $2}')
        DNS=$(cat /etc/resolv.conf|grep ^nameserver|cut -d' ' -f 2)

        cat > /etc/sysconfig/network-scripts/ifcfg-br-ex <<-EOF
TYPE=OVSBridge
BOOTPROTO=none
DEVICE=br-ex
ONBOOT=yes
DEVICETYPE=ovs 
IPADDR=$IP
PREFIX=$MASK
GATEWAY=$GW
DNS1=$DNS
EOF
        cat >/etc/sysconfig/network-scripts/ifcfg-$NIC <<-EOF
TYPE=OVSPort
DEVICE=$NIC
ONBOOT=yes
DEVICETYPE=ovs
OVS_BRIDGE=br-ex
EOF

echo "Please using service network restart common to restart your network "
else
	echo "Install Failed Please Check Your network and run this script again"
fi
	;;
	no)
	echo "Please rerun this script"
	exit 10
	;;
esac
