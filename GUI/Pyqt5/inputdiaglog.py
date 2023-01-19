import sys
from PyQt5.QtWidgets import QMainWindow,  QApplication, QLineEdit, QInputDialog, QPushButton

class Example(QMainWindow):
	"""docstring for ExQMainWindow"""
	def __init__(self):
		super().__init__()

		self.initUI()

	def  initUI(self):

		self.btn = QPushButton('Gialog', self)
		self.btn.move(20, 20)
		self.btn.clicked.connect(self.showDialog)

		self.le = QLineEdit(self)
		self.le.move(130, 20)

		self.setGeometry(300, 300, 200, 200)
		self.setWindowTitle("statusBar")
		self.show()

	def showDialog(self):
		text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter youe name:')
		if ok:
			self.le.setText(str(text))

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())