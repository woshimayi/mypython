# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\zsfile\python27\GUI\Pyqt5\QButton\Button_test.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QLabel
# from PyQt5.QtGui import QPainter, QGradient
# from PyQt5.QtCore import Qt


import os
import sys
import webbrowser

from PyQt5.QtCore import QSize, Qt, QUrl, QTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QFont, QLinearGradient, QGradient, QColor,\
    QBrush, QPaintEvent, QPixmap, QPen
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel,\
    QHBoxLayout, QSpacerItem, QSizePolicy, QScrollArea, QAbstractSlider, QMainWindow

from PyQt5.QtCore import QPoint, QRect, QSize, Qt
from PyQt5.QtWidgets import (QApplication, QLayout, QPushButton, QSizePolicy,
                             QWidget)

from lxml.etree import HTML  # @UnresolvedImport

# 重构label 类


class CoverLabel(QLabel):

    def __init__(self, cover_path, cover_title, video_url, *args, **kwargs):
        super(CoverLabel, self).__init__(*args, **kwargs)
#         super(CoverLabel, self).__init__(
#             '<html><head/><body><img src="{0}"/></body></html>'.format(os.path.abspath(cover_path)), *args, **kwargs)
        self.setCursor(Qt.PointingHandCursor)
        self.setScaledContents(True)
        self.setMinimumSize(220, 308)
        self.setMaximumSize(220, 308)
        self.cover_path = cover_path
        self.cover_title = cover_title
        self.video_url = video_url
        self.setStyleSheet("background-color:grey")
        # self.setPixmap(QPixmap("1.jpg"))

    # def setCoverPath(self, path):
    #     self.cover_path = path
    #
    # def mouseReleaseEvent(self, event):
    #     super(CoverLabel, self).mouseReleaseEvent(event)
    #     webbrowser.open_new_tab(self.video_url)

    def paintEvent(self, event):
        # super().paintEvent(event)
        # painter = QPainter(self)
        # painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        # painter.drawText(20, 20, "sss")

        super(CoverLabel, self).paintEvent(event)
        if hasattr(self, "cover_title") and self.cover_title != "":
            # 底部绘制文字
            painter = QPainter(self)
            rect = self.rect()
            rect.bottom()
            # 粗略字体高度
            painter.save()
            fheight = self.fontMetrics().height()
            # 底部矩形框背景渐变颜色
            bottomRectColor = QLinearGradient(
                rect.width() / 2, rect.height() - 24 - fheight,
                rect.width() / 2, rect.height())
            bottomRectColor.setSpread(QGradient.PadSpread)
            bottomRectColor.setColorAt(0, QColor(255, 255, 255, 70))
            bottomRectColor.setColorAt(1, QColor(0, 0, 0, 50))
            # 画半透明渐变矩形框
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(bottomRectColor))
            painter.drawRect(rect.x(), rect.height() - 24 -
                             fheight, rect.width(), 24 + fheight)
            painter.restore()
            # 距离底部一定高度画文字
            font = self.font() or QFont()
            font.setPointSize(16)
            painter.setFont(font)
            painter.setPen(Qt.white)
            rect.setHeight(rect.height() - 12)  # 底部减去一定高度
            painter.drawText(rect, Qt.AlignHCenter |
                                 Qt.AlignBottom, "asas")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)

        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        # 图片label
        self.clabel = CoverLabel(
            '1.jpg',
            "aaaaa",
            "http://www.baidu.com",
            self.centralWidget)

        # painter = QPainter(self.clabel)
        # painter.begin(self.clabel)
        # # 自定义绘制方法
        # painter.setPen(QColor(168, 34, 3))
        # # 设置字体
        # painter.setFont(QFont('SimSun', 20))
        # # 绘制文字
        # painter.drawText(20, 20, "sssss")
        # painter.end()




if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
