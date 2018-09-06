from PyQt5 import QtCore, QtGui, QtWidgets

import sys, cv2, time

# from x import Ui_TabWidget

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QFileDialog,QTabWidget 

from PyQt5.QtCore import QTimer, QThread, pyqtSignal, Qt

from PyQt5.QtGui import QPixmap, QImage

from PyQt5.QtWidgets import QLabel,QWidget


class Ui_TabWidget(object):

    def setupUi(self, TabWidget):
        TabWidget.setObjectName("TabWidget") #创建的是"TabWidget"
        TabWidget.resize(789, 619)
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab") #"第一个子窗口"
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(10, 30, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 90, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(110, 30, 461, 311))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(620, 30, 151, 341))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        TabWidget.addTab(self.tab, "")
        self.tab1 = QtWidgets.QWidget() # "第二个子窗口"
        self.tab1.setObjectName("tab1")
        TabWidget.addTab(self.tab1, "")
        self.tab_2 = QtWidgets.QWidget() #"第三个子窗口"
        self.tab_2.setObjectName("tab_2")
        TabWidget.addTab(self.tab_2, "")

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)
        self.pushButton.clicked.connect(TabWidget.imageprocessing) #将按键与事件相连
        self.pushButton_2.clicked.connect(TabWidget.videoprocessing) 
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "TabWidget"))
        self.pushButton.setText(_translate("TabWidget", "打开图片"))
        self.pushButton_2.setText(_translate("TabWidget", "打开视频"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "Tab 1"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab1), _translate("TabWidget", "Tab 2"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_2), _translate("TabWidget", "页"))



class mywindow(QTabWidget,Ui_TabWidget): #这个窗口继承了用QtDesignner 绘制的窗口

    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)

    def videoprocessing(self):
        print("gogo")
        global videoName #在这里设置全局变量以便在线程中使用
        videoName,videoType= QFileDialog.getOpenFileName(self, #返回路径下视频的全名称
                                    "打开视频",
                                    "",
                                    #" *.jpg;;*.png;;*.jpeg;;*.bmp")
                                    " *.mp4;;*.avi;;All Files (*)")
        #cap = cv2.VideoCapture(str(videoName))
        th = Thread(self)
        th.changePixmap.connect(self.setImage)
        th.start()

    def setImage(self, image):
        self.label.setPixmap(QPixmap.fromImage(image))
    def imageprocessing(self):
        print("hehe")
        imgName,imgType= QFileDialog.getOpenFileName(self,
                                    "打开图片",
                                    "",
                                    #" *.jpg;;*.png;;*.jpeg;;*.bmp")
                                    " *.jpg;;*.png;;*.jpeg;;*.bmp;;All Files (*)")

        #利用qlabel显示图片
        print(str(imgName))
        png = QtGui.QPixmap(imgName).scaled(self.label_2.width(), self.label_2.height())#适应设计label时的大小
        self.label_2.setPixmap(png)

class Thread(QThread):#采用线程来播放视频

    changePixmap = pyqtSignal(QtGui.QImage)
    def run(self):
        cap = cv2.VideoCapture(videoName)
        print(videoName)
        while (cap.isOpened()==True):
            ret, frame = cap.read()
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                convertToQtFormat = QtGui.QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)#在这里可以对每帧图像进行处理，
                p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)
                time.sleep(0.01) #控制视频播放的速度
            else:
                break


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())