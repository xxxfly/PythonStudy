#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr,formataddr
import smtplib


# msg=MIMEText('hello,send by Python..','plain','utf-8')
# #输入Eamil的地址和口令
# from_addr=input('From:')
# password=input('Password:')
# #输入收件人地址：
# to_addr=input('To:')
# #输入SMTP服务器地址：
# smtp_server=input('SMTP server:')

# server=smtplib.SMTP(smtp_server,465) #SMTP协议默认端口25 QQ邮箱为465或587
# server.set_debuglevel(1)
# server.login(from_addr,password)
# server.sendmail(from_addr,[to_addr],msg.as_string())
# server.quit()

# def _format_addr(s):
#     name,addr=parseaddr(s)
#     return formataddr((Header(name,'utf-8').encode(),addr))

# from_addr=input('From:')
# password=input('Password:')
# to_addr=input('To:')
# smtp_server=input('SMTP server:')

# msg=MIMEText('Hello,send by python...','plain','utf-8')
# msg['From']=_format_addr('Python爱好者<%s>'%from_addr)
# msg['To']=_format_addr('管理员 <%s>'%to_addr)
# msg['Subject']=Header('来自SMTP的问候...','utf-8').encode()

# server=smtplib.SMTP(smtp_server,587)
# server.set_debuglevel(1)
# print('login...')
# server.login(from_addr,password)
# server.sendmail(from_addr,[to_addr],msg.as_string())
# server.quit()

#发送HTML邮件
# msg=MIMEText('<html><body><h1>Hello</h1><p>send by <a href="http://www.python.org">Python</a>...</p></body></html>','html','utf-8')

#发送附件
# msg=MIMEMultipart()


