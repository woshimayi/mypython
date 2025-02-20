import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QPushButton, QFrame)
from PyQt5.QtGui import QColor

class Example(QMainWindow):
	"""docstring for ExQMainWindow"""
	def __init__(self):
		super().__init__()

		self.initUI()

	def  initUI(self):
		self.col = QColor(0, 0, 0)
		redb = QPushButton('Red', self)
		redb.setCheckable(True)
		redb.move(10, 10)
		redb.clicked[bool].connect(self.setColor)

		greenb = QPushButton('Green', self)
		greenb.setCheckable(True)
		greenb.move(10, 60)
		greenb.clicked[bool].connect(self.setColor)

		blued = QPushButton('Blue', self)
		blued.setCheckable(True)
		blued.move(10, 100)
		blued.clicked[bool].connect(self.setColor)

		self.square = QFrame(self)
		self.square.setGeometry(150, 20, 100, 100)
		self.square.setStyleSheet("QWidget {background-color: %s}" % self.col.name())

		self.setGeometry(300, 300, 200, 200)
		self.setWindowTitle("toggle button")
		self.show()


	def setColor(self, pressed):
		source = self.sender()

		if pressed:
			val = 255
		else:
			val = 0

		if source.text() == "Red":
			self.col.setRed(val)
		elif source.text() == "Green":
			self.col.setGreen(val)
		else:
			self.col.setBlue(val)

		self.square.setStyleSheet("QFrame {background-color: %s}"  % self.col.name())



if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())