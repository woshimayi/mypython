import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, QAction

class Example(QMainWindow):
	"""docstring for ExQMainWindow"""
	def __init__(self):
		super().__init__()

		self.initUI()

	def  initUI(self):
		menubar = self.menuBar()

		fileMenu = menubar.addMenu('File')
		newAct = QAction('New', self)

		impMenu = QMenu('Import', self)
		impAct = QAction('Import mail', self)
		impMenu.addAction(impAct)

		fileMenu.addAction(newAct)
		fileMenu.addMenu(impMenu)

		self.setGeometry(300, 300, 200, 200)
		self.setWindowTitle("Submenu")
		self.show()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())