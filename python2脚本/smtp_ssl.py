#!/usr/bin/python
#coding=utf-8
#smtp模块发送邮件脚本
import smtplib
import string
from smtplib import SMTP_SSL  #采用SSL加密模块
HOST = "smtp.xxxxxxxx.com" #定义smtp主机
SUBJECT = "Test email from Python" #定义邮件主题
TO = "yangchao@chucloud.com.cn" #定义邮件收件人
FROM = "xxxxxxx.xxxxxxx@chucloud.com.cn" #定义邮件发件人
text = "Python rules them all!"     #邮件内容
BODY = string.join((                #组装sdemail方法的邮件内容，各段以"\r\n"进行分隔
        "From: %s" % FROM,          
        "To: %s" % TO,
        "Subject: %s" % SUBJECT ,
        "",
        text
        ), "\r\n")
server = SMTP_SSL()            #创建一个SMTP()对象,采用SSL加密
server.connect(HOST,"465")           #通过connect方法连接smtp主机
server.login("xxx.xxxxxxxxx@chucloud.com.cn","xxxxxxxxxx")   #邮箱账号登录校验
server.sendmail(FROM, [TO], BODY)  #邮件发送
server.quit()                      #断开连接
