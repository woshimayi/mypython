import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt

class Example(QWidget):
	"""docstring for ExQMainWindow"""
	def __init__(self):
		super().__init__()

		self.initUI()
		self.desktop = QApplication.desktop()
		self.screeenRect = self.desktop.screenGeometry()
		self.height = self.screeenRect.height()
		self.width = self.screeenRect.width()

	def  initUI(self):
		self.setWindowTitle("statusBar")
		self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint)     # 无边框 置顶
		self.window().setAttribute(Qt.WA_TranslucentBackground)                 # 透明背景色
		self.showFullScreen()

	def paintEvent(self, e):
		qp = QPainter()
		qp.begin(self)
		self.drawLines(qp)
		qp.end()

	def drawLines(self, qp):
		pen = QPen(Qt.black, 20, Qt.SolidLine)
		qp.setPen(QPen(QColor(3, 255, 255), 3))

		print(self.width, self.height)

		# qp.drawLine(self.width/2-50, self.height/2, self.width/2+50, self.height/2)
		qp.drawLine(self.width/2-50, self.height/2, self.width/2-10, self.height/2)
		qp.drawLine(self.width/2+10, self.height/2, self.width/2+50, self.height/2)

		qp.drawLine(self.width/2, self.height/2+10, self.width/2, self.height/2+50)

		qp.setPen(QPen(QColor(255, 0, 0), 2))
		qp.drawLine(self.width / 2, self.height / 2, self.width / 2, self.height / 2)

		# pen.setStyle(Qt.DashLine)
		# qp.setPen(pen)
		# qp.drawLine(20, 80, 250, 80)

		# pen.setStyle(Qt.DashDotLine)
		# qp.setPen(pen)
		# qp.drawLine(20, 100, 250, 100)

		# pen.setStyle(Qt.DotLine)
		# qp.setPen(pen)
		# qp.drawLine(20, 120, 250, 120)

		# pen.setStyle(Qt.DashDotDotLine)
		# qp.setPen(pen)
		# qp.drawLine(20, 140, 250, 140)

		# pen.setStyle(Qt.CustomDashLine)
		# pen.setDashPattern([1, 4, 5, 4])
		# qp.setPen(pen)
		# qp.drawLine(20, 240, 250, 240)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())