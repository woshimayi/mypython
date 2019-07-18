import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit, QAction, QFileDialog
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
	"""docstring for ExQMainWindow"""
	def __init__(self):
		super().__init__()

		self.initUI()

	def  initUI(self):
		self.textEdit = QTextEdit()
		self.setCentralWidget(self.textEdit)
		self.statusBar()

		openFile = QAction(QIcon('hello.png'), 'Open', self)
		openFile.setShortcut('Ctrl+O')
		openFile.setStatusTip('Open new File')
		openFile.triggered.connect(self.showDialog)

		menubar = self.menuBar()

		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(openFile)

		self.setGeometry(300, 300, 200, 200)
		self.setWindowTitle("statusBar")
		self.show()

	def showDialog(self):
		fname = QFileDialog.getOpenFileName(self, 'Open file', 'E:\\')

		if fname[0]:
			f= open(fname[0], 'r')

			with f:
				data = f.read()
				self.textEdit.setText(data)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())