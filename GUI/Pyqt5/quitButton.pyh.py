import sys
from  PyQt5.QtWidgets import QWidget, QPushButton, QApplication

class Example(QWidget):
    """docstring for Example"""
    def __init__(self):
        super().__init__()

        self.initUI()

    def  initUI(self):

        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QApplication.instance().quit)

        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)
        self.setGeometry(2000, 1800, 200, 200)
        self.setWindowTitle('Quit button')
        self.show()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())