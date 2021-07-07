import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QApplication,QListWidget,QGridLayout,QLabel
from PyQt5.QtCore import QTimer,QDateTime

class WinForm(QWidget):
    def __init__(self,parent=None):
        super(WinForm, self).__init__(parent)
        #设置标题
        self.setWindowTitle('QTimer demo')

        #实例化一些控件
        self.listFile=QListWidget()
        self.lable=QLabel('显示当前时间')
        self.startBtn=QPushButton('开始')
        self.endBtn=QPushButton('结束')

        #栅格布局
        layout=QGridLayout()

        #初始化一个定时器
        self.timer=QTimer()
        #定时器结束，触发showTime方法
        self.timer.timeout.connect(self.showTime)

        #添加控件到栅格指定位置
        layout.addWidget(self.lable,0,0,1,2)
        layout.addWidget(self.startBtn,1,0)
        layout.addWidget(self.endBtn,1,1)

        #开始结束按钮点击触发相应的槽函数
        self.startBtn.clicked.connect(self.startTimer)
        self.endBtn.clicked.connect(self.endTimer)

        #设置布局方式
        self.setLayout(layout)
    def showTime(self):
        #获取系统当前时间
        time=QDateTime.currentDateTime()
        #设置系统时间的显示格式
        timeDisplay=time.toString('yyyy-MM-dd hh:mm:ss dddd')
        #在标签上显示时间
        self.lable.setText(timeDisplay)
    def startTimer(self):
        #设置时间间隔并启动定时器
        self.timer.start(1000)
        #设置开始按钮不可点击，结束按钮可点击
        self.startBtn.setEnabled(False)
        self.endBtn.setEnabled(True)

    def endTimer(self):
        #停止定时器
        self.timer.stop()
        #结束按钮不可点击，开始按钮可以点击
        self.startBtn.setEnabled(True)
        self.endBtn.setEnabled(False)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    form=WinForm()
    form.show()
    sys.exit(app.exec_())