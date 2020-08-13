# -*-coding:utf-8 -*-


import smtplib 
import email.MIMEMultipart
import email.MIMEText
import email.MIMEBase
import os.path
import mimetypes

import sys
import os

def PP():
    print sys._getframe().f_back.f_lineno, sys._getframe(1).f_code.co_name 


From = 'xxxxxxxxxxxxxxx@twsz.com'
To = 'xxxxxxxxxxxxxxxxxxxx@qq.com'
file_name = 'D:\\timeview.jpg'
PP()
server = smtplib.SMTP('mailsh.twsz.com')
server.login('xxxxxxxxxxxxxxxxxx@twsz.com', 'zs.2017')
PP()
main_msg = email.MIMEMultipart.MIMEMultipart()

text_msg = email.MIMEText.MIMEText('this is a test to text mine', _charset='utf-8')
main_msg.attach(text_msg)
PP()
date = open(file_name, 'rb')
ctype, encodeing = mimetype.guess_type(file_name)
if ctype is None or encodeing is not None:
	PP()
	ctype = 'application/octet-stream'
PP()
maintype, subtype = ctype.split('/',1)
file_msg = email.MIMEBase.MIMEBase(maintype, subtype)
file_msg.set_payload(data.read())
date.close()
PP()

email.Encoder.encode_base64(file_msg)

PP()

basename = os.path.basename(file_name)
file_msg.add_header('Content-Disponition', 'attachment', filename = basename)
main_msg.attach(file_name)
PP()
main_msg['From'] = From
main_msg['To'] = To
main_msg['Subject'] = 'attch test'
main_msg['Date'] = email.Utils.formatdate()
PP()
fullText = main_msg.as_string()
PP()
try:
	server.sendmail(From, To, fullText)
finally:
	server.quit()