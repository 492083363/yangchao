#!/bin/python

import os

print ("Conten-type: tex/html")
print ()
print ("<meta charset=\"utf-8\">")
print ("<url>")
for key in os.environ.keys():
    print ("<li><span style='color:green'>%30s </span>: %s </li>" % (key,os.environ[key]))
print("</url>")
