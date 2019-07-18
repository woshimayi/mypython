import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QMainWindow, QApplication, QLCDNumber, QSlider, QVBoxLayout

class Example(QMainWindow):
	"""docstring for ExQMainWindow"""
	def __init__(self):
		super().__init__()

		self.initUI()

	def  initUI(self):

		lcd  = QLCDNumber(self)
		sld = QSlider(Qt.Horizontal, self)

		vbox = QVBoxLayout()
		vbox.addWidget(lcd)
		vbox.addWidget(sld)
		self.setLayout(vbox)

		sld.valueChanged.connect(lcd.display)

		self.setGeometry(300, 300, 200, 200)
		self.setWindowTitle("Signal and slot")
		self.show()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = Example()
	print(Example().__doc__)
	sys.exit(app.exec_())