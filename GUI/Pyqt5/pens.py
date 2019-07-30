import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt

class Example(QWidget):
	"""docstring for ExQMainWindow"""
	def __init__(self):
		super().__init__()

		self.initUI()

	def  initUI(self):

		self.setGeometry(300, 300, 200, 200)
		self.setWindowTitle("statusBar")
		self.show()

	def paintEvent(self, e):
		qp = QPainter()
		qp.begin(self)
		self.drawLines(qp)
		qp.end()

	def drawLines(self, qp):
		pen = QPen(Qt.black, 2, Qt.SolidLine)

		qp.setPen(pen)
		qp.drawLine(20, 40, 250, 40)

		pen.setStyle(Qt.DashLine)
		qp.setPen(pen)
		qp.drawLine(20, 80, 250, 80)

		pen.setStyle(Qt.DashDotLine)
		qp.setPen(pen)
		qp.drawLine(20, 100, 250, 100)

		pen.setStyle(Qt.DotLine)
		qp.setPen(pen)
		qp.drawLine(20, 120, 250, 120)

		pen.setStyle(Qt.DashDotDotLine)
		qp.setPen(pen)
		qp.drawLine(20, 140, 250, 140)

		pen.setStyle(Qt.CustomDashLine)
		pen.setDashPattern([1, 4, 5, 4])
		qp.setPen(pen)
		qp.drawLine(20, 240, 250, 240)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())