#!/bin/python
import os
import http.cookies

print("Content-type:text/html")
print()

print("""
<html>
<head>
<meta charset="utf-8">
<title>cainiaojiaozheng</title>
</head>
<body>
<h1>read cookie message</h1>
""")


if 'HTTP_COOKIE' in os.environ:
    cookie_string = os.environ.get('HTTP_COOKIE')
    c = http.cookies.SimpleCookie()
    c.load(cookie_string)

try:
    data = c['name'].value
    print("cookie data: "+data+"<br>")
except KeyError:
     print("cookie is not set or has past<br>")

print("""
    </body>
    </html>
    """)