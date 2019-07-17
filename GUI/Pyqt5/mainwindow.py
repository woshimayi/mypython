# http://zetcode.com/gui/pyqt5/menustoolbars/

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QTextEdit, QApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
	"""docstring for ExQMainWindow"""
	def __init__(self):
		super().__init__()

		self.initUI()

	def  initUI(self):

		textEdit = QTextEdit()
		self.setCentralWidget(textEdit)

		exitAct = QAction(QIcon('hello.png'), 'Exit', self)
		exitAct.setShortcut("Ctrl+Q")
		exitAct.setStatusTip('Exit application')

		self.statusBar()

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(exitAct)

		toolbar = self.addToolBar('Exit')
		toolbar.addAction(exitAct)

		self.setGeometry(300, 300, 200, 200)
		self.setWindowTitle("statusBar")
		self.show()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())