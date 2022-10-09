from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, QGridLayout, 
        QGroupBox, QRadioButton,  
        QPushButton, QLabel, QListWidget)

from data structure.py import list_from_choices, list_from_types

txt_alt = 'Choose '
txt_next = 'Next'
txt_prev = 'Back' 
txt_finish = 'Finish'
txt_title = 'Super oh-so-differential survey'
txt_result = 'Points'
txt_descr = 'Description'
txt_more = 'More'


win_width, win_height = 800, 300
win_x, win_y = 200, 200

class AlternativeGroup():
    ''' displays two options'''
    def __init__(self, a1, a2, number, parent=None):
        ''' two alternatives and a question number are given '''
        self.a1 = QRadioButton(a1, parent)
        self.a2 = QRadioButton(a2, parent)
        self.number = number
        self.initUI()
    def initUI(self):
        ''' creates graphic elements '''
        layoutH = QHBoxLayout()
        layoutH.addWidget(self.a1, alignment=Qt.AlignHCenter)
        layoutH.addWidget(self.a2, alignment=Qt.AlignHCenter)
        text = txt_alt + str(self.number + 1)
        self.group = QGroupBox(text)
        self.group.setLayout(layoutH)
    def show(self):
        self.group.show()
    def hide(self):
        self.group.hide()
    def is_checked(self):
        '''answers if an answer is selected'''
        return self.a1.isChecked() or self.a2.isChecked() 
    def value(self):
        val = 0
        answer = ''
        if self.a1.isChecked():
            val, answer = 1, self.a1.text()
        elif self.a2.isChecked():
            val, answer = 2, self.a2.text()
        return (self.number, val, answer)

class AllQuestions(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        ''' a widget with lots of panels, each with two options '''
        super().__init__(parent=parent, flags=flags)
        self.list_choices = [] # a list of panel-instances of the AlternativeGroup class
        self.layoutV = QVBoxLayout()
        self.current_choice = -1 # current question
    def add_choice(self, a1, a2):
        number = len(self.list_choices)
        choice = AlternativeGroup(a1, a2, number, self)
        self.list_choices.append(choice)
        self.layoutV.addWidget(choice.group)
        choice.hide()
    def show_curr(self):
        self.list_choices[self.current_choice].show()
    def hide_curr(self):
        self.list_choices[self.current_choice].hide()
    def start(self):
        self.current_choice = 0
        self.show_curr()
        self.setLayout(self.layoutV)
        self.show()
    def is_checked(self):
        return self.list_choices[self.current_choice].is_checked()
    def is_last(self):
        return self.current_choice >= len(self.list_choices) - 1
    def is_first(self):
        return self.current_choice <= 0
    def next(self):
        if self.is_checked() and not self.is_last():
            self.hide_curr()
            self.current_choice += 1
            self.show_curr()
    def prev(self):
        if not self.is_first():
            self.hide_curr()
            self.current_choice -= 1
            self.show_curr()

    def calculate_values(self):
        values = []
        for choice in self.list_choices:
            values.append(choice.value()) 
        return values

class MainWindow(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        ''' window in which the survey is conducted '''
        super().__init__(parent=parent, flags=flags)
        # loading data: 
        self.list_choices = list_from_choices()
        self.list_types = list_from_types()
        # creating and customizing graphic elements:
        self.initUI()
        self.connects()
        self.set_appear()
        # transferring data to widgets:
        self.load_questions()
        self.questionnary.start()
        # start:
        self.show()

    def initUI(self):
        ''' creates graphic elements '''
        self.questionnary = AllQuestions()
        self.btn_next = QPushButton(txt_next, self)
        self.btn_prev = QPushButton(txt_prev, self)

        layout_line = QHBoxLayout()
        layout_line.addStretch(1)
        layout_line.addWidget(self.btn_prev)
        layout_line.addStretch(1)
        layout_line.addWidget(self.btn_next)
        layout_line.addStretch(1)                

        layout_column = QVBoxLayout()
        layout_column.addWidget(self.questionnary)
        layout_column.addLayout(layout_line)
        self.setLayout(layout_column)

    def addchoice(self, a1, a2):
        self.questionnary.add_choice(a1, a2)

    def load_questions(self):
        for question in self.list_choices:
            self.addchoice(question.a1, question.a2)
    
    def next_click(self):
        if self.questionnary.is_last():
            self.finish(self.questionnary.calculate_values())
        else:
            self.questionnary.next()
            if self.questionnary.is_last():
                self.btn_next.setText(txt_finish)
            
    def prev_click(self):
        self.btn_next.setText(txt_next)
        self.questionnary.prev()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
        self.btn_prev.clicked.connect(self.prev_click)

    def set_appear(self):
        ''' sets how the window will look (label, size, location) '''
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def finish(self, list_answers):
        list_result = []
        for i, profession_type in enumerate(self.list_types):
            result = profession_type.check(list_answers)
            list_result.append( (result, i, profession_type.description) ) 
        list_result.sort(reverse=True) # sorting in descending order
        self.rt = ResultTable(list_result, self.list_types)
        self.hide()
        self.rt.show()

class ResultTable(QWidget):
    def __init__(self, list_result, list_types, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.list_result = list_result
        self.list_types = list_types
        self.show_results()
        self.add_answerslist()
        self.connects()

    def show_results(self):
        self.layoutG = QGridLayout()
        self.generate_buttons()
        self.add_titlerow()
        self.add_rows()

    def add_answerslist(self):
        self.lw_answers = QListWidget(self)
        layoutV = QVBoxLayout()
        layoutV.addLayout(self.layoutG)
        layoutV.addWidget(self.lw_answers)
        self.lw_answers.hide()
        self.setLayout(layoutV)

    def generate_buttons(self):
        self.buttons = []
        for i in self.list_result:
            self.buttons.append(QPushButton(txt_more))

    def add_titlerow(self):
        self.layoutG.addWidget(QLabel(txt_result), 0, 0)
        self.layoutG.addWidget(QLabel(txt_descr), 0, 1)
        
    def add_row(self, row, result, i, description):
        self.layoutG.addWidget(QLabel(str(result)), row, 0)
        self.layoutG.addWidget(QLabel(description), row, 1)
        self.layoutG.addWidget(self.buttons[i], row, 2)

    def add_rows(self):
        for row, res in enumerate(self.list_result):
            result, i, description = res[0], res[1], res[2]
            self.add_row(row + 1, result, i, description)

    def clicked_0(self):
        self.current_index = 0
        self.show_answers()
    def clicked_1(self):
        self.current_index = 1
        self.show_answers()
    def clicked_2(self):
        self.current_index = 2
        self.show_answers()
    def clicked_3(self):
        self.current_index = 3
        self.show_answers()
    def clicked_4(self):
        self.current_index = 4
        self.show_answers()

    def connects(self):
        self.buttons[0].clicked.connect(self.clicked_0)
        self.buttons[1].clicked.connect(self.clicked_1)
        self.buttons[2].clicked.connect(self.clicked_2)
        self.buttons[3].clicked.connect(self.clicked_3)
        self.buttons[4].clicked.connect(self.clicked_4)

    def show_answers(self):
        l_a = self.list_types[self.current_index].answers
        self.lw_answers.hide()
        show_list(self.lw_answers, l_a)
        self.lw_answers.show()
        
def show_list(lw: QListWidget, list_data):
    lw.clear()
    for data_str in list_data:
        lw.addItem(data_str)

def main():
    app = QApplication([])
    mw = MainWindow()
    app.exec_()

main()

