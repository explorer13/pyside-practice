# First App!
from PySide2.QtWidgets import QApplication, QWidget
import sys

# Exactly one instance of QApplication is needed per app
app = QApplication(sys.argv)

# Create a widget
win = QWidget()
# Show the widget (by default widgets are invisible)
win.show()

# Start vent loop
app.exec_()