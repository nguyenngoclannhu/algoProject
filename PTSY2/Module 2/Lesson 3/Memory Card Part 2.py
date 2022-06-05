from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication([])

btn_OK = QPushButton('Answer') # answer button
question = QLabel('Which is the highest mountain in the world?')

#create radio button for the answer
btn_ans1 = QRadioButton('Answer 1')
btn_ans2 = QRadioButton('Answer 2')
btn_ans3 = QRadioButton('Answer 3')
btn_ans4 = QRadioButton('Answer 4')

layout_verticle = QVBoxLayout()
layout_questions = QHBoxLayout() #question
Hlayout2 = QHBoxLayout() #answer 1,2
Hlayout3 = QHBoxLayout() #answer 3,4
layout_answers = QHBoxLayout() #answer box
layout_answers_btn = QHBoxLayout() #answer button

#Answer group box
RadioGroupBox = QGroupBox('Answer options')
layout_group = QVBoxLayout()

#add all the widget onto the vertical layout
#(align center)
layout_questions.addWidget(question, alignment = Qt.AlignCenter)

Hlayout2.addWidget(btn_ans1, alignment = Qt.AlignCenter)
Hlayout2.addWidget(btn_ans2, alignment = Qt.AlignCenter)

Hlayout3.addWidget(btn_ans3, alignment = Qt.AlignCenter)
Hlayout3.addWidget(btn_ans4, alignment = Qt.AlignCenter)

#Result group box
lb_Result = QLabel('are you correct or not?') 
lb_Correct = QLabel('the answer will be here!')

AnsGroupBox = QGroupBox("Test result")
layout_res = QVBoxLayout()

layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)

AnsGroupBox.setLayout(layout_res)

#add layout to main layout
layout_group.addLayout(Hlayout2)
layout_group.addLayout(Hlayout3)
RadioGroupBox.setLayout(layout_group)

layout_answers.addWidget(RadioGroupBox)
layout_answers.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_answers_btn.addWidget(btn_OK)


#create vertical box layout
layout_verticle = QVBoxLayout()
layout_verticle.addLayout(layout_questions)
layout_verticle.addLayout(layout_answers)
layout_verticle.addLayout(layout_answers_btn)

def show_result():
    ''' show answer panel '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Next question')
 
def show_question():
    ''' show question pan el '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Answer')
    RadioGroup.setExclusive(False) # remove limits in order to reset radio button selection
    btn_ans1.setChecked(False)
    btn_ans2.setChecked(False)
    btn_ans3.setChecked(False)
    btn_ans4.setChecked(False)
    RadioGroup.setExclusive(True) # bring back the limits so only one radio button can be selected 
 
#PART 2
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
 
def ask(question, right_answer, wrong1, wrong2, wrong3):
    ''' the function writes the value of the question and answers into the corresponding widgets while distributing the answer options randomly'''
    shuffle(answers)
    answers[0].setText(right_answer)
    answers[1].setText(wrong1)
    answers[2].setText(wrong2)
    answers[3].setText(wrong3)
    lb_Question.setText(question)
    lb_Correct.setText(right_answer) 
    show_question() 
 
def show_correct(res):
    ''' show result - put the written text into "result" and show the corresponding panel '''
    lb_Result.setText(res)
    show_result()
 
def check_answer():
    ''' if an answer option was selected, check and show answer panel '''
    if answers[0].isChecked():
        show_correct('Correct!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Incorrect!')

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
ask('The national language of Brazil', 'Portuguese', 'Brazilian', 'Spanish', 'Italian')
btn_OK.clicked.connect(check_answer) 
 
window.show()
app.exec()








































