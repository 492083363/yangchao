urlib
====
#urllib是标准库，它是一个工具包模块，包含下面的模块来处理url
*  urllib.request用于打开和读写url:
*  urllib.error包含了由urllib.request引起的异常
*  urllib.parse用于解析url
*  urllib.robotparser分析robots.txt文件

python提供了urllib和urllib2
python3中将urlib合并到了urllib2中，并只提供了标准库urllib包

#提交方法mehod

最常用的HTTP交互数据的方法是GET POST
GET方法，数据是通过URL传递，也就是说数据是在HTTP报文的header部分
POST方法，数据是放在HTTP报文的body部分提交的
数据都是健值对形式，多个参数之间使用&符号连接，例如a=1&b=abc

##GET方法
