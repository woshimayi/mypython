import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction

class Example(QMainWindow):
	"""docstring for ExQMainWindow"""
	def __init__(self):
		super().__init__()

		self.initUI()

	def  initUI(self):
		self.statusbar = self.statusBar()
		self.statusbar.showMessage('Ready')

		menubar = self.menuBar()
		viewMenu = menubar.addMenu('View')

		viewStatusAct = QAction('View statusbar 1', self, checkable=True)
		viewStatusAct.setStatusTip('View statusbar')
		viewStatusAct.setChecked(False)
		viewStatusAct.triggered.connect(self.toggleMenu)

		viewMenu.addAction(viewStatusAct)

		self.setGeometry(300, 300, 200, 200)
		self.setWindowTitle("check menu")
		self.show()

	def toggleMenu(self, state):
		if state:
			self.statusbar.show()
		else:
			self.statusbar.hide()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())