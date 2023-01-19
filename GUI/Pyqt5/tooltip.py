import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
from PyQt5.QtGui import QFont

class Example(QWidget):
	"""docstring for Example"""
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		QToolTip.setFont(QFont('SansSerif', 10))
		self.setToolTip('This is a <b>QWidget</b> widget')

		btn = QPushButton('Button', self)
		btn.setToolTip('This is a <b>QPushButton</b> widget')
		btn.resize(btn.sizeHint())
		# btn.resize(20, 20)
		btn.move(50, 50)

		self.setGeometry(2000, 1500, 400, 300)
		self.setWindowTitle('ToolTip')
		self.show()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())