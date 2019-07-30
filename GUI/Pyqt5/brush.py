import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QBrush
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
		self.drawBrushes(qp)
		qp.end()

	def drawBrushes(self, qp):

		brush = QBrush(Qt.SolidPattern)
		qp.setBrush(brush)
		qp.drawRect(10, 10, 90, 60)

		brush = QBrush(Qt.Dense1Pattern)
		qp.setBrush(brush)
		qp.drawRect(10, 100, 90, 60)

		brush = QBrush(Qt.Dense2Pattern)
		qp.setBrush(brush)
		qp.drawRect(10, 200, 90, 60)

		brush = QBrush(Qt.DiagCrossPattern)
		qp.setBrush(brush)
		qp.drawRect(10, 300, 90, 60)

		brush = QBrush(Qt.Dense5Pattern)
		qp.setBrush(brush)
		qp.drawRect(10, 400, 90, 60)

		brush = QBrush(Qt.Dense6Pattern)
		qp.setBrush(brush)
		qp.drawRect(10, 500, 90, 60)

		brush = QBrush(Qt.HorPattern)
		qp.setBrush(brush)
		qp.drawRect(10, 600, 90, 60)

		brush = QBrush(Qt.VerPattern)
		qp.setBrush(brush)
		qp.drawRect(10, 700, 90, 60)

		brush = QBrush(Qt.BDiagPattern)
		qp.setBrush(brush)
		qp.drawRect(10, 800, 90, 60)





if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())