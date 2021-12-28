from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QWidget
import sys


def View():
    

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('MPTAG')
window.setGeometry(0, 0, 250, 100)
window.move(200, 200)

hello_label = QLabel('<h1>Hello World!</h1>', parent=window)
hello_label.move(60, 30)

window.show()

sys.exit(app.exec())