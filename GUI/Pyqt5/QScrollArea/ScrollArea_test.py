import sys
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self,):
        super(QMainWindow, self).__init__()
        self.number = 0

        w = QWidget()
        self.setCentralWidget(w)

        self.topFiller = QWidget()
        self.topFiller.setMinimumSize(1000, 2000)  # 设置滚动条的尺寸

        positions = [(i*60, j*20) for i in range(20) for j in range(10)]

        # 创建一个滚动条
        self.scroll = QScrollArea()
        self.scroll.setWidget(self.topFiller)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.scroll)
        for position in positions:
            self.MapButton = QPushButton(self.topFiller)
            self.MapButton.setText("sss")
            self.MapButton.move(*position)
        w.setLayout(self.vbox)
        self.resize(250, 2000)


        self.desktop = QApplication.desktop()
 
        #获取显示器分辨率大小
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height()
        self.width = self.screenRect.width()
 
        print(self.height)
        print(self.width)


if __name__ == "__main__":
    # app = QApplication(sys.argv)
    # mainwindow = MainWindow()
    # mainwindow.show()
    # sys.exit(app.exec_())

    positions = [(i, j) for i in range(20) for j in range(10)]
    pos = [(i, j) for i in range(20) for j in range(20)]
    for position, po in zip(positions, pos):
        print(position[0], position[1], position)


        
