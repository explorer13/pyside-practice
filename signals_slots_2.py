# Oneshot App
import sys 
from PySide2.QtWidgets import(
    QMainWindow,
    QApplication,
    QPushButton
)
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        button = QPushButton("I dare you to press me!")
        button.clicked.connect(self.one_shot)
        self.setCentralWidget(button)

    def one_shot(self, checked):
        button = self.centralWidget()
        button.setText("Game over!")
        button.setEnabled(False)
        self.setWindowTitle("Oneshot App!")

app = QApplication(sys.argv)

win = MainWindow()
win.show()

app.exec_()