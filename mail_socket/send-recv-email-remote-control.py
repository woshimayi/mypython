#! /usr/bin/env python
# coding=utf-8
import ast
import base64
import json
import sys
import time
import poplib
import smtplib

# 邮件发送函数
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.parser import Parser
# 用来解析邮件主题
from email.header import decode_header
# 用来解析邮件来源
from email.utils import parseaddr


def parser_subject(msg):
    print(msg)
    subject = msg['Subject']
    value, charset = decode_header(subject)[0]
    if charset:
        value = value.decode(charset)
    # print('邮件主题： {0}'.format(value))
    return value


def parser_address(msg):
    hdr, addr = parseaddr(msg['From'])
    # name 发送人邮箱名称， addr 发送人邮箱地址
    name, charset = decode_header(hdr)[0]
    if charset:
        name = name.decode(charset)
    # print('发送人邮箱名称: {0}，发送人邮箱地址: {1}'.format(name, addr))
    return addr


def parser_content(msg):
    content = msg.get_payload()
    # 文本信息
    content_charset = content[0].get_content_charset()  # 获取编码格式
    text = content[0].as_string().split('base64')[-1]
    text_content = base64.b64decode(text).decode(content_charset)  # base64解码
    # print("===============", text_content)

    # print("content", len(content))
    # 添加了HTML代码的信息
    # content_charset = content[1].get_content_charset()
    # text = content[1].as_string().split('base64')[-1]
    # html_content = base64.b64decode(text).decode(content_charset)
    # print('文本信息: {0}\n添加了HTML代码的信息: {1}'.format(text_content, html_content))

    return text_content


def send_email(info):
    if info is None:
        return

    # sender是邮件发送人邮箱，passWord是服务器授权码，mail_host是服务器地址（这里是QQsmtp服务器）
    sender = 'xxxxxxxxxx@qq.com'
    passWord = 'xxxxxxxxxxxxxxxx'
    mail_host = 'smtp.qq.com'
    # receivers是邮件接收人，用列表保存，可以添加多个
    receivers = ['xxxxxxxxxx@qq.com']

    # 设置email信息
    msg = MIMEMultipart()
    # 邮件主题
    # msg['Subject'] = input(f"{'请输入邮件主题：'}")
    msg['Subject'] = str("auto")
    # 发送方信息
    msg['From'] = sender
    # 邮件正文是MIMEText:
    # msg_content = input(f"{'请输入邮件主内容:'}")

    msg_content = info
    msg.attach(MIMEText(msg_content, 'plain', 'utf-8'))

    try:
        # QQsmtp服务器的端口号为465或587
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        # s.set_debuglevel(1)
        s.login(sender, passWord)
        # 给receivers列表中的联系人逐个发送邮件
        for i in range(len(receivers)):
            to = receivers[i]
            msg['To'] = to
            s.sendmail(sender, to, msg.as_string())
            print('Success!', end='')
        s.quit()
        print("All emails have been sent over!", end='')
    except smtplib.SMTPException as e:
        print("Falied,%s", e)
    # 登录并发送邮件


# 邮件接收函数
def accpet_mail():
    try:
        p = poplib.POP3('pop.qq.com')

        # p.set_debuglevel(1)
        # print(p.getwelcome().decode('utf8'))
        p.user('xxxxxxxxxx@qq.com')
        p.pass_('xxxxxxxxxxxxxxxx')

        email_num, email_size = p.stat()
        # print("消息的数量: {0}, 消息的总大小: {1}".format(email_num, email_size))

        # 使用list()返回所有邮件的编号，默认为字节类型的串
        rsp, msg_list, rsp_siz = p.list()
        # print(
        #     "服务器的响应: {0},\n消息列表： {1},\n返回消息的大小： {2}".format(
        #         rsp, msg_list, rsp_siz))
        #
        # print('邮件总数： {}'.format(len(msg_list)))

        # 下面单纯获取最新的一封邮件
        total_mail_numbers = len(msg_list)
        rsp, msglines, msgsiz = p.retr(total_mail_numbers)
        # print("服务器的响应: {0},\n原始邮件内容： {1},\n该封邮件所占字节大小： {2}".format(rsp, msglines, msgsiz))

        msg_content = b'\r\n'.join(msglines).decode('gbk')

        msg = Parser().parsestr(text=msg_content)
        # print('解码后的邮件信息:\n{}'.format(msg))

        # 关闭与服务器的连接，释放资源
        p.quit()
        return msg

        # ret = p.stat() #返回一个元组:(邮件数,邮件尺寸)
        # p.retr('邮件号码') #方法返回一个元组:(状态信息,邮件,邮件尺寸)

    except poplib.error_proto:
        print("Login failed:")
        sys.exit(1)


# 运行当前文件时，执行sendmail和accpet_mail函数
if __name__ == "__main__":
    with open('auto.json', 'r') as f:
        # json_str = content1 = ast.literal_eval(f.read())
        json_str = f.read()
        print('json_str', json_str, type(json_str))
        # json_str = json.load(f)
    send_email(json_str)

    while 1:
        # 返回解码的邮件信息
        msg = accpet_mail()
        # 解析邮件主题
        subject = parser_subject(msg)
        # 解析发件人详情
        address = parser_address(msg)
        # 解析内容
        content = parser_content(msg)

        if "xxxxxxxxxx" not in address:
            print("not in addr")
            continue

        # print(subject, address, content)
        content1 = json.dumps(content)
        print('111111', content1)
        content2 = json.loads(content1)
        print('222222', content2)

        if subject in "auto":
            print('content', content, type(content))
            content1 = ast.literal_eval(content)
            print('content1', content1, len(content1))
            for i in range(len(content1)):
                if 'auto' == content1[0]['auto']:
                    print('auto', content1[0]['auto'])
        elif "https" in content:
            print('https', content)
