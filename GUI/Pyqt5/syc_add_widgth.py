# -*- coding: utf-8 -*-
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import  QApplication, QDialog, QPushButton, QGridLayout, QLabel
import sys
'''
Pyqt 动态的添加控件
'''


# class DynAddObject(QDialog):
#     def __init__(self, parent=None):
#         super(DynAddObject, self).__init__(parent)
#         addButton = QPushButton(u"添加控件")
#         self.layout = QGridLayout()
#         self.layout.addWidget(addButton, 1, 0)
#         self.setLayout(self.layout)
#         self.add()
 
#     def add(self):
#         self.button={}
#         print(type(self.button))
#         for i in range(1, 8):
#             self.button[i]=QPushButton(str(i))
#             self.layout.addWidget(self.button[i])
 


class DynAddObject(QDialog):
    def __init__(self, parent=None):
        super(DynAddObject, self).__init__(parent)

        addButton = QPushButton(u"添加控件")

        self.layout = QGridLayout()
        self.layout.addWidget(addButton, 0, 5)
        self.setLayout(self.layout)

        addButton.clicked.connect(self.add_label)

    def add(self):
        btncont= self.layout.count()
        widget = QPushButton(str(btncont), self)
        self.layout.addWidget(widget)

    def add_label(self):
        count = self.layout.count()
        widget = QLabel(str(count)+".jpg",  self)
        <self class="layout addWidget">
            <widget></widget>
        </self>
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = DynAddObject()
    form.show()
    app.exec_()