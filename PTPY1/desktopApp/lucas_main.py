from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

app = QApplication([])
mainWin = QWidget()

height = QLineEdit()
height.setPlaceholderText("Enter your height")

weight = QLineEdit()
weight.setPlaceholderText("Enter your weight")

main_layout = QVBoxLayout()
main_layout.addWidget(height)
main_layout.addWidget(weight)

mainWin.setLayout(main_layout)
mainWin.show()
app.exec_()