import sys, random
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter
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
		self.drawPoints(qp)
		qp.end()

	def drawPoints(self, qp):
		qp.setPen(Qt.red)
		size = self.size()

		for i in range(100000):
			x = random.randint(1, size.width() - 1)
			y = random.randint(1, size.height() - 1)
			qp.drawPoint(x, y)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())