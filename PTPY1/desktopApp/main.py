import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setMinimumSize(400,600)
        self.setWindowTitle("Health Test")

        self.label = QLabel(self, text = "Name: ")
        self.line = QLineEdit(self)

        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.label.move(20, 20)

        self.label1 = QLabel(self, text = "Age: ")
        self.line1 = QLineEdit(self)

        self.line1.move(80, 20)
        self.line1.resize(200, 32)
        self.label1.move(20, 20)

        pybutton = QPushButton('OK', self)
        pybutton.clicked.connect(self.clickEnter)

        # enter.clicked.connect(self.clickEnter)
    
    def clickEnter(self):
        self.nextWindow = FirstWindow()
        self.nextWindow.show() 
        self.close()
    
class FirstWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = mainWindow()
    mainWin.show()
    sys.exit(app.exec_())