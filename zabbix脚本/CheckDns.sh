#!/bin/bash
#传递三个参数，例如监测dig www.baidu.com@202.103.44.150解析的ip地址是否正确
A=$(dig $1 +time=3 +short @$2)
if [ ${A} = $3 ]
then
  echo 1 
else
  echo 0
fi
