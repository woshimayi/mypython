# -*- coding: utf-8 -*-

import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

import sys, os

#sender���ʼ����������䣬passWord�Ƿ�������Ȩ�룬mail_host�Ƿ�������ַ��������QQsmtp��������
sender = '2638288078@qq.com'
passWord = 'dajqsprqcbececgf'
mail_host = 'smtp.qq.com'
#receivers���ʼ������ˣ����б��棬������Ӷ��
receivers = ['2638288078@qq.com','2638288078@qq.com']

#����email��Ϣ
msg = MIMEMultipart()
#�ʼ�����
# msg['Subject'] = input(f"{'�������ʼ����⣺'}")
msg['Subject'] = "text"
#���ͷ���Ϣ
msg['From'] = sender
#�ʼ�������MIMEText:
# msg_content = input(f"{'�������ʼ�������:'}")
msg_content = "text"
msg.attach(MIMEText(msg_content, 'plain', 'utf-8'))
# ��Ӹ������Ǽ���һ��MIMEBase���ӱ��ض�ȡһ��ͼƬ:
with open('C:/Users/zs/Pictures/123.jpg', 'rb') as f:
    # ���ø�����MIME���ļ�����������jpg����,���Ի�png����������:
    mime = MIMEBase('image', 'jpg', filename='Lyon.png')
    # ���ϱ�Ҫ��ͷ��Ϣ:
    mime.add_header('Content-Disposition', 'attachment', filename='Lyon.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # �Ѹ��������ݶ�����:
    mime.set_payload(f.read())
    # ��Base64����:
    encoders.encode_base64(mime)
    # ��ӵ�MIMEMultipart:
    msg.attach(mime)


if __name__ == "__main__":
    if 2 >= len(sys.argv):
        print("get file fail")
        return False
    #��¼�������ʼ�
    try:
        #QQsmtp�������Ķ˿ں�Ϊ465��587
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.set_debuglevel(1)
        s.login(sender,passWord)
        #��receivers�б��е���ϵ����������ʼ�
        for i in range(len(receivers)):
            to = receivers[i]
            msg['To'] = to
            s.sendmail(sender,to,msg.as_string())
            print('Success!')
        s.quit()
        print ("All emails have been sent over!")
    except smtplib.SMTPException as e:
        print ("Falied,%s",e)