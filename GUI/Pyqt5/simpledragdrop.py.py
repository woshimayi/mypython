import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QWidget

class Button(QPushButton):
	"""docstring for Button"""
	def __init__(self, title, parent):
		super().__init__(title, parent)

		self.setAcceptDrops(True)

	def dragEnterEvent(self, e):
		if e.mimeData().hasFormat('text/plain'):
			e.accept()
		else:
			e.ignore()

	def dropEvent(self, e):
		self.setText(e.mimeData().text())


class Example(QWidget):
	"""docstring for ExQMainWindow"""
	def __init__(self):
		super().__init__()

		self.initUI()

	def  initUI(self):

		edit = QLineEdit("", self)
		edit.setDragEnabled(True)
		edit.move(30, 65)

		button = Button("Button", self)
		button.move(190, 50)

		self.setGeometry(500, 500, 200, 200)
		self.setWindowTitle("Simple drag and drop")
		self.show()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())