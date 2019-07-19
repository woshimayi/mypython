import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QCalendarWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QDate

class Example(QMainWindow):
	"""docstring for ExQMainWindow"""
	def __init__(self):
		super().__init__()

		self.initUI()

	def  initUI(self):
		vbox = QVBoxLayout(self)

		cal = QCalendarWidget(self)
		cal.setGridVisible(True)
		cal.clicked[QDate].connect(self.showDate)

		vbox.addWidget(cal)

		self.lbl = QLabel(self)
		date = cal.selectedDate()
		self.lbl.setText(date.toString())

		vbox.addWidget(self.lbl)

		self.setLayout(vbox)

		self.setGeometry(300, 300, 400, 400)
		self.setWindowTitle("Calendar")
		self.show()

	def showDate(self, date):
		self.lbl.setText(date.toString())

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())