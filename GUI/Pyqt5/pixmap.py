from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication)
from PyQt5.QtGui import QPixmap
import sys

class Example(QWidget):
	"""docstring for ExQMainWindow"""
	def __init__(self):
		super().__init__()

		self.initUI()

	def  initUI(self):
		hbox = QHBoxLayout(self)
		
		pixmap = QPixmap("0.png")

		lbl = QLabel(self)
		lbl.setPixmap(pixmap)

		hbox.addWidget(lbl)
		self.setLayout(hbox)

		self.move(200, 200)
		self.setWindowTitle("red Rock")
		self.show()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())