爬虫
====
#通用爬虫
常见的的就是搜索引擎，无差别的收集数据、存储、提取关键字，构建索引库，给用户提供搜索接口
#爬取一般流程
* 1、初始一批URL，将这些URL放到待爬去列队
* 2、列队取出这些URL，通过DNS解析IP，对IP对应的站点下载HTML页面，保存到本地服务器中，爬取完的URL放到已爬取的列队中
* 3、分析这些网页的内容，找出网页里面的其他的关系的URL连接，继续执行第二步，直到爬取条件结束
搜索引擎如何获取一个新网站的URL
* 新网站主动提交给搜索引擎
* 通过其他网站页面中设置的外链
* 搜索引擎和DNS服务商合作，获取最新收录的网站


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
