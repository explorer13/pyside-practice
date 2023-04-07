from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nonesense!")
        self.setFixedSize(300,400)
        button = QPushButton("Do not press me!")
        self.setCentralWidget(button)

app = QApplication(sys.argv)

win = MainWindow()
win.show()

app.exec_()