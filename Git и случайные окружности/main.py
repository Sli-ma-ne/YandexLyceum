import sys

from UI import Ui_MainWindow
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from random import randint


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paint)
        # Обратите внимание: имя элемента такое же как в QTDesigner
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        qp.setPen(QPen(QColor(255, 255, 255), 1))
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        n = randint(50, 100)
        qp.drawEllipse(randint(0, 450), randint(0, 450), n, n)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())