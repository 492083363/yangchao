#!/bin/bash
#count the linux server 's  process number
running=0
sleeping=0
stoped=0
zombie=0

for pid in /proc/[1-9]*
do 
    procs=$[procs+1]
    stat=$(awk'{print $3}' $pid/stat)

    case $stat in
    R)
        running=$[running+1]
        ;;
    T)
        stoped=$[stoped+1]
        ;;
    S)
        sleeping=$[sleeping+1]
        ;;
    Z)
        zombie=$[zombie+1]
        ;;
    esac
done

echo ""
echo ""
echo ""
echo ""
echo ""
echo ""