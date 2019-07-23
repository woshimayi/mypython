import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QLabel, QLineEdit)

class Example(QMainWindow):
	"""docstring for ExQMainWindow"""
	def __init__(self):
		super().__init__()

		self.initUI()

	def  initUI(self):
		self.lbl = QLabel(self)
		# self.lbl.move(60, 80)

		qle = QLineEdit(self)
		qle.move(60, 100)
		qle.textChanged[str].connect(self.onChanged)

		self.setGeometry(300, 300, 200, 200)
		self.setWindowTitle("QLineEdit")
		self.show()

	def onChanged(self, text):
		self.lbl.setText(text)
		self.lbl.adjustSize()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())