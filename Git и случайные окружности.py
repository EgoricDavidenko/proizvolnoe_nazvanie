import sys
from random import randint

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.do_paint = False

    def initUI(self):
        self.setGeometry(600, 300, 600, 600)
        self.setWindowTitle('Git и случайные окружности')

        self.btn = QPushButton("Создать окружности", self)
        self.btn.resize(150, 30)
        self.btn.move(225, 285)
        self.btn.clicked.connect(self.run)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
            self.do_paint = False

    def draw(self, qp):
        for i in range(10):
            a, b, c = randint(0, 255), randint(0, 255), randint(0, 255)
            qp.setBrush(QColor(a, b, c))
            x = randint(0, 200)
            qp.drawEllipse(randint(0, 800), randint(0, 600), x, x)

    def run(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())