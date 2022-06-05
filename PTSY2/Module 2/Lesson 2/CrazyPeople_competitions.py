from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QMessageBox, QRadioButton

 #1. create an application
app = QApplication([])
 
 #2. create main window
main_win = QWidget()
 #set window title
main_win.setWindowTitle("Competition from Crazy People")

 #create question label
question = QLabel("--Enter your question in here--")

btn_ans1 = QRadioButton("Answer 1")
btn_ans2 = QRadioButton("Answer 2")
btn_ans3 = QRadioButton("Answer 3")
btn_ans4 = QRadioButton("Answer 4")

#add a vertical layout and 3 horizontal layout
layout_verticle = QVBoxLayout()
#create 3 horizontal guidelines
Hlayout1 = QHBoxLayout()
Hlayout2 = QHBoxLayout()
Hlayout3 = QHBoxLayout()

#add all the widget onto the vertical layout
#(align center)
Hlayout1.addWidget(question, alignment = Qt.AlignCenter)

Hlayout2.addWidget(btn_ans1, alignment = Qt.AlignCenter)
Hlayout2.addWidget(btn_ans2, alignment = Qt.AlignCenter)

Hlayout3.addWidget(btn_ans3, alignment = Qt.AlignCenter)
Hlayout3.addWidget(btn_ans4, alignment = Qt.AlignCenter)

#add horizontal layout onto the vertical layout
layout_verticle.addLayout(Hlayout1)
layout_verticle.addLayout(Hlayout2)
layout_verticle.addLayout(Hlayout3)

#set layout for the main window
main_win.setLayout(layout_verticle)

#add 'show_win()' and 'show_lose()'
def show_win():
    win = QMessageBox()
    win.setText('Correct answer! You win a prize!')
    win.exec_()
def show_lose():
    lose = QMessageBox()
    lose.setText('Incorrect answer!')
    lose.exec_()
    
#ans 1 is correct
btn_ans1.clicked.connect(show_win)
#connect others ans to show_lose
btn_ans2.clicked.connect(show_lose)
btn_ans3.clicked.connect(show_lose)
btn_ans4.clicked.connect(show_lose)
 #show the main window
main_win.show()
 #execute the application
app.exec_()




 