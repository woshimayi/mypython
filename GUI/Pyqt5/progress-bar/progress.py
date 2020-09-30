# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import threading

from PyQt5.QtCore import pyqtSlot, QDateTime, QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication
from Ui_progress import Ui_MainWindow
import sys, os
from send_email import send_email

class BackendThread(QThread):
    # 通过类成员对象定义信号
    update_date = pyqtSignal(str)

    # 处理业务逻辑
    def run(self):
        while True:
            data = QDateTime.currentDateTime()
            currTime = data.toString("yyyy-MM-dd hh:mm:ss")
            self.update_date.emit( str(currTime) )
            time.sleep(1)

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
    
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


    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print("doAction")
        # self.pushButton.setText("ssssssss")
        # self.textBrowser.setText("sdasdasdas")
        if self.pushButton.text() == "Start":
            file = r'C:\Users\zs\Pictures\105846277.jpg'
            # th2 = threading.Thread(target=send_email, args=(file, self.send_flag,))
            # th2.start()
        elif self.pushButton.text() == "Finshed":
            self.close()
        # raise NotImplementedError
        # print(self.progressBar.value())
        # self.progressBar.setValue(23)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
    

