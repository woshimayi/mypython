import sys
from PyQt5.QtWidgets import  QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt
from PyQt5.sip 

class Example(QWidget):
	"""docstring for ExQMainWindow"""
	def __init__(self):
		super().__init__()

		self.initUI()

	def  initUI(self):
		self.text = "sdfsdfsdfsdfsdfdfsdfsdf"

		self.setGeometry(300, 300, 200, 200)
		self.setWindowTitle("statusBar")
		self.show()

	def paintEvent(self, event):
		qp = QPainter()
		qp.begin(self)
		self.drawText(event, qp)
		qp.end()

	def drawText(self, event, qp):
		qp.setPen(QColor(168, 34, 3))
		qp.setFont(QFont('Decoreative', 10))
		qp.drawText(event.rect(), Qt.AlignCenter, self.text)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())