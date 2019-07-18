import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFrame, QColorDialog, QApplication
from PyQt5.QtGui import QColor

class Example(QMainWindow):
	"""docstring for ExQMainWindow"""
	def __init__(self):
		super().__init__()

		self.initUI()

	def  initUI(self):
		col  = QColor(0, 0, 0)

		self.btn = QPushButton('Gialog', self)
		self.btn.move(20, 20)
		self.btn.clicked.connect(self.showDialog)

		self.frm = QFrame(self)
		self.frm.setStyleSheet("QWidget{background-color: %s}" % col.name())
		self.frm.setGeometry(130, 22, 100, 100)

		self.setGeometry(300, 300, 200, 200)
		self.setWindowTitle("statusBar")
		self.show()

	def  showDialog(self):
		col = QColorDialog.getColor()
		if col.isValid():
			self.frm.setStyleSheet("QWidget {background-color: %s}" % col.name())


if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())