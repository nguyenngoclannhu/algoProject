from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import randint 

app = QApplication([])
main_win = QWidget()
main_layout = QVBoxLayout() 

button = QPushButton("Answer")

ans1 = QRadioButton("The Danube")
ans2 = QRadioButton("The Nile")
ans3 = QRadioButton("The Mekong River")
ans4 = QRadioButton("The Thames")

label = QLabel("What is the longest river?")

row = QHBoxLayout()

col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(ans1)
col1.addWidget(ans3)

col2.addWidget(ans2)
col2.addWidget(ans4)

row.addLayout(col1)
row.addLayout(col2)

main_layout.addWidget(label, alignment= Qt.AlignCenter)
main_layout.addLayout(row)
main_layout.addWidget(button, alignment= Qt.AlignCenter)
main_win.setLayout(main_layout)

def showCorrect():
    if ans1.isChecked():
        win = QMessageBox()
        win.setText("You are correct!")
        win.exec_() 
    else:
        win = QMessageBox()
        win.setText("Sorry! This is not the correct answer.")
        win.exec_() 

button.clicked.connect(showCorrect)

main_win.show()
app.exec_()