import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QComboBox, QLabel

class Example(QMainWindow):
	"""docstring for ExQMainWindow"""
	def __init__(self):
		super().__init__()

		self.initUI()

	def  initUI(self):

		self.lbl = QLabel("ubuntu" ,self)

		combo = QComboBox(self)
		combo.addItem("Ubuntu")
		combo.addItem("Mandrive")
		combo.addItem("Fedora")
		combo.addItem("Arch")
		combo.addItem("Gentoo")

		combo.move(50, 50)
		self.lbl.move(50, 150)

		combo.activated[str].connect(self.onActivated)

		self.setGeometry(300, 300, 200, 200)
		self.setWindowTitle("statusBar")
		self.show()

	def onActivated(self, text):
		self.lbl.setText(text)
		self.lbl.adjustSize()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())