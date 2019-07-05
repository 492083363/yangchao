#!/bin/python

import cgi,cgitb

form = cgi.FieldStorage()

site_name =form.getvalue('name')
site_url = form.getvalue('url')

print ("Content-type:text/html")
print ()
print ("<html>")
print("<head>")
print ("<meta charset=\"utf-8\">")
print ("<title>cainiao</title>")
print ("</head>")
print ("<body>")
print ("<h2>%sguanwang:%s</h2>" % (site_name,site_url))
print ("</body>")
print("</html>") 
