import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QSlider, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class Example(QMainWindow):
	"""docstring for ExQMainWindow"""
	def __init__(self):
		super().__init__()

		self.initUI()

	def  initUI(self):

		sld = QSlider(Qt.Horizontal, self)
		sld.setFocusPolicy(Qt.NoFocus)
		sld.setGeometry(30, 40, 100, 30)
		sld.valueChanged[int].connect(self.changeValue)

		self.label = QLabel(self)
		self.label.setPixmap(QPixmap('0.png'))
		self.label.setGeometry(160, 40, 400, 400)

		self.setGeometry(300, 300, 400, 600)
		self.setWindowTitle("slider")
		self.show()

	def  changeValue(self, value):
		self.setWindowTitle(str(value))
		if value == 0:
			self.label.setPixmap(QPixmap('0.png'))
		elif value > 0  and value <= 30:
			self.label.setPixmap(QPixmap('3.png'))
		elif value > 30 and value < 80:
			self.label.setPixmap(QPixmap('0.png'))
		else:
			self.label.setPixmap(QPixmap('3.png'))

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())