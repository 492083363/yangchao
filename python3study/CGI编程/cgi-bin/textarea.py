#!/bin/python
import cgi
import cgitb
form = cgi.FieldStorage()

if form.getvalue('textcontent'):
    text_content = form.getvalue('textcontent')
else:
    text_content = "null"

print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("<title>cainiaojiaocheng CGI</title>")
print("</head>")
print("<body>")
print("<h2> your input data is %s</h2>" % text_content)
print("</body>")
print("</html>")
