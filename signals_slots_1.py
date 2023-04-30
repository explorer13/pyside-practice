# simple experiment with signals, and slots
import sys

from PySide2.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() # call the constructor of parent
        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        self.setCentralWidget(self.button)
        self.button.clicked.connect(self.button_clicked)
    
    def button_clicked(self, checked):
        print("Checked? ", checked)

app = QApplication(sys.argv)

win = MainWindow()
win.show()

app.exec_()

