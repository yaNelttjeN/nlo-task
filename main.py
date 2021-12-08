import sys
import traceback
import random

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window_size = (250, 250)
        self.setFixedSize(self.window_size[0], self.window_size[1])

        self._size = (32, 32)
        self._pos = [0, 0]
        self.change = 16

        self.label = QLabel(self)
        self.label.resize(self._size[0], self._size[1])
        self.pixmap = QPixmap('nlo.png')
        self.pixmap = self.pixmap.scaled(self._size[0],  self._size[1])
        self.label.setPixmap(self.pixmap)

    def update_pos(self):
        self.label.move(self._pos[0], self._pos[1])

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            self._pos[0] -= self.change
        if event.key() == Qt.Key_Right:
            self._pos[0] += self.change
        if event.key() == Qt.Key_Up:
            self._pos[1] -= self.change
        if event.key() == Qt.Key_Down:
            self._pos[1] += self.change
        self.check_border()
        self.update_pos()

    def check_border(self):
        if self._pos[0] + self._size[0] > self.window_size[0]:
            self._pos[0] = 0
        if self._pos[0] < 0:
            self._pos[0] = self.window_size[0] - self._size[0]
        if self._pos[1] + self._size[1] > self.window_size[1]:
            self._pos[1] = 0
        if self._pos[1] < 0:
            self._pos[1] = self.window_size[1] - self._size[1]


def excepthook(exc_type, exc_value, exc_tb):
    tb = ''.join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print(tb)


sys.excepthook = excepthook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec())
