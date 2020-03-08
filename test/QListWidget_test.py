#!/usr/bin/env python
# -*- coding: UTF8 -*-
from PyQt5 import QtCore, QtGui
# import configdialog_rc3

class ConfigDialog(QtGui.QDialog):
	def __init__(self, parent=None):
		super(ConfigDialog, self).__init__(parent)

		self.contentsWidget = QtGui.QListWidget()
		self.contentsWidget.setViewMode(QtGui.QListView.IconMode)
		self.contentsWidget.setIconSize(QtCore.QSize(96, 84))  #Icon 大小
		self.contentsWidget.setMovement(QtGui.QListView.Static)  #Listview显示状态
		self.contentsWidget.setMaximumWidth(800)  # 最大宽度
		self.contentsWidget.setSpacing(12)  # 间距大小
		self.createIcons()
		horizontalLayout = QtGui.QHBoxLayout()
		horizontalLayout.addWidget(self.contentsWidget)
		mainLayout = QtGui.QVBoxLayout()
		mainLayout.addLayout(horizontalLayout)
		self.setLayout(mainLayout)
		self.resize(300,300)

	def createIcons(self):
		configButton = QtGui.QListWidgetItem(self.contentsWidget)
		configButton.setIcon(QtGui.QIcon(':/images/config.png'))
		configButton.setText("Configuration")
		configButton.setTextAlignment(QtCore.Qt.AlignHCenter)
		configButton.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

		updateButton = QtGui.QListWidgetItem(self.contentsWidget)
		updateButton.setIcon(QtGui.QIcon(':/images/update.png'))
		updateButton.setText("Updatessss")
		updateButton.setTextAlignment(QtCore.Qt.AlignHCenter)
		updateButton.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

		queryButton = QtGui.QListWidgetItem(self.contentsWidget)
		queryButton.setIcon(QtGui.QIcon(':/images/query.png'))
		queryButton.setText("Query")
		queryButton.setTextAlignment(QtCore.Qt.AlignHCenter)
		queryButton.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
		self.contentsWidget.currentItemChanged.connect(self.changePage)

	#QListWidget current 改变时触发
	def changePage(self, current, previous):
		print(self.contentsWidget.row(current))


if __name__ == '__main__':
	import sys
	app = QtGui.QApplication(sys.argv)
	dialog = ConfigDialog()
	dialog.show()
	sys.exit(dialog.exec_())