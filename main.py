import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor
from random import randint


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.draw)
        self.flag = False

    def paint_random(self):
        storona = randint(10, 200)
        x = randint(storona, 600 - storona)
        y = randint(storona, 600 - storona)
        self.qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        self.qp.drawEllipse(x - storona // 2, y - storona // 2, storona, storona)

    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        self.paint_random()
        self.qp.end()

    def draw(self):
        self.flag = True
        self.update()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = Example()
    ex.show()
    sys.exit(app.exec())
