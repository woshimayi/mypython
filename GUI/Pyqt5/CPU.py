
import sys, os

def path():
    pathSelected = dirModel.filePath(r"C:\Users\zs\Pictures")
    print('pathSelected   ', pathSelected)
        # 遍历路径下的媒体文件
    for item in os.listdir(pathSelected):
        if item.split('.')[-1] in FILE_TYPE:
            print(item)
            # 添加widget
            # try:
            #     widget = ImageWidget()
            #     widget.displayText = item
            #     widget.setThumb(str(pathSelected + '/' + item))
            #     self.imageContainer.addWidget(widget)
            # except:
            #     print(u'出错了')
            #     pass
            #     
            #     autopep8 --in-place --aggressive --aggressive

path()

# ==============================================================================================================================

'''
from PyQt5 import QtWidgets,QtCore,QtGui
import pyqtgraph as pg
import sys
import traceback
import psutil

class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CPU使用率监控 - 州的先生http://zmister.com")
        self.main_widget = QtWidgets.QWidget()  # 创建一个主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建一个网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置主部件的布局为网格
        self.setCentralWidget(self.main_widget)  # 设置窗口默认部件

        self.plot_widget = QtWidgets.QWidget()  # 实例化一个widget部件作为K线图部件
        self.plot_layout = QtWidgets.QGridLayout()  # 实例化一个网格布局层
        self.plot_widget.setLayout(self.plot_layout)  # 设置K线图部件的布局层
        self.plot_plt = pg.PlotWidget()  # 实例化一个绘图部件
        self.plot_plt.showGrid(x=True,y=True) # 显示图形网格
        self.plot_layout.addWidget(self.plot_plt)  # 添加绘图部件到K线图部件的网格布局层
        # 将上述部件添加到布局层中
        self.main_layout.addWidget(self.plot_widget, 1, 0, 3, 3)

        self.setCentralWidget(self.main_widget)
        self.plot_plt.setYRange(max=100,min=0)
        self.data_list = []
        self.timer_start()

    # 启动定时器 时间间隔秒
    def timer_start(self):
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.get_cpu_info)
        self.timer.start(1000)

    # 获取CPU使用率
    def get_cpu_info(self):
        try:
            cpu = "%0.2f" % psutil.cpu_percent(interval=1)
            self.data_list.append(float(cpu))
            print(float(cpu))
            self.plot_plt.plot().setData(self.data_list,pen='g')
        except Exception as e:
            print(traceback.print_exc())

def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
'''
# =========================================================================================================
# 
# 

'''
from PyQt5.QtCore import pyqtSlot, QIODevice, QByteArray
from PyQt5.QtSerialPort import QSerialPortInfo, QSerialPort
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
# from Lib.UiSerialPort import Ui_FormSerialPort  # @UnresolvedImport


class Ui_FormSerialPort(object):
    def setupUi(self, FormSerialPort):
        FormSerialPort.setObjectName("FormSerialPort")
        FormSerialPort.resize(721, 597)
        FormSerialPort.setStyleSheet("#labelStatus {\n"
                                    "    border-radius: 13px;\n"
                                    "    background-color: gray;\n"
                                    "}\n"
                                    "#labelStatus[isOn=\"true\"] {\n"
                                    "    background-color: green;\n"
                                    "}")
        self.gridLayout = QtWidgets.QGridLayout(FormSerialPort)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(FormSerialPort)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.comboBoxPort = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxPort.setObjectName("comboBoxPort")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBoxPort)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.comboBoxBaud = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxBaud.setObjectName("comboBoxBaud")
        self.comboBoxBaud.addItem("")
        self.comboBoxBaud.addItem("")
        self.comboBoxBaud.addItem("")
        self.comboBoxBaud.addItem("")
        self.comboBoxBaud.addItem("")
        self.comboBoxBaud.addItem("")
        self.comboBoxBaud.addItem("")
        self.comboBoxBaud.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBoxBaud)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.comboBoxParity = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxParity.setObjectName("comboBoxParity")
        self.comboBoxParity.addItem("")
        self.comboBoxParity.addItem("")
        self.comboBoxParity.addItem("")
        self.comboBoxParity.addItem("")
        self.comboBoxParity.addItem("")
        self.comboBoxParity.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBoxParity)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.comboBoxData = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxData.setObjectName("comboBoxData")
        self.comboBoxData.addItem("")
        self.comboBoxData.addItem("")
        self.comboBoxData.addItem("")
        self.comboBoxData.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBoxData)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.comboBoxStop = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxStop.setObjectName("comboBoxStop")
        self.comboBoxStop.addItem("")
        self.comboBoxStop.addItem("")
        self.comboBoxStop.addItem("")
        self.comboBoxStop.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comboBoxStop)
        self.buttonConnect = QtWidgets.QPushButton(self.groupBox)
        self.buttonConnect.setObjectName("buttonConnect")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.buttonConnect)
        self.labelStatus = QtWidgets.QLabel(self.groupBox)
        self.labelStatus.setProperty("isOn", False)
        self.labelStatus.setObjectName("labelStatus")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.labelStatus)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(6, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(FormSerialPort)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 1, 2, 1)
        self.widget = QtWidgets.QWidget(FormSerialPort)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.checkBoxHexView = QtWidgets.QCheckBox(self.widget)
        self.checkBoxHexView.setObjectName("checkBoxHexView")
        self.verticalLayout.addWidget(self.checkBoxHexView)
        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(FormSerialPort)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.buttonSend = QtWidgets.QPushButton(self.widget_2)
        self.buttonSend.setObjectName("buttonSend")
        self.verticalLayout_2.addWidget(self.buttonSend)
        self.checkBoxHexSend = QtWidgets.QCheckBox(self.widget_2)
        self.checkBoxHexSend.setObjectName("checkBoxHexSend")
        self.verticalLayout_2.addWidget(self.checkBoxHexSend)
        self.gridLayout.addWidget(self.widget_2, 2, 0, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(FormSerialPort)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 2, 1, 1, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setRowStretch(0, 3)

        self.retranslateUi(FormSerialPort)
        self.comboBoxBaud.setCurrentIndex(3)
        self.comboBoxData.setCurrentIndex(3)
        self.pushButton_2.clicked.connect(self.textBrowser.clear)
        QtCore.QMetaObject.connectSlotsByName(FormSerialPort)

    def retranslateUi(self, FormSerialPort):
        _translate = QtCore.QCoreApplication.translate
        FormSerialPort.setWindowTitle(_translate("FormSerialPort", "串口调试小助手"))
        self.label.setText(_translate("FormSerialPort", "端  口"))
        self.label_2.setText(_translate("FormSerialPort", "波特率"))
        self.comboBoxBaud.setItemText(0, _translate("FormSerialPort", "1200"))
        self.comboBoxBaud.setItemText(1, _translate("FormSerialPort", "2400"))
        self.comboBoxBaud.setItemText(2, _translate("FormSerialPort", "4800"))
        self.comboBoxBaud.setItemText(3, _translate("FormSerialPort", "9600"))
        self.comboBoxBaud.setItemText(4, _translate("FormSerialPort", "19200"))
        self.comboBoxBaud.setItemText(5, _translate("FormSerialPort", "38400"))
        self.comboBoxBaud.setItemText(6, _translate("FormSerialPort", "57600"))
        self.comboBoxBaud.setItemText(7, _translate("FormSerialPort", "115200"))
        self.label_3.setText(_translate("FormSerialPort", "校验位"))
        self.comboBoxParity.setItemText(0, _translate("FormSerialPort", "No"))
        self.comboBoxParity.setItemText(1, _translate("FormSerialPort", "Even"))
        self.comboBoxParity.setItemText(2, _translate("FormSerialPort", "Odd"))
        self.comboBoxParity.setItemText(3, _translate("FormSerialPort", "Space"))
        self.comboBoxParity.setItemText(4, _translate("FormSerialPort", "Mark"))
        self.comboBoxParity.setItemText(5, _translate("FormSerialPort", "Unknown"))
        self.label_4.setText(_translate("FormSerialPort", "数据位"))
        self.comboBoxData.setItemText(0, _translate("FormSerialPort", "5"))
        self.comboBoxData.setItemText(1, _translate("FormSerialPort", "6"))
        self.comboBoxData.setItemText(2, _translate("FormSerialPort", "7"))
        self.comboBoxData.setItemText(3, _translate("FormSerialPort", "8"))
        self.label_5.setText(_translate("FormSerialPort", "停止位"))
        self.comboBoxStop.setItemText(0, _translate("FormSerialPort", "OneStop"))
        self.comboBoxStop.setItemText(1, _translate("FormSerialPort", "OneAndHalfStop"))
        self.comboBoxStop.setItemText(2, _translate("FormSerialPort", "TwoStop"))
        self.comboBoxStop.setItemText(3, _translate("FormSerialPort", "UnknownStopBits"))
        self.buttonConnect.setText(_translate("FormSerialPort", "打开串口"))
        self.labelStatus.setText(_translate("FormSerialPort", "      "))
        self.pushButton_2.setText(_translate("FormSerialPort", "清空接收区"))
        self.checkBoxHexView.setText(_translate("FormSerialPort", "十六进制显示"))
        self.buttonSend.setText(_translate("FormSerialPort", "手动发送"))
        self.checkBoxHexSend.setText(_translate("FormSerialPort", "十六进制发送"))

class Window(QWidget, Ui_FormSerialPort):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self._serial = QSerialPort(self)  # 用于连接串口的对象
        self._serial.readyRead.connect(self.onReadyRead)  # 绑定数据读取信号
        # 首先获取可用的串口列表
        self.getAvailablePorts()

    @pyqtSlot()
    def on_buttonConnect_clicked(self):
        # 打开或关闭串口按钮
        if self._serial.isOpen():
            # 如果串口是打开状态则关闭
            self._serial.close()
            self.textBrowser.append('串口已关闭')
            self.buttonConnect.setText('打开串口')
            self.labelStatus.setProperty('isOn', False)
            self.labelStatus.style().polish(self.labelStatus)  # 刷新样式
            return

        # 根据配置连接串口
        name = self.comboBoxPort.currentText()
        if not name:
            QMessageBox.critical(self, '错误', '没有选择串口')
            return
        port = self._ports[name]
#         self._serial.setPort(port)
        # 根据名字设置串口（也可以用上面的函数）
        self._serial.setPortName(port.systemLocation())
        # 设置波特率
        self._serial.setBaudRate(  # 动态获取,类似QSerialPort::Baud9600这样的吧
            getattr(QSerialPort, 'Baud' + self.comboBoxBaud.currentText()))
        # 设置校验位
        self._serial.setParity(  # QSerialPort::NoParity
            getattr(QSerialPort, self.comboBoxParity.currentText() + 'Parity'))
        # 设置数据位
        self._serial.setDataBits(  # QSerialPort::Data8
            getattr(QSerialPort, 'Data' + self.comboBoxData.currentText()))
        # 设置停止位
        self._serial.setStopBits(  # QSerialPort::Data8
            getattr(QSerialPort, self.comboBoxStop.currentText()))

        # NoFlowControl          没有流程控制
        # HardwareControl        硬件流程控制(RTS/CTS)
        # SoftwareControl        软件流程控制(XON/XOFF)
        # UnknownFlowControl     未知控制
        self._serial.setFlowControl(QSerialPort.NoFlowControl)
        # 读写方式打开串口
        ok = self._serial.open(QIODevice.ReadWrite)
        if ok:
            self.textBrowser.append('打开串口成功')
            self.buttonConnect.setText('关闭串口')
            self.labelStatus.setProperty('isOn', True)
            self.labelStatus.style().polish(self.labelStatus)  # 刷新样式
        else:
            self.textBrowser.append('打开串口失败')
            self.buttonConnect.setText('打开串口')
            self.labelStatus.setProperty('isOn', False)
            self.labelStatus.style().polish(self.labelStatus)  # 刷新样式

    @pyqtSlot()
    def on_buttonSend_clicked(self):
        # 发送消息按钮
        if not self._serial.isOpen():
            print('串口未连接')
            return
        text = self.plainTextEdit.toPlainText()
        if not text:
            return
        text = QByteArray(text.encode('gb2312'))  # emmm windows 测试的工具貌似是这个编码
        if self.checkBoxHexSend.isChecked():
            # 如果勾选了hex发送
            text = text.toHex()
        # 发送数据
        print('发送数据:', text)
        self._serial.write(text)

    def onReadyRead(self):
        # 数据接收响应
        if self._serial.bytesAvailable():
            # 当数据可读取时
            # 这里只是简答测试少量数据,如果数据量太多了此处readAll其实并没有读完
            # 需要自行设置粘包协议
            data = self._serial.readAll()
            if self.checkBoxHexView.isChecked():
                # 如果勾选了hex显示
                data = data.toHex()
            data = data.data()
            # 解码显示（中文啥的）
            try:
                self.textBrowser.append('我收到了: ' + data.decode('gb2312'))
            except:
                # 解码失败
                self.textBrowser.append('我收到了: ' + repr(data))

    def getAvailablePorts(self):
        # 获取可用的串口
        self._ports = {}  # 用于保存串口的信息
        infos = QSerialPortInfo.availablePorts()
        infos.reverse()  # 逆序
        for info in infos:
            # 通过串口名字-->关联串口变量
            self._ports[info.portName()] = info
            self.comboBoxPort.addItem(info.portName())

    def closeEvent(self, event):
        if self._serial.isOpen():
            self._serial.close()
        super(Window, self).closeEvent(event)


if __name__ == '__main__':
    import sys
    import cgitb
    sys.excepthook = cgitb.enable(1, None, 5, '')
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())

'''
# =========================================================================================================
#
'''
import webbrowser

from PyQt5.QtCore import Qt, QPropertyAnimation, QPoint, QTimer, pyqtSignal
from PyQt5.QtWidgets import QWidget, QPushButton

# from Lib.UiNotify import Ui_NotifyForm  # @UnresolvedImport

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NotifyForm(object):
    def setupUi(self, NotifyForm):
        NotifyForm.setObjectName("NotifyForm")
        NotifyForm.resize(300, 200)
        NotifyForm.setStyleSheet("QWidget#widgetTitle {\n"
"    background-color: rgb(76, 169, 106);\n"
"}\n"
"QWidget#widgetBottom {\n"
"    border-top-style: solid;\n"
"    border-top-width: 2px;\n"
"    border-top-color: rgb(185, 218, 201);\n"
"}\n"
"QLabel#labelTitle {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QLabel#labelContent {\n"
"    padding: 5px;\n"
"}\n"
"QPushButton {\n"
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"QPushButton#buttonClose {\n"
"    font-family: \"webdings\";\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#buttonClose:hover {\n"
"    background-color: rgb(212, 64, 39);\n"
"}\n"
"QPushButton#buttonView {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"    border: solid 1px rgb(76, 169, 106);\n"
"    background-color: rgb(76, 169, 106);\n"
"}\n"
"QPushButton#buttonView:hover {\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(NotifyForm)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widgetTitle = QtWidgets.QWidget(NotifyForm)
        self.widgetTitle.setMinimumSize(QtCore.QSize(0, 26))
        self.widgetTitle.setObjectName("widgetTitle")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widgetTitle)
        self.horizontalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelTitle = QtWidgets.QLabel(self.widgetTitle)
        self.labelTitle.setText("")
        self.labelTitle.setObjectName("labelTitle")
        self.horizontalLayout_3.addWidget(self.labelTitle)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.buttonClose = QtWidgets.QPushButton(self.widgetTitle)
        self.buttonClose.setMinimumSize(QtCore.QSize(26, 26))
        self.buttonClose.setMaximumSize(QtCore.QSize(26, 26))
        self.buttonClose.setObjectName("buttonClose")
        self.horizontalLayout_3.addWidget(self.buttonClose)
        self.verticalLayout.addWidget(self.widgetTitle)
        self.labelContent = QtWidgets.QLabel(NotifyForm)
        self.labelContent.setText("")
        self.labelContent.setWordWrap(True)
        self.labelContent.setObjectName("labelContent")
        self.verticalLayout.addWidget(self.labelContent)
        self.widgetBottom = QtWidgets.QWidget(NotifyForm)
        self.widgetBottom.setObjectName("widgetBottom")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widgetBottom)
        self.horizontalLayout.setContentsMargins(0, 5, 5, 5)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(170, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.buttonView = QtWidgets.QPushButton(self.widgetBottom)
        self.buttonView.setMinimumSize(QtCore.QSize(75, 25))
        self.buttonView.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonView.setObjectName("buttonView")
        self.horizontalLayout.addWidget(self.buttonView)
        self.verticalLayout.addWidget(self.widgetBottom)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(NotifyForm)
        QtCore.QMetaObject.connectSlotsByName(NotifyForm)

    def retranslateUi(self, NotifyForm):
        _translate = QtCore.QCoreApplication.translate
        NotifyForm.setWindowTitle(_translate("NotifyForm", "消息提示"))
        self.buttonClose.setText(_translate("NotifyForm", "r"))
        self.buttonView.setText(_translate("NotifyForm", "查 看"))



class WindowNotify(QWidget, Ui_NotifyForm):

    SignalClosed = pyqtSignal()  # 弹窗关闭信号

    def __init__(self, title="", content="", timeout=5000, *args, **kwargs):
        super(WindowNotify, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setTitle(title).setContent(content)
        self._timeout = timeout
        self._init()

    def setTitle(self, title):
        if title:
            self.labelTitle.setText(title)
        return self

    def title(self):
        return self.labelTitle.text()

    def setContent(self, content):
        if content:
            self.labelContent.setText(content)
        return self

    def content(self):
        return self.labelContent.text()

    def setTimeout(self, timeout):
        if isinstance(timeout, int):
            self._timeout = timeout
        return self

    def timeout(self):
        return self._timeout

    def onView(self):
        print("onView")
        webbrowser.open_new_tab("http://alyl.vip")

    def onClose(self):
        #点击关闭按钮时
        print("onClose")
        self.isShow = False
        QTimer.singleShot(100, self.closeAnimation)#启动弹回动画

    def _init(self):
        # 隐藏任务栏|去掉边框|顶层显示
        self.setWindowFlags(Qt.Tool | Qt.X11BypassWindowManagerHint |
                            Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        # 关闭按钮事件
        self.buttonClose.clicked.connect(self.onClose)
        # 点击查看按钮
        self.buttonView.clicked.connect(self.onView)
        # 是否在显示标志
        self.isShow = True
        # 超时
        self._timeouted = False
        # 桌面
        self._desktop = QApplication.instance().desktop()
        # 窗口初始开始位置
        self._startPos = QPoint(
            self._desktop.screenGeometry().width() - self.width() - 5,
            self._desktop.screenGeometry().height()
        )
        # 窗口弹出结束位置
        self._endPos = QPoint(
            self._desktop.screenGeometry().width() - self.width() - 5,
            self._desktop.availableGeometry().height() - self.height() - 5
        )
        # 初始化位置到右下角
        self.move(self._startPos)

        # 动画
        self.animation = QPropertyAnimation(self, b"pos")
        self.animation.finished.connect(self.onAnimationEnd)
        self.animation.setDuration(1000)  # 1s

        # 弹回定时器
        self._timer = QTimer(self, timeout=self.closeAnimation)

    def show(self, title="", content="", timeout=5000):
        self._timer.stop()  # 停止定时器,防止第二个弹出窗弹出时之前的定时器出问题
        self.hide()  # 先隐藏
        self.move(self._startPos)  # 初始化位置到右下角
        super(WindowNotify, self).show()
        self.setTitle(title).setContent(content).setTimeout(timeout)
        return self

    def showAnimation(self):
        print("showAnimation isShow = True")
        # 显示动画
        self.isShow = True
        self.animation.stop()#先停止之前的动画,重新开始
        self.animation.setStartValue(self.pos())
        self.animation.setEndValue(self._endPos)
        self.animation.start()
        # 弹出5秒后,如果没有焦点则弹回去
        self._timer.start(self._timeout)
#         QTimer.singleShot(self._timeout, self.closeAnimation)

    def closeAnimation(self):
        print("closeAnimation hasFocus", self.hasFocus())
        # 关闭动画
        if self.hasFocus():
            # 如果弹出后倒计时5秒后还有焦点存在则失去焦点后需要主动触发关闭
            self._timeouted = True
            return  # 如果有焦点则不关闭
        self.isShow = False
        self.animation.stop()
        self.animation.setStartValue(self.pos())
        self.animation.setEndValue(self._startPos)
        self.animation.start()

    def onAnimationEnd(self):
        # 动画结束
        print("onAnimationEnd isShow", self.isShow)
        if not self.isShow:
            print("onAnimationEnd close()")
            self.close()
            print("onAnimationEnd stop timer")
            self._timer.stop()
            print("onAnimationEnd close and emit signal")
            self.SignalClosed.emit()

    def enterEvent(self, event):
        super(WindowNotify, self).enterEvent(event)
        # 设置焦点(好像没啥用,不过鼠标点击一下后,该方法就有用了)
        print("enterEvent setFocus Qt.MouseFocusReason")
        self.setFocus(Qt.MouseFocusReason)

    def leaveEvent(self, event):
        super(WindowNotify, self).leaveEvent(event)
        # 取消焦点
        print("leaveEvent clearFocus")
        self.clearFocus()
        if self._timeouted:
            QTimer.singleShot(1000, self.closeAnimation)

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication, QHBoxLayout
    app = QApplication(sys.argv)

    window = QWidget()
    notify = WindowNotify(parent=window)

    layout = QHBoxLayout(window)

    b1 = QPushButton(
        "弹窗1", window, clicked=lambda: notify.show(content=b1.text()).showAnimation())
    b2 = QPushButton(
        "弹窗2", window, clicked=lambda: notify.show(content=b2.text()).showAnimation())

    layout.addWidget(b1)
    layout.addWidget(b2)

    window.show()
    sys.exit(app.exec_())
'''
# =========================================================================================================