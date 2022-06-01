# -*- coding: utf-8 -*-
'''
@author: woshimayi
@license: (C) Copyright 2015-2049, Node Supply Chain Manager Corporation Limited.
@contact: 2638288078@qq.com
@software: garner
@file: progress.py
@time: 2020/9/30
@desc: pyqt5 send email progress
'''

import threading
import time
from PyQt5.QtCore import pyqtSlot, QDateTime, QThread, pyqtSignal, QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from Ui_progress import Ui_MainWindow

import sys
import smtplib
import threading
from email import encoders

from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

from winsound import Beep

from email_RW import Email_operate


class BackendThread(QThread):
    # 通过类成员对象定义信号
    update_date = pyqtSignal(int)

    """docstring for ClassName"""

    def __init__(self, filename):
        super(BackendThread, self).__init__()
        self.file = filename

        self.C = Email_operate('email.ini')

        # sender是邮件发送人邮箱，passWord是服务器授权码，mail_host是服务器地址（这里是QQsmtp服务器）
        print("zzzzzzzz", self.C.read_sendMail(), self.C.read_sendPass(), self.C.read_sendUser())
        self.C.show()
        self.sender = self.C.read_sendMail()
        self.passWord = self.C.read_sendPass()
        self.mail_host = self.C.read_sendUser()
        # receivers是邮件接收人，用列表保存，可以添加多个
        self.receivers = []
        # self.receivers.append(self.C.read_sendMail())
        print('self.receivers', self.C.read_recvMail().split())

    # 处理业务逻辑
    def run(self):
        # 发送文件名
        file_name = self.file.split('\\')[-1]

        self.update_date.emit(1)

        # 设置email信息
        msg = MIMEMultipart()
        # 邮件主题
        # msg['Subject'] = input(f"{'请输入邮件主题：'}")
        msg['Subject'] = str(
            time.strftime(
                "%Y%m%d%H%M%S",
                time.localtime())) + ': ' + file_name
        # 发送方信息
        msg['From'] = self.sender
        # 邮件正文是MIMEText:
        # msg_content = input(f"{'请输入邮件主内容:'}")
        self.update_date.emit(2)

        msg_content = filename
        if msg_content == 'auto.json':
            with open('auto.json', 'r') as f:
                json_str = f.read()
            msg.attach(MIMEText(json_str, 'plain', 'utf-8'))
        else:
            # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
            with open(self.file, 'rb') as f:
                # 设置附件的MIME和文件名，这里是jpg类型,可以换png或其他类型:
                mime = MIMEBase('image', 'jpg', filename=file_name)
                # 加上必要的头信息:
                mime.add_header(
                    'Content-Disposition',
                    'attachment',
                    filename=filename)
                mime.add_header('Content-ID', '<0>')
                mime.add_header('X-Attachment-Id', '0')
                # 把附件的内容读进来:
                mime.set_payload(f.read())
                # 用Base64编码:
                encoders.encode_base64(mime)
                # 添加到MIMEMultipart:
                msg.attach(mime)
        self.update_date.emit(3)

        try:
            # QQsmtp服务器的端口号为465或587
            s = smtplib.SMTP_SSL("smtp.qq.com", 465)
            # s.set_debuglevel(1)
            s.login(self.sender, self.passWord)
            self.update_date.emit(4)
            if msg_content.split('.')[-1] in ['txt',
                                              'html', 'pdf', 'epub', 'mobi', 'azw3']:
                flag = True
            else:
                flag = False

            if flag:
                # 给receivers列表中的联系人逐个发送邮件
                for i in range(len(self.receivers)):
                    to = self.receivers[i]
                    msg['To'] = to
                    s.sendmail(self.sender, to, msg.as_string())
                    print('Success!', end='')
            else:
                s.sendmail(self.sender, self.receivers[0], msg.as_string())
                self.update_date.emit(5)
                print('Success!', end='')
            s.quit()
        except smtplib.SMTPException as e:
            print("Falied,%s", e)
            self.update_date.emit(6)
        # 登录并发送邮件


class MainWindow(QDialog, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, filename, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        Beep(400, 100)
        self.filename = filename
        self.timeThread = BackendThread(self.filename)
        self.timeThread.update_date.connect(self.chang_time)
        self.timeThread.start()

    @pyqtSlot(str)
    def on_progressBar_objectNameChanged(self, objectName):
        """
        Slot documentation goes here.

        @param objectName DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSlot(str)
    def on_progressBar_windowIconTextChanged(self, iconText):
        """
        Slot documentation goes here.

        @param iconText DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSlot(int)
    def on_progressBar_valueChanged(self, value):
        """
        Slot documentation goes here.

        @param value DESCRIPTION
        @type int
        """
        # TODO: not implemented yet

    def chang_time(self, value):
        self.progressBar.setValue(value * 20)
        if value <= 4:
            self.label.setText("sending")
        elif value == 5:
            self.label.setText("send success")
            QTimer.singleShot(1000, app.quit)
            Beep(500, 300)
            # self.close()
        # else:
        #     self.label.setText("send fail")
        #     time.sleep(2)
        #     self.close()


if __name__ == "__main__":
    if 2 != len(sys.argv):
        print("get file fail")
        sys.exit()

    print(sys.argv[1])
    print(sys.argv)
    filename = sys.argv[1]
    # filename = r'./progress.e4p'

    app = QApplication(sys.argv)
    ui = MainWindow(filename)
    ui.show()
    sys.exit(app.exec_())
