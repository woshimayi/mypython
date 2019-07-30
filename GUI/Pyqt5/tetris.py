import  sys, random
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal



class Tetris(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        '''initiates application UI'''

        self.tboard = Board(self)
        self.setCentralWidget(self.tboard)

        self.statusbar = self.statusBar()
        self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)

        self.tboard.start()

        self.resize(180, 380)
        self.center()
        self.setWindowTitle("tetris")
        self.show()

    def center(self):
        '''center the window on the screen'''

        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(screen.width()-size.width()/2, (screen.height()-size.height()/2))




class Board(QFrame):
    msg2Statusbar = pyqtSignal(str)

    BoardWidth = 10
    BoardHeight = 22
    Speed = 300

    def __init__(self, parent):
        super().__init__(parent)
        self.initBoard()

    def initBoard(self):
        '''initiates board'''

        self.timer = QBasicTimer()
        self.isWaitingAfterLine = False

        self.curX = 0
        self.curY = 0
        self.numLinesRemoved = 0
        self.board = []

    def shapwAt(self, x, y):
        '''determines shape at the board position'''
        return self.board[(y * Board.BoardWidth) + x]

    def setShapeAt(self, x, y, shape):
        '''set a shape at the board'''
        self.board[(y * BoardWidth) + x] = shape

    def squareWidth