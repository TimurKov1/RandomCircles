import sys
import random
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.draw.clicked.connect(self.change)
        self.loop = 0

    def change(self):
        self.loop = 1
        self.repaint()

    def paintEvent(self, event):
        if self.loop:
            qp = QPainter()
            qp.begin(self)
            self.create_circle(qp)
            qp.end()
            self.loop = 0

    def create_circle(self, qp):
        qp.setBrush(QColor(random.choice(range(256)), random.choice(range(256)), random.choice(range(256))))
        r = random.choice(range(self.width() // 2 + 1))
        x, y  = random.choice(range(self.width() - r + 1)), random.choice(range(self.height() - r + 1))
        print(x, y, r)
        qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())