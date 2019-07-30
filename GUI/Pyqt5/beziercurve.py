import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPainterPath
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
		qp.setRenderHint(QPainter.Antialiasing)
		self.drawBezierCurve(qp)
		qp.end()

	def drawBezierCurve(self, qp):
		path = QPainterPath()
		path.moveTo(30, 30)
		path.cubicTo(0, 30, 100, 200, 600, 30)
		qp.drawPath(path)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())