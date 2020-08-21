import logging
import smtplib
import sys
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.parser import Parser
from email.header import decode_header, Header
from email.utils import parseaddr
import poplib

# 设置logging的等级以及打印格式
from digital_my import BeautifulPicture

logging.basicConfig(
    level=logging.ERROR,
    format='[%(funcName)s:%(lineno)d] - %(levelname)s: %(message)s')


class Auto_ctrl(object):
    """docstrinAuto_ctrlssName"""

    def __init__(self):
        logging.debug('==== recv email ====')
        # 输入邮件地址, 口令和POP3服务器地址:
        self.email = 'xxxxxxxxxxxx@qq.com'
        self.password = 'xxxxxxxxxxxxxxxxxx'  # 这个密码不是邮箱登录密码，是pop3服务密码
        self.pop3_server = 'pop.qq.com'
        self.email_num = 0

    def decode_str(self, s):
        value, charset = decode_header(s)[0]
        if charset:
            value = value.decode(charset)
        return value

    def print_info(self, msg):
        # 输出发件人，收件人，邮件主题信息
        info = []
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = self.decode_str(value)  # 将主题名称解密
                else:
                    hdr, addr = parseaddr(value)
                    name = self.decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            logging.debug('%s: %s' % (header, value))
            info.append(value)
        # logging.debug('===== %s' % info)
        # 获取邮件主体信息
        attachment_files = []
        for part in msg.walk():
            file_name = part.get_filename()  # 获取附件名称类型
            contentType = part.get_content_type()  # 获取数据类型
            mycode = part.get_content_charset()  # 获取编码格式
            if file_name:
                h = Header(file_name)
                dh = decode_header(h)  # 对附件名称进行解码
                filename = dh[0][0]
                if dh[0][1]:
                    filename = self.decode_str(
                        str(filename, dh[0][1]))  # 将附件名称可读化
                attachment_files.append(filename)
                data = part.get_payload(decode=True)  # 下载附件
                with open(filename, 'wb') as f:  # 在当前目录下创建文件，注意二进制文件需要用wb模式打开
                    #with open('指定目录路径'+filename, 'wb') as f: 也可以指定下载目录
                    f.write(data)  # 保存附件
                logging.debug(f'附件 {filename} 已下载完成')
            elif contentType == 'text/plain':  # or contentType == 'text/html':
                # 输出正文 也可以写入文件
                data = part.get_payload(decode=True)
                content = data.decode(mycode)
                logging.debug('正文：%s' % content)
                logging.debug('附件文件名列表 %s' % attachment_files)
                info.append(content)
        return info

    def recv_email(self):
        # 连接到POP3服务器:
        server = poplib.POP3_SSL(self.pop3_server, 995)
        # 可以打开或关闭调试信息:
        # server.set_debuglevel(1)
        # 可选:打印POP3服务器的欢迎文字:
        logging.debug(server.getwelcome().decode('utf-8'))
        # 身份认证:
        server.user(self.email)
        server.pass_(self.password)
        # stat()返回邮件数量和占用空间:
        logging.debug('Messages: %s. Size: %s' % server.stat())
        # list()返回所有邮件的编号:
        resp, mails, octets = server.list()
        # 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
        logging.debug(mails)
        # 由于pop3协议不支持对已读未读邮件的标记，因此，要判断一封pop邮箱中的邮件是否是新邮件必须与邮件客户端联合起来才能做到。
        index = len(mails)
        logging.error('未读邮件的数量 %s: 已知邮件: %s', index, self.email_num)

        if self.email_num == 0:  # 程序初始化
            self.email_num = index
            return
        elif self.email_num < index:  # 接受新邮件
            self.email_num = index
            pass
        elif self.email_num >= index:
            self.email_num = index
            return

        ctrl = []
        # 获取最新一封邮件, 注意索引号从1开始，最后一个索引代表的是最新接收的邮件:
        # 可以写个循环，获取所有邮件的内容 for i in range(1,index+1)
        for i in range(index - 5, index + 1):
            logging.debug(i)
            resp, lines, octets = server.retr(i)
            # logging.debug('===== %s %s %s' % resp, lines, octets)
            # lines存储了邮件的原始文本的每一行,
            # 可以获得整个邮件的原始文本:
            msg_content = b'\r\n'.join(lines).decode('utf-8')
            # 稍后解析出邮件:
            msg = Parser().parsestr(msg_content)
            # 获取邮件内容
            info = self.print_info(msg)
            if 'auto' in info:
                logging.debug("not in list")
                ctrl = info
                continue
            ctrl.clear()
            # 可以根据邮件索引号直接从服务器删除邮件:
            # server.dele(2)
        # 关闭连接:
        server.quit()
        return ctrl

    def send_email(self, info):
        if info is None:
            logging.error('info is NULL')
            return

        # sender是邮件发送人邮箱，passWord是服务器授权码，mail_host是服务器地址（这里是QQsmtp服务器）
        # sender = 'xxxxxxxxxx@qq.com'
        # passWord = 'xxxxxxxxxxxxxxxx'
        mail_host = 'smtp.qq.com'
        # receivers是邮件接收人，用列表保存，可以添加多个
        receivers = ['xxxxxxxxxxxxxx@qq.com']

        # 设置email信息
        msg = MIMEMultipart()
        # 邮件主题
        # msg['Subject'] = input(f"{'请输入邮件主题：'}")
        msg['Subject'] = str("request")
        # 发送方信息
        msg['From'] = self.email
        # 邮件正文是MIMEText:
        # msg_content = input(f"{'请输入邮件主内容:'}")

        msg_content = info
        msg.attach(MIMEText(msg_content, 'plain', 'utf-8'))  # 添加正文

        try:
            # QQsmtp服务器的端口号为465或587
            s = smtplib.SMTP_SSL("smtp.qq.com", 465)
            # s.set_debuglevel(1)
            s.login(self.email, self.password)
            # 给receivers列表中的联系人逐个发送邮件
            for i in range(len(receivers)):
                to = receivers[i]
                msg['To'] = to
                s.sendmail(self.email, to, msg.as_string())
                logging.debug('Success!', end='')
            s.quit()
            logging.debug("All emails have been sent over!", end='')
        except smtplib.SMTPException as e:
            logging.debug("Falied,%s", e)
        # 登录并发送邮件


if __name__ == '__main__':
    A = Auto_ctrl()
    base_url = 'https://www.dgtle.com/'

    while True:
        logging.error('sleep 30 secend')
        ctrl = A.recv_email()
        logging.error(ctrl)
        if not ctrl:
            time.sleep(30)
            continue

        if 'dgtle' in ctrl[3]:
            logging.error(ctrl)

            tmp_index = ctrl[3].split('\r\n')
            for i in range(len(tmp_index)):
                logging.error('tmp %s' % tmp_index[i])
                url = ''
                if 'http' in tmp_index[i]:
                    logging.error('tmp %s' % tmp_index[i])
                    if 'opser.wap.dgtle' in tmp_index[i] or 'm.dgtle' in tmp_index[i]:
                        if 'interestTopicDetails' in tmp_index[i]:
                            logging.error('interestTopicDetails %s ' %
                                          tmp_index[i].split('/')[-1])
                            url = base_url + 'inst-' + \
                                tmp_index[i].split('/')[-1] + '-1.html'
                        elif 'article' in tmp_index[i]:
                            url = base_url + 'article-' + \
                                tmp_index[i].split('/')[-1] + '-1.html'
                    else:
                        logging.error('web %s' % tmp_index[i])
                        url = tmp_index[i]
                    break

            if url:
                path = r'./get_pic' + \
                       str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
                logging.error('url %s' % url)
                be = BeautifulPicture()
                be.mk_dir(path)
                be.get_pic(url)
                A.send_email(tmp_index[0])
            ctrl.clear()
