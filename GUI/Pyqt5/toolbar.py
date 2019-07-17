import sys
from PyQt5.QtWidgets import qApp, QMainWindow, QApplication, QAction
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
	"""docstring for ExQMainWindow"""
	def __init__(self):
		super().__init__()

		self.initUI()

	def  initUI(self):

		exitAct = QAction(QIcon('hello.png'), 'Exit', self)
		exitAct.setShortcut('Ctrl+Q')
		exitAct.triggered.connect(qApp.quit)

		self.toolbar = self.addToolBar('Exit')
		self.toolbar.addAction(exitAct)

		self.setGeometry(300, 300, 200, 200)
		self.setWindowTitle("ToolBar")
		self.show()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())