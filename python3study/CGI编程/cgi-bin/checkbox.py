#!/bin/python
import cgi,cgitb

form =cgi.FieldStorage()

if form.getvalue('google'):
    google_flag='yes'
else:
    google_flag='no'

if form.getvalue('菜鸟教程'):
    runoob_falg='yes'
else:
    runoob_flag='no'

print ("Content-type:text/html")
print ()
print ("<html>")
print ("<head>")
print ("<meta charset=\"utf-8\">")
print ("<title>菜鸟教程 CGI 测试实例</title>")
print ("</head>")
print ("<body>")
print ("<h2> 菜鸟教程是否选择了 : %s</h2>" % runoob_flag)
print ("<h2> Google 是否选择了 : %s</h2>" % google_flag)
print ("</body>")
print ("</html>")