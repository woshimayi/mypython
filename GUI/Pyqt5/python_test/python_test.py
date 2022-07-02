# -*- coding: utf-8 -*-

"""
Module implementing widget_exec.
"""
import json
import os
import sys
import telnetlib
import threading
import time

import requests
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QTextCursor, QBrush, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QCheckBox, QTableWidgetItem

from Ui_python_test import Ui_Form


# import xlutils.copy


class widget_exec(QWidget, Ui_Form):
    """
        Class documentation goes here.
        """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(widget_exec, self).__init__(parent)
        self.setupUi(self)
        self.tn = ''
        self.factorycfg = ''
        self.factorycfg_dict_save = {}
        self.factorycfg_dict_confirm = {}
        self.hard_test = {}

        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36",
            'authorization': ""
        }
        self.get_regionUrl = 'http://192.168.1.1/hgsreadme'

        self.addTableWidget(2)
        self.radioButton_2.setChecked(True)

        self.smt = True
        th1 = threading.Thread(target=self.get_region())
        th2 = threading.Thread(target=self.telnet_enable())

        th1.start()
        th2.start()

        th1.join(5)  ##20秒超时时间
        th2.join(5)  ##20秒超时时间


    def __del__(self):
        if self.tn:
            self.tn.close()

    def json_format(self, data):
        print(json.dumps(data, sort_keys="true", indent=4, separators=(",", ":")))

    def get_region(self):
        print("get region")
        try:
            r = requests.get(self.get_regionUrl, headers=self.headers, timeout=20)
            r.encoding = 'utf-8'
            # soup = BeautifulSoup(r.text, "lxml")
            # soup.prettify()
            if r.status_code == 200:
                # print(r.text)
                self.json_format(r.json())
                j = r.json()
                print(j['Region'])
                self.label_svn.setText(j['SvnRevision'])
                self.label_region.setText(j['Region'])
                self.smt = 'SMT' in j['Region']
                return self.smt
        except Exception as e:
            print(e)

    def open_file(self):
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(),
                                                                   "All Files(*);;Text Files(*.w)")
        print(fileName)
        print(fileType)

    def telnet_enable(self):
        try:
            url = 'http://192.168.1.1/setObjs'
            enableTelnet = {"TelnetEnable": True, "TelnetWANEnable": False, "TelnetUserName": "CMCCAdmin",
                            "TelnetPassword": "aDm8H%MdA",
                            "fullPath": "InternetGatewayDevice.DeviceInfo.X_CMCC_ServiceManage."}
            data = []
            data.append(enableTelnet)

            print("\t\tpost", url, data)
            r = requests.post(url, json=data, headers=self.headers, timeout=20)
            r.encoding = 'utf-8'
            if r.status_code == 200:
                print('\t\t', r.text)
                self.json_format(r.json())
                print(r.status_code)
        except:
            print("error ")

    def getdeviceinfo(self):
        self.to_telnet(['cat /etc/svn_info'])

    def device_info_compare(self):
        print("zzzzz compare save   ", self.factorycfg_dict_save)
        print("zzzzz compare cpmform", self.factorycfg_dict_confirm)
        print(self.factorycfg_dict_confirm == self.factorycfg_dict_save)
        flag = self.factorycfg_dict_confirm == self.factorycfg_dict_save

        row = 0
        for key in self.factorycfg_dict_save.keys():
            if self.factorycfg_dict_save[key] == self.factorycfg_dict_confirm[key]:
                self.tableWidget.item(row, 3).setText('yes')
                self.tableWidget.item(row, 3).setBackground(QBrush(QColor(0, 255, 0)))
            else:
                self.tableWidget.item(row, 3).setText('no')
                self.tableWidget.item(row, 3).setBackground(QBrush(QColor(255, 0, 0)))
            row += 1

            if flag == False:
                break


    def str2dict(self, str):
        dict = {}
        for data in str.splitlines():
            if '=' in data:
                dict[data.split('=')[0]] = data.split('=')[1]
        return dict


    def do_telnet(self, Host, username, password, finish, commands):
        '''Telnet远程登录：Windows客户端连接Linux服务器'''

        # 连接Telnet服务器
        if self.tn:
            print("success", self.tn, self.tn.get_socket())
        else:
            try:
                self.tn = telnetlib.Telnet(Host, port=23, timeout=10)
                # 输入登录用户名
                self.tn.read_until('Login: '.encode())
                self.tn.write(username.encode() + b'\n')
                # 输入登录密码
                self.tn.read_until('Password: '.encode())
                self.tn.write(password.encode() + b'\n')
                self.tn.read_until(finish.encode())

                if finish == '>':
                    self.tn.write('sh'.encode() + b'\n')
                    time.sleep(0.3)
                    self.tn.read_very_eager().decode('ascii')
            except Exception as e:
                print("error fail open telnet")
                self.textEdit.append("连接失败" % Host)
                # return
            print('error', (self.tn))

        # 登录完毕后执行命令
        self.tn.set_debuglevel(0)
        for command in commands:
            try:
                # print('cmd', command)
                # i += 1
                if 0 == len(command):
                    continue
                self.tn.write(b'%s\n' % command.encode())
                time.sleep(0.3)
                str = ''
                str1 = ''

                if self.radioButton_1.isChecked():
                    print('radio 1', command)
                    # self.tableWidget.item()
                    while True:
                        b, c, d = self.tn.expect([b"# "], timeout=20)
                        # print(b, c, d)
                        str += d.decode()

                        if b == 0:
                            # print('there are more data')
                            pass
                        else:
                            # print('break')
                            break
                    print('str zzzzz', str.splitlines())
                    self.hard_test[command] = str.splitlines()[1:]

                else:
                    # str = self.tn.expect([b"#"], 10)[2].decode('ascii')
                    str = self.tn.read_very_eager().decode('ascii')

                    str1 = '%s' % (str)
                    print('str1', str1)
                    self.hard_test[command] = str1

                    self.textEdit.append(str1)
                    self.textEdit.moveCursor(QTextCursor.End)

                    if command == 'factorycfg get':
                        self.factorycfg = str1
                        self.factorycfg_dict_confirm = self.str2dict(self.factorycfg)
                        self.label_region.setText(self.factorycfg_dict_confirm['region'])
                    elif 'svn_info' in command:
                        print('svn', str1.splitlines(), str1.splitlines()[1].strip('# '))
                        self.label_svn.setText(str1.splitlines()[1].strip('# '))
            except Exception as e:
                print(e)
                self.textEdit.append("连接失败" % e)
                self.tn.close()



    def to_telnet(self, commands):
        Host = '192.168.1.1'  # Telnet服务器IP


        if self.get_region():
            username = 'telnetadmin'  # 登录用户名
            password = 'telnetadmin'  # 登录密码
            finish = '#'
        else:
            username = 'CMCCAdmin'  # 登录用户名
            password = 'aDm8H%MdA'  # 登录密码
            finish = '>'

        try:
            th1 = threading.Thread(target=self.do_telnet, args=(Host, username, password, finish, commands))
            th1.start()
            th1.join(5)  ##20秒超时时间
        except Exception as e:
            print("aaa", e)


    def addTableWidget(self, item):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(['选择', '项目', '参数', 'ok'])
        row = self.tableWidget.rowCount()
        print("addwidget", row)

        if item == 1:
            projects = {'启动检测': '',
                        '网口口测试': '',
                        'USB接口测试': 'ls /mnt/disk1_1',
                        'RESET按键测试': 'factorytest resetbutton start',
                        'WPS按键测试': 'factorytest wpsbutton start',
                        '无线按键测试': 'factorytest wifibutton start',
                        '摘挂机及拨号检测': 'voice hookdialtest 0 start',
                        '振铃测试': 'voice ringtest 0 start; sleep 10; voice ringtest 0 stop',
                        'LED测试开始': 'factorytest led start',
                        'LED测试停止': 'factorytest led stop'}
        elif item == 2:
            projects = {'svn': 'cat /etc/svn_info', 'lcinfo': 'lcinfo', 'factorycfg':'factorycfg get'}
        elif item == 3:
            print('add widget', self.factorycfg_dict_save)
            projects = self.factorycfg_dict_confirm
        elif 4 == item:
            print('add widget', "upgrade")
            projects = {'image 1': 'ssssssssssssss', 'image 2': 'sssssssssssss'}

        for pro in projects.keys():
            self.add_line(pro, projects[pro], 0)

    def add_line(self, project, arg, ok):
        row = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(row + 1)

        ##下面六行用于生成居中的checkbox，不知道有没有别的好方法
        ck = QCheckBox()
        ck.setChecked(True)
        # h = QHBoxLayout()
        # h.setAlignment(Qt.AlignCenter)
        # h.addWidget(ck)
        # w = QWidget()
        # w.setLayout(h)

        self.tableWidget.setCellWidget(row, 0, ck)
        self.tableWidget.setItem(row, 1, QTableWidgetItem(project))
        self.tableWidget.setItem(row, 2, QTableWidgetItem(arg))
        self.tableWidget.setItem(row, 3, QTableWidgetItem(ok))

    def cycle_deviceinfo(self, commands):
        print("zzzzz cycle", commands)
        while True:
            try:
                print("aaaaa cycle")
                self.to_telnet(commands)
                time.sleep(1)
                self.to_telnet(['factorycfg get'])
                self.device_info_compare()
                print('cycle', self.checkBox.isChecked())
                if self.checkBox.isChecked() == False:
                    print("tread exit")
                    break
                time.sleep(3)
            except Exception as e:
                print(e)
                break

    def cycle_exec(self, commands):
        print("zzzzz cycle", commands)
        while True:
            self.to_telnet(commands)
            if self.checkBox.isChecked() == False:
                print("tread exit")
                break
            time.sleep(0.5)


    def cycle_hard(self, commands):
        print("zzzzz cycle 1", commands)
        while True:
            self.to_telnet(commands)
            if self.checkBox.isChecked() == False:
                print("tread exit")
                break
            time.sleep(3)
        print(self.hard_test)


    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print("button click")
        # self.textEdit.append("button click")

        print('zzzz', self.tableWidget.item(0, 1).text())

        print(self.tableWidget.rowCount())
        row = self.tableWidget.rowCount()

        commands = []
        facCmd = ''
        for i in range(row):
            if self.radioButton_3.isChecked():
                facCmd += ' ' + self.tableWidget.item(i, 1).text() + '=' + '"' + self.tableWidget.item(i, 2).text() + '"'
                self.factorycfg_dict_save[self.tableWidget.item(i, 1).text()] = self.tableWidget.item(i, 2).text()
            else:
                commands.append(self.tableWidget.item(i, 2).text())

        print(commands)

        if self.radioButton_1.isChecked():
            self.to_telnet(commands)

        elif self.radioButton_2.isChecked():
            th1 = threading.Thread(target=self.cycle_exec, args=(commands,))
            th1.start()
            th1.join(5)  ##20秒超时时间

        elif self.radioButton_3.isChecked():
            facCmd = 'factorycfg set ' + facCmd
            commands.append(facCmd)
            print(facCmd)
            th2 = threading.Thread(target=self.cycle_deviceinfo, args=(commands,))
            th2.start()
            th2.join(5)  ##20秒超时时间

        elif self.radioButton_upgrade.isChecked():
            print("radio 4", commands)




    @pyqtSlot()
    def on_lineEdit_returnPressed(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print("line edit enter pressd", self.lineEdit.text())
        # self.textEdit.append(self.lineEdit.text())
        command = []
        command.append(self.lineEdit.text())
        self.to_telnet(command)


    @pyqtSlot()
    def on_radioButton_1_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print("radio")
        self.addTableWidget(1)

    @pyqtSlot()
    def on_radioButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print("radio 2")
        self.addTableWidget(2)

    @pyqtSlot()
    def on_radioButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print("radio 3")
        self.to_telnet(['factorycfg get'])
        self.addTableWidget(3)

    @pyqtSlot()
    def on_pushButton_save_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print("button save")

    @pyqtSlot()
    def on_pushButton_get_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print("button add table view")
        # projects = {}
        self.add_line("dd", "ss", 0)
        # self.to_telnet()

        # print(self.factorycfg)
        # for data in self.factorycfg.splitlines():
        #     self.factorycfg_dict[data.split('=')[0]] = data.split('=')[1]

        # print('zzzzz', self.factorycfg_dict)
    
    @pyqtSlot()
    def on_radioButton_upgrade_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.addTableWidget(4)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = widget_exec()
    ui.show()
    sys.exit(app.exec_())
