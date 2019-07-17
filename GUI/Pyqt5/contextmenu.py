import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, qApp, QMenu

class Example(QMainWindow):
	"""docstring for ExQMainWindow"""
	def __init__(self):
		super().__init__()

		self.initUI()

	def  initUI(self):

		self.setGeometry(300, 300, 400, 200)
		self.setWindowTitle("context menu")
		self.show()

	def  contextMenuEvent(self, event):
		cmenu = QMenu(self)

		newAct = cmenu.addAction('New')
		openAct = cmenu.addAction('open')
		quitAct = cmenu.addAction('Quit')

		action = cmenu.exec_(self.mapToGlobal(event.pos()))

		if action == quitAct:
			qApp.quit()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())