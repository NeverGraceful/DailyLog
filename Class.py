import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QColor, QPalette

class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
        paletta = self.palette()
        paletta.setColor(QPalette.Window, QColor(color))
        self.setPalette(paletta)

class moo_window(QMainWindow):
    def __init__(self):
        super(moo_window, self).__init__()
        self.setGeometry(1200, 300, 700, 700)
        self.setWindowTitle("hannibal")

        slutLayout = QtWidgets.QGridLayout()
        slutLayout.addWidget(Color('purple'),0,0)
        slutLayout.addWidget(Color('white'),50,50)
        slutLayout.setSpacing(40)

        whoreLayout = QtWidgets.QHBoxLayout()
        whoreLayout.addWidget(Color('pink'))
        whoreLayout.addWidget(Color('orange'))
        whoreLayout.addWidget(Color('white'))

        widget = QWidget()
        widget.setLayout(slutLayout)
        self.setCentralWidget(widget)
        
        self.init_UI()
    
    def init_UI(self):
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText("Hao>w<!!!!!!: ")
        self.lbl_name.move(50, 50)

        self.user_input = QtWidgets.QLineEdit(self) #Input
        self.user_input.move(200, 60)

        self.butt_save = QtWidgets.QPushButton(self)
        self.butt_save.setText('SavexD')
        self.butt_save.clicked.connect(self.clickedUwU)
        self.butt_save.move(200, 130)

    def clickedUwU(self):
        name = self.user_input.text()
        if str(name) == "I love you hannibal":
            print("i luv you will..... UwU<3: ")
        else:
            print("*stimache rumbles*")



def window():
    app = QApplication(sys.argv)
    win = moo_window()
    win.show()
    sys.exit(app.exec_())

window()