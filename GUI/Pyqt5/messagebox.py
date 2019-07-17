import sys
from  PyQt5.QtWidgets import QWidget, QMessageBox, QApplication

class Example(QWidget):
	"""docstring for Example"""
	def __init__(self):
		super().__init__()

		self.initUI()

	def  initUI(self):
	
		
		self.setGeometry(2000, 1500, 400, 400)
		self.setWindowTitle('MessageBox')
		self.show()
		
	def closeEvent(self, event):
		reply = QMessageBox.question(self, 'Message', "are you sure to quit ?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()



if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())