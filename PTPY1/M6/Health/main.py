from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # checking types of input values
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, QGridLayout, 
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)

win_width, win_height = 800, 300
win_width2, win_height2 = 1200, 600
win_width3, win_height3 = 500, 200
win_x, win_y = 200, 200

txt_hello = 'Welcome to the health assessment program!'
txt_next = 'Start'
txt_instruction = ('This application will help you conduct a primary health diagnostic test using the Ruffier index.\n'
                    'The Ruffier index is a test to measure\n'
                    'aerobic endurance. The subject lies on their back for 5 minutes and then\n'
                    ' they measure their resting heart rate over 15 seconds; then the subject performs 30 squats in 45 seconds.\n'
                    'At the end of the exercise, the subject lies down, and measures their heart rate over the first\n'
                    '15 seconds, and then over the last 15 seconds of the first minute of the recovery period.\n'
                    'Important! If during the test you feel unwell (dizziness, ringing in\n'
                    'your ears, severe shortness of breath, etc.), the test should be stopped and you should consult a doctor.' )
txt_title = 'Health'
txt_name = 'Please enter your full name.:'
txt_hintname = "Full name"
txt_hintage = "0"
txt_test1 = 'Lie on your back and measure your heart rate over 15 seconds. Click the "Start first test" button to start the timer. \nEnter the result in the appropriate field.'
txt_test2 = 'Do 30 squats in 45 seconds. When you start, click the button "Start doing squats",\nto start the squat counter.'
txt_test3 = 'Lie on your back and measure your heart rate first over the first 15 seconds of the minute, then over the last 15 seconds.\nClick the "Start final test" button to start the timer.\nThe seconds are shown in green for when you need to \nmeasure your heart rate, the minutes when you don’t need to measure your heart rate are in black. Record your results in the appropriate fields.'
txt_sendresults = 'Send Results'

txt_hinttest1 = '0'
txt_hinttest2 = '0'
txt_hinttest3 = '0'
txt_starttest1 = 'Start first test'
txt_starttest2 = 'Start doing squats'
txt_starttest3 = 'Start final test'
time = QTime(0, 0, 15)
txt_timer = time.toString("hh:mm:ss")
txt_age = 'Age:'
txt_finalwin = 'Results'
txt_index = 'Ruffier index: '
txt_workheart = 'Heart health: '
txt_res1 = "low. See a doctor urgently!"
txt_res2 = "satisfactory. See a doctor!"
txt_res3 = "average. You may want to be examined by a doctor."
txt_res4 = "above average"
txt_res5 = "high"

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Experiment():
    def __init__(self, person, test1, test2, test3):
        self.person = person
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3

class FinalWindow(QWidget):
    def __init__(self, exp, parent=None, flags=Qt.WindowFlags()):
        ''' window in which the survey is conducted '''
        super().__init__(parent=parent, flags=flags)

        #get data about the experiment
        self.exp = exp

        # create and customize graphic elements:
        self.initUI()

        #sets connections between elements
        self.connects()

        #sets how the window will look (label, size, location)
        self.set_appear()
        
        # start:
        self.show()

    def results(self):
        if self.exp.person.age < 7:
            self.index = 0
            return "no data for this age"
        self.index = (4 * (int(self.exp.test1) + int(self.exp.test2) + int(self.exp.test3)) - 200) / 10
        if self.exp.person.age == 7 or self.exp.person.age == 8:
            if self.index >= 21:
                return txt_res1
            elif self.index < 21 and self.index >= 17:
                return txt_res2
            elif self.index < 17 and self.index >= 12:
                return txt_res3
            elif self.index < 12 and self.index >= 6.5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.person.age == 9 or self.exp.person.age == 10:
            if self.index >= 19.5:
                return txt_res1
            elif self.index < 19.5 and self.index >= 15.5:
                return txt_res2
            elif self.index < 15.5 and self.index >= 10.5:
                return txt_res3
            elif self.index < 10.5 and self.index >= 5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.person.age == 11 or self.exp.person.age == 12:
            if self.index >= 18:
                return txt_res1
            elif self.index < 18 and self.index >= 14:
                return txt_res2
            elif self.index < 14 and self.index >= 9:
                return txt_res3
            elif self.index < 9 and self.index >= 3.5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.person.age == 13 or self.exp.person.age == 14:
            if self.index >= 16.5:
                return txt_res1
            elif self.index < 16.5 and self.index >= 12.5:
                return txt_res2
            elif self.index < 12.5 and self.index >= 7.5:
                return txt_res3
            elif self.index < 7.5 and self.index >= 2:
                return txt_res4
            else:
                return txt_res5
        if self.exp.person.age >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index < 15 and self.index >= 11:
                return txt_res2
            elif self.index < 11 and self.index >= 6:
                return txt_res3
            elif self.index < 6 and self.index >= 0.5:
                return txt_res4
            else:
                return txt_res5

    def initUI(self):
        ''' creates graphic elements '''
        self.workh_text = QLabel(txt_workheart + self.results())
        self.index_text = QLabel(txt_index + str(self.index))

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.workh_text, alignment = Qt.AlignCenter)         
        self.setLayout(self.layout_line)

    ''' sets how the window will look (label, size, location) '''
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width3, win_height3)
        self.move(win_x, win_y)

class TestWindow(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        ''' window in which the survey is conducted '''
        super().__init__(parent=parent, flags=flags)

        # creates and customizes graphic elements:
        self.initUI()

        #sets connections between elements
        self.connects()

        #sets how the window will look (label, size, location)
        self.set_appear()
        
        # start:
        self.show()

    def initUI(self):
        ''' creates graphic elements '''
        self.btn_next = QPushButton(txt_next, self)
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.instruction, alignment = Qt.AlignLeft) 
        self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)          
        self.setLayout(self.layout_line)

    
    def next_click(self):
        self.tw = TestWindow()
        self.hide()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    ''' sets how the window will look (label, size, location) '''
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        ''' creates graphic elements '''
        #self.questionnary = AllQuestions()
        self.btn_next = QPushButton(txt_sendresults, self)
        self.btn_test1 = QPushButton(txt_starttest1, self)
        self.btn_test2 = QPushButton(txt_starttest2, self)
        self.btn_test3 = QPushButton(txt_starttest3, self)


        self.text_name = QLabel(txt_name)
        self.text_age = QLabel(txt_age)
        self.text_test1 = QLabel(txt_test1)
        self.text_test2 = QLabel(txt_test2)
        self.text_test3 = QLabel(txt_test3)
        self.text_timer = QLabel(txt_timer)
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))

        self.loc = QLocale(QLocale.English, QLocale.UnitedStates) # language, country
        self.validator = QDoubleValidator()
        self.validator.setLocale(self.loc)

        self.line_name = QLineEdit(txt_hintname)

        self.line_age = QLineEdit(txt_hintage)
        self.line_age.setValidator(self.validator) # the age should be a number!
        self.line_age.setValidator(QIntValidator(7, 150))

        self.line_test1 = QLineEdit(txt_hinttest1)
        self.line_test1.setValidator(self.validator)
        self.line_test1.setValidator(QIntValidator(0, 150))

        self.line_test2 = QLineEdit(txt_hinttest2)
        self.line_test2.setValidator(self.validator)
        self.line_test2.setValidator(QIntValidator(0, 150))

        self.line_test3 = QLineEdit(txt_hinttest3)
        self.line_test3.setValidator(self.validator)
        self.line_test3.setValidator(QIntValidator(0, 150))
    
        self.layout_lineleft = QVBoxLayout()
        self.layout_lineright = QVBoxLayout()
        self.layout_hline = QHBoxLayout()
        self.layout_lineright.addWidget(self.text_timer, alignment = Qt.AlignCenter)
        self.layout_lineleft.addWidget(self.text_name, alignment = Qt.AlignLeft)
        self.layout_lineleft.addWidget(self.line_name, alignment = Qt.AlignLeft) 
        self.layout_lineleft.addWidget(self.text_age, alignment = Qt.AlignLeft)
        self.layout_lineleft.addWidget(self.line_age, alignment = Qt.AlignLeft)
        self.layout_lineleft.addWidget(self.text_test1, alignment = Qt.AlignLeft)
        self.layout_lineleft.addWidget(self.btn_test1, alignment = Qt.AlignLeft)
        self.layout_lineleft.addWidget(self.line_test1, alignment = Qt.AlignLeft) 
        self.layout_lineleft.addWidget(self.text_test2, alignment = Qt.AlignLeft)
        self.layout_lineleft.addWidget(self.btn_test2, alignment = Qt.AlignLeft) 
        self.layout_lineleft.addWidget(self.text_test3, alignment = Qt.AlignLeft)
        self.layout_lineleft.addWidget(self.btn_test3, alignment = Qt.AlignLeft)
        self.layout_lineleft.addWidget(self.line_test2, alignment = Qt.AlignLeft)
        self.layout_lineleft.addWidget(self.line_test3, alignment = Qt.AlignLeft) 
        self.layout_lineleft.addWidget(self.btn_next, alignment = Qt.AlignCenter) 
        self.layout_hline.addLayout(self.layout_lineleft)  
        self.layout_hline.addLayout(self.layout_lineright)        
        self.setLayout(self.layout_hline)

    
    def next_click(self):
        self.hide()
        self.prs = Person(self.line_name.text, int(self.line_age.text()))
        self.exp = Experiment(self.prs, self.line_test1.text(), self.line_test2.text(), self.line_test2.text())
        self.fw = FinalWindow(self.exp)

    def timer_test1(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer_bob(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        #one squat in 1.5 seconds
        self.timer.start(1500)

    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
        self.btn_test1.clicked.connect(self.timer_test1)
        self.btn_test2.clicked.connect(self.timer_bob)
        self.btn_test3.clicked.connect(self.timer_final)

    ''' sets how the window will look (label, size, location) '''
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width2, win_height2)
        self.move(win_x, win_y)


class MainWindow(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        ''' window in which the greeting is located '''
        super().__init__(parent=parent, flags=flags)

        # creates and customizes graphic elements:
        self.initUI()

        #sets connections between elements
        self.connects()

        #sets how the window will look (label, size, location)
        self.set_appear()

        # start:
        self.show()

    def initUI(self):
        ''' creates graphic elements '''
        self.btn_next = QPushButton(txt_next, self)
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.instruction, alignment = Qt.AlignLeft) 
        self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)          
        self.setLayout(self.layout_line)

    
    def next_click(self):
        self.tw = TestWindow()
        self.hide()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    ''' sets how the window will look (label, size, location) '''
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

def main():
    app = QApplication([])
    mw = MainWindow()
    app.exec_()

main()

