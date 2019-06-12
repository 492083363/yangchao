#!/bin/bash
#查看消耗内存的进程

echo -e `date +%y%m%d%H%M`  
echo -e "PID\t\tMem\t\tProc_Name"

# 下面这个for是拿出/proc目录下所有以数字为名的目录（进程名是数字才是进程，其它如sys,net等存放的是其他信息）
for pid in `ls -l /proc | grep ^d | awk '{ print $9 }'| grep -v [^0-9]`
do
    if [ $pid -eq 1 ];then continue;fi
    grep -q "VmRSS" /proc/$pid/status 2&gt;/dev/null
    if [ $? -eq 0 ];then
        mem=$(grep VmRSS /proc/$pid/status \
            | gawk '{ sum+=$2;} END{ print sum }')
        proc_name=$(ps aux | grep -w "$pid" | grep -v grep \
            | awk '{ for(i=11;i&lt;=NF;i++){ printf("%s ",$i); }}')
        if [ $mem -gt 0 ];then
            echo -e "${pid}\t${mem}\t${proc_name}"
        fi 
    fi 
done | sort -k2 -n | awk -F'\t' '{
    pid[NR]=$1;
    size[NR]=$2;
    name[NR]=$3;
}
END{
    for(id=1;id&lt;=length(pid);id++)
    {
        if(size[id]&lt;1024)
            printf("%-10s\t%15sKB\t%s\n",pid[id],size[id],name[id]);
        else if(size[id]&lt;1048576)
            printf("%-10s\t%15.2fMB\t%s\n",pid[id],size[id]/1024,name[id]);
        else
            printf("%-10s\t%15.2fGB\t%s\n",pid[id],size[id]/1048576,name[id]);
    }
