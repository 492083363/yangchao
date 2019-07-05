#!/bin/python
import cgi
import cgitb
form = cgi.FieldStorage()

if form.getvalue('stie'):
    site = form.getvalue('site')
else:
    site = "null"

print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("<title>cainiaojiaocheng CGI</title>")
print("</head>")
print("<body>")
print("<h2> xuanzhongd1wangzhanshi %s</h2>" % site)
print("</body>")
print("</html>")
