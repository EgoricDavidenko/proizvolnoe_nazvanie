import sys

from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('button.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
            self.do_paint = False

    def draw(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        for i in range(10):
            a = randint(0, 200)
            qp.drawEllipse(randint(0, 800), randint(0, 600), a, a)

    def run(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())