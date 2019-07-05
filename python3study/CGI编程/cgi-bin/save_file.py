#!/bin/python
#coding=utf-8
import cgi
import os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

fileitem = form['filename']

if fileitem.fillename:
    fn = os.path.basename(fileitem.filename)
    open('/var/www/upload/'+fn, 'wb').write(fileitem.file.read())
    message = 'file"'+fn+'"upload success!'

else:
    message = 'upload failed'

print("""\
Content-Type:text/html\n
<html>
<head>
<meta charset="utf-8">
<title>cainiaojiaozheng</title>
</head>
<body>
    <p>%s</p>
</body>
</html>
""" % (message,))
