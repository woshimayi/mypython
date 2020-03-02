import sys
try:
from PySide import QtGui, QtCore
except ImportError:
from PyQt4 import QtGui, QtCore

app = QtGui.QApplication(sys.argv)
img = QtGui.QImage(400, 300, QtGui.QImage.Format_ARGB32)
img.fill(0)
img.save("test.png")
#sys.exit(app.exec_())