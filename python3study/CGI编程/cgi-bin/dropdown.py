#!/bin/python
import cgi
import cgitb
form = cgi.FieldStorage()

if form.getvalue('dropdown'):
    dropdown = form.getvalue('dropdown')
else:
    dropdown = "null"

print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("<title>cainiaojiaocheng CGI</title>")
print("</head>")
print("<body>")
print("<h2> xuanzhongd1wangzhanshi %s</h2>" % dropdown)
print("</body>")
print("</html>")