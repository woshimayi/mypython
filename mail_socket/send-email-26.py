# -*- coding: utf-8 -*-

import smtplib
import threading
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import sys, os
import time
from winsound import Beep

send_flag = 0

def send_email(file):
    if file is None:
        return
    # 发送文件名
    filename = file.split('\\')[-1]
    global send_flag

    #sender是邮件发送人邮箱，passWord是服务器授权码，mail_host是服务器地址（这里是QQsmtp服务器）
    sender = '2638288078@qq.com'
    passWord = 'dajqsprqcbececgf'
    mail_host = 'smtp.qq.com'
    #receivers是邮件接收人，用列表保存，可以添加多个
    receivers = ['2638288078@qq.com']
    send_flag = 1

    #设置email信息
    msg = MIMEMultipart()
    #邮件主题
    # msg['Subject'] = input(f"{'请输入邮件主题：'}")
    msg['Subject'] = str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
    #发送方信息
    msg['From'] = sender
    #邮件正文是MIMEText:
    # msg_content = input(f"{'请输入邮件主内容:'}")
    send_flag = 2

    msg_content = filename
    msg.attach(MIMEText(msg_content, 'plain', 'utf-8'))
    # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
    with open(file, 'rb') as f:
        # 设置附件的MIME和文件名，这里是jpg类型,可以换png或其他类型:
        mime = MIMEBase('image', 'jpg', filename=filename)
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename=filename)
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)
    send_flag = 3

    try:
        #QQsmtp服务器的端口号为465或587
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        # s.set_debuglevel(1)
        s.login(sender,passWord)
        send_flag = 4
        #给receivers列表中的联系人逐个发送邮件
        for i in range(len(receivers)):
            to = receivers[i]
            msg['To'] = to
            s.sendmail(sender,to,msg.as_string())
            print('Success!', end='')
        s.quit()
        send_flag = 5
        # print ("All emails have been sent over!", end='')
    except smtplib.SMTPException as e:
        print ("Falied,%s",e)
    #登录并发送邮件

def progress_bar():
    global send_flag
    while 1:
        print("\r", end="")
        if send_flag != 5:
            for i in range(0,80):
                print("\r", end="")
                print("{}%: ".format(i), "▋" * (i // 2), 'send email', end="")
                sys.stdout.flush()
                time.sleep(0.01)
                i = i + 1
        else:
            print("{}%: ".format(100), "▋" * (100 // 2), 'Success!', end="")
            sys.stdout.flush()
            time.sleep(0.01)
        if send_flag == 5:
            break


if __name__ == "__main__":
    if 2 != len(sys.argv):
        print("get file fail")
        sys.exit()

    print(sys.argv[1])
    # input("input file:")
    # file = r'C:\Users\zs\Pictures\105846277.jpg'
    file = sys.argv[1]
    # print(file.split('\\')[-1])

    Beep(400, 100)
    th1 = threading.Thread(target=progress_bar)
    th2 = threading.Thread(target=send_email, args=(file,))

    th1.start()
    th2.start()

    th1.join(2)
    th2.join(2)
    Beep(500, 300)
    sys.exit()