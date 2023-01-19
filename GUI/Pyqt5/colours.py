import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QBrush

class Example(QWidget):
	"""docstring for ExQMainWindow"""
	def __init__(self):
		super().__init__()

		self.initUI()

	def  initUI(self):

		self.setGeometry(400, 400, 600, 400)
		self.setWindowTitle("colours")
		self.show()

	def paintEvent(self, e):
		qp = QPainter()
		qp.begin(self)
		self.drawRectangles(qp)
		qp.end()

	def drawRectangles(self, qp):
		col = QColor(0, 0, 0)
		col.setNamedColor('#d4d4d4')
		qp.setPen(col)

		qp.setBrush(QColor(200, 0, 0, 255))
		qp.drawRect(10, 15, 90, 60)

		qp.setBrush(QColor(0, 255, 0))
		qp.drawRect(130, 15, 90, 60)

		qp.setBrush(QColor(0, 0, 255, 255)) # param R G B  颜色深度
		qp.drawRect(250, 15, 90, 60)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())