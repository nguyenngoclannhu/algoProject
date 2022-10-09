''' The program assists in calculating the NPV (Net Present Value) of cash flows.
The user enters amounts for some period of time (after so many years/months)
and the program brings all these amounts up to date.
You can see when a project will pay off, if at the present certain spending is needed,
and whether there will be earnings in the future.
'''

from PyQt5.QtCore import Qt, QLocale # Qt - namespace, needed to use constants
                                     # QLocale - needed to switch the number format to American, which only understands Python
from PyQt5.QtGui import QDoubleValidator, QIntValidator # checking input value types
from PyQt5.QtWidgets import (QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, QGridLayout,
        QSpinBox, QLabel, QLineEdit, QPushButton)

QSS_LabelBold = '''QLabel { 
    font: bold 20px;
}'''
QSS_Columns = '''QLabel { 
    font: bold 14px "Courier New";
}'''

def fix_point(amount):
    ''' adjusts the string to return a number in any case '''
    try:
        result = float(amount)
        return result
    except ValueError:
        try:
            result = float(amount.replace(',', '.')) # Qt allows commas to be entered even with English locale...
            return result
        except ValueError:
            return 0 # if the user has deleted everything, Qt will skip this string.

def discount(amount, years, months, base, rate):
    ''' the function calculates the present value of a future amount 
     by time - in years and months from now
     by interest rate (percent per annum).
     The base parameter says how often the interest is calculated (a number between 1 and 12 months is expected)'''
    # we calculate how many times interest was accrued during this time:
    total_months = 12 * years + months
    periods = total_months // base # so many times
    tail = total_months % base # so many months have passed in the last period, a simple percentage is applied to them

    # we calculate with the rate as a percentage that is paid for base months (i.e. not always interest per annum!)
    rate = rate/100 # we move from percent to a normal number
    simple = 1 + (tail * rate) / base # accruals in the last period - according to the rule of simple interest, i.e. simple in proportion
    compound = pow(1 + rate, periods) # so much compound interest

    return round( amount / (simple * compound) , 4)

class FutureAmount(QWidget):
    ''' One string of the table. 
    The string contains the amount and time (in how many years/months it will be)
     The discounted amount is written automatically when you enter these values
     To calculate, you need to know the interest rate, so the string stores a pointer to the corresponding input field
    '''
    def __init__(self, rate_widget, base_widget, amount=0, years=0, months=0, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags) # creating a base widget
        # remember the parameters with which the instance is created:
        self.years = years
        self.months = months
        self.amount = amount
        self.rate_widget = rate_widget
        self.base_widget = base_widget
        # placing visual elements:
        self.create_widgets()
        # connect the signals and show the string:
        self.recalc() # we call it manually once to calculate the values from the constructor
        self.connects()
        self.show()
    
    def create_widgets(self):
        ''' creates internal widgets and calls their placement method'''
        self.txt_amount = QLineEdit(str(self.amount))
        loc = QLocale(QLocale.English, QLocale.UnitedStates) # language, country
        validator = QDoubleValidator()
        validator.setLocale(loc)
        self.txt_amount.setValidator(validator) # the amount of money must be a number!
        self.txt_years = QLineEdit(str(self.years))
        self.txt_years.setValidator(QIntValidator(0, 10000)) # must be limited somehow ))
        self.txt_months = QLineEdit(str(self.months))
        self.txt_months.setValidator(QIntValidator(0, 11)) # this will limit it to two decimal places 
        self.lbl_pv = QLabel() # present value cannot be edited
        self.lay_widgets()

    def lay_widgets(self):
        ''' places the internal widgets in a row'''
        layout_h = QHBoxLayout()
        layout_h.setContentsMargins(20, 0, 20, 0)
        layout_h.addWidget(self.txt_years)
        layout_h.addWidget(self.txt_months)
        layout_h.addStretch(1)
        layout_h.addWidget(self.txt_amount)
        layout_h.addStretch(1)
        layout_h.addWidget(self.lbl_pv)
        self.setLayout(layout_h)

    def connects(self):
        ''' the current value is recalculated inside the string if any number is changed'''
        self.txt_amount.editingFinished.connect(self.recalc)
        self.txt_years.editingFinished.connect(self.recalc)
        self.txt_months.editingFinished.connect(self.recalc)

    def recalc(self):
        ''' recalculates the values of the class properties, sets the required amount in the corresponding label '''
        base = int(self.base_widget.text())   # we take the frequency of accrual from the input field 
        rate = fix_point(self.rate_widget.text()) # we take the appropriate rate from the input field 
                    # right, it isn’t pretty, no data layer separation, 
                    # but in this program it does not make sense to start a data level separately
        # save the values from the input fields:
        self.amount = fix_point(self.txt_amount.text())
        self.years = int(self.txt_years.text())
        self.months = int(self.txt_months.text())
        # calculate PV:
        result = discount(self.amount, self.years, self.months, base, rate)
        # self.lbl_pv.setText(str(result)) # rendering
        self.lbl_pv.setText("{0:.4f}".format(result)) # rendering - redone to always have 4 decimal places

class CashFlow(QWidget):
    ''' the "Flow" class stores the strings that make up the cash flow,
     and it also shows the general parameters of the cash flow: interest rate, frequency of interest accrual, the NPV itself '''
    def __init__(self, rate=0.0, base=12, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        # remembering the parameters with which the instance is created:
        self.rate = rate
        self.base = base
        # there is no cash flow yet, we start the corresponding properties:
        self.NPV = 0 
        self.amounts = []
        # placing visual elements:
        self.create_widgets()
        # connecting the signals and showing:
        self.connects()
        self.show()

    def add_fa(self):
        ''' adds one future amount'''
        months = self.months_to_add()
        years, months = months // 12, months % 12
        # adding with calculated parameters:
        fa = FutureAmount(self.txt_rate, self.spin_base, self.last_amount(), years, months)
        self.layout_famounts.addWidget(fa) # rendering
        # we do not have a signal to change the total amount, so we do this:
        fa.txt_amount.editingFinished.connect(self.recalc)
        fa.txt_years.editingFinished.connect(self.recalc)
        fa.txt_months.editingFinished.connect(self.recalc)
        # adding to the list:
        self.amounts.append(fa)
        # recalculating the total amount:
        self.recalc()
    
    def months_to_add(self):
        ''' it is trying to predict how many months to add for a new string'''
        total = len(self.amounts)
        if 0 == total:
            return 0 # we expect the first line to have the initial investments
        elif 1 == total:
            return 12 # we automatically start adding years
        else:
            # when we have the two last lines, we need to understand how many months are between them, 
            # and add that to the last one
            fa_2 = self.amounts[total - 2] # second string from the end
            fa_1 = self.amounts[total - 1] # first from the end
            months_1 = int(fa_1.txt_years.text()) * 12 + int(fa_1.txt_months.text())
            months_2 = int(fa_2.txt_years.text()) * 12 + int(fa_2.txt_months.text())
            return months_1 + (months_1 - months_2)
    
    def last_amount(self):
        ''' returns the sum in the last string to duplicate it in the newly added one '''
        total = len(self.amounts)
        if total:
            fa = self.amounts[total - 1]
            return fix_point(fa.txt_amount.text())
        return 0

    def recalc(self):
        ''' sums up the total for all strings '''
        result = 0
        for future_amount in self.amounts:
            result += float(future_amount.lbl_pv.text())
        self.lbl_npv.setText(str(round(result, 4)))
    
    def recalc_them_all(self):
        ''' recalculates all subtotals and the total'''
        for future_amount in self.amounts:
            future_amount.recalc()
        self.recalc()

    def connects(self):
        ''' imports the processing of user actions '''
        self.button_plus.clicked.connect(self.add_fa)
        self.txt_rate.editingFinished.connect(self.recalc_them_all)
        self.spin_base.valueChanged.connect(self.recalc_them_all)
    
    def create_widgets(self):
        ''' creates internal widgets and calls their placement method'''
        # choose recalculation frequency:
        self.lbl_base1 = QLabel('accrual once in')
        self.spin_base = QSpinBox() 
        # self.spin_base.
        # setValidator(QIntValidator(1, 13))
        self.spin_base.setValue(self.base)
        self.spin_base.setRange(1, 12)
        self.lbl_base2 = QLabel('months')
        # enter rate:
        self.lbl_rate1 = QLabel('rate:')
        self.txt_rate = QLineEdit('0')
        loc = QLocale(QLocale.English, QLocale.UnitedStates) # we enter it with a dot separator, so that python understands
        validator = QDoubleValidator()
        validator.setLocale(loc)
        self.txt_rate.setValidator(validator)
        self.lbl_rate2 = QLabel('percent')
        # result:
        self.lbl_result1 = QLabel('Total:')
        self.lbl_npv = QLabel(str(self.NPV))
        self.lbl_npv.setStyleSheet(QSS_LabelBold)
        self.lbl_result2 = QLabel(' rubles')
        # "OK" and "+" buttons at the end of all strings:
        self.button_ok = QPushButton('OK')
        self.button_plus = QPushButton(' + ')
        # now place
        self.lay_widgets()

    def lay_widgets(self):
        ''' places widgets in a column,
         and one of the cells in this column is layout,
         to which widgets of the type FutureAmount will be added '''
        self.layout_main = QVBoxLayout()
        self.layout_famounts = QVBoxLayout()
        layout_h1 = QHBoxLayout() # result
        layout_h2 = QHBoxLayout() # percent
        layout_h3 = QHBoxLayout() # frequency
        layout_top = QHBoxLayout() # top string
        layout_bottom = QHBoxLayout() # bottom string
        # let’s go:
        layout_h1.addWidget(self.lbl_result1, alignment=Qt.AlignRight)
        layout_h1.addWidget(self.lbl_npv)
        layout_h1.addWidget(self.lbl_result2, alignment=Qt.AlignLeft)
        layout_h2.addWidget(self.lbl_rate1, alignment=Qt.AlignRight)
        layout_h2.addWidget(self.txt_rate)
        layout_h2.addWidget(self.lbl_rate2, alignment=Qt.AlignLeft)
        layout_h3.addWidget(self.lbl_base1, alignment=Qt.AlignRight)
        layout_h3.addWidget(self.spin_base)
        layout_h3.addWidget(self.lbl_base2, alignment=Qt.AlignLeft)
        # we form the top string from this:
        # layout_top.addLayout(layout_h1) - no, the bottom string looks better!
        # layout_top.addStretch(2)
        layout_top.addLayout(layout_h2)
        layout_top.addStretch(2)
        layout_top.addLayout(layout_h3)
        self.layout_main.addLayout(layout_top) # added
        # and bottom string:
        layout_bottom.addWidget(self.button_ok)
        layout_bottom.addStretch(2)
        layout_bottom.addLayout(layout_h1)
        layout_bottom.addStretch(2)
        layout_bottom.addWidget(self.button_plus, alignment=Qt.AlignRight)
        self.layout_main.addLayout(layout_bottom) # added

        # now a string with the column names:
        layout_h = QHBoxLayout()
        # you can align all the headers with fields using the table, but if there isn’t one, you have to do it like this:
        layout_h.setContentsMargins(20, 0, 20, 0)
        lbc1 = QLabel(':      years      :') 
        lbc1.setStyleSheet(QSS_Columns)
        layout_h.addWidget(lbc1, alignment=Qt.AlignHCenter)
        lbc2 = QLabel(':    months    :')
        lbc2.setStyleSheet(QSS_Columns)
        layout_h.addWidget(lbc2, alignment=Qt.AlignHCenter)
        layout_h.addStretch(1)
        lbc3 = QLabel(':     amount     :')
        lbc3.setStyleSheet(QSS_Columns)
        layout_h.addWidget(lbc3, alignment=Qt.AlignHCenter)
        layout_h.addStretch(1)
        lbc4 = QLabel('total:')
        lbc4.setStyleSheet(QSS_Columns)
        layout_h.addWidget(lbc4, alignment=Qt.AlignRight)
    
        self.layout_famounts.addLayout(layout_h)
        # in layout_famounts strings will be added by clicking on '+'
        self.layout_main.addLayout(self.layout_famounts) # added

        self.setLayout(self.layout_main)

app = QApplication([])
main = CashFlow()
main.resize(750, 200)
main.setWindowTitle('Financial calculator')
app.exec()

