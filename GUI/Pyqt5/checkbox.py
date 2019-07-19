import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QCheckBox
from PyQt5.QtCore import Qt



class Example(QMainWindow):
	"""docstring for ExQMainWindow"""
	def __init__(self):
		super().__init__()

		self.initUI()

	def  initUI(self):
		cb = QCheckBox('Show title', self)
		cb.move(20 , 20)
		cb.toggle()
		cb.stateChanged.connect(self.changeTitle)

		self.setGeometry(300, 300, 200, 200)
		self.setWindowTitle("statusBar")
		self.show()

	def changeTitle(self, state):
		if state == Qt.Checked:
			self.setWindowTitle('QCheckBox')
		else:
			self.setWindowTitle(' ')

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())