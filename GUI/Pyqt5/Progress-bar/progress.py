# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import threading

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication
from Ui_progress import Ui_MainWindow
import sys, os
from send_email import send_email


send_flag = 0

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
        # file = r'C:\Users\zs\Pictures\105846277.jpg'
        #
        # th2 = threading.Thread(target=send_email, args=(file,))
        # th2.start()
        # raise NotImplementedError
        # self.progressBar.setValue(50)


    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print("doAction")
        # self.pushButton.setText("ssssssss")
        # self.textBrowser.setText("sdasdasdas")
        # file = r'C:\Users\zs\Pictures\105846277.jpg'
        # send_email(file)
        # raise NotImplementedError
        # print(self.progressBar.value())
        # self.progressBar.setValue(23)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
    

