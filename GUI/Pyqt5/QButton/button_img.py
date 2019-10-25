import sys
from PyQt5.QtWidgets import QApplication,QWidget, QLabel
from PyQt5.QtGui import QPainter,QColor,QFont
from PyQt5.QtCore import Qt

class Drawing(QWidget):
    def __init__(self,parent=None):
        super(Drawing, self).__init__(parent)
        self.setWindowTitle('在窗口绘制文字')
        self.resize(300,200)
        self.text='欢迎学习 PyQt5'

    def paintEvent(self,event):

        self.label = QLabel(self)

        painter=QPainter(self.label)
        painter.begin(self.label)
        #自定义绘制方法
        painter.setPen(QColor(168,34,3))
        #设置字体
        painter.setFont(QFont('SimSun',20))
        #绘制文字
        # painter.drawText(event.rect(),Qt.AlignCenter,self.text)
        painter.drawText(20, 20,"sssss")    
        painter.end()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Drawing()
    demo.show()
    sys.exit(app.exec_())