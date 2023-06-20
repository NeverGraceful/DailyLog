import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(1200, 300, 700, 700)
    win.setWindowIcon(QIcon("hannibal.jpg"))
    win.setWindowTitle("hannibal")

    lbl_name = QtWidgets.QLabel(win) #Text
    lbl_name.setText('Hao>w<!!!!!!: ')
    lbl_name.move(50, 50)
    
    txt_name = QtWidgets.QLineEdit(win) #Input
    txt_name.move(200, 60)

    butt_save = QtWidgets.QPushButton(win)
    butt_save. setText('SavexD')
    butt_save.clicked.connect(clickedUwU)
    butt_save.move(200, 130)

    def clickedUwU(self):
        print("i luv you will..... UwU<3: " + txt_name.text())
        


    win.show()
    sys.exit(app.exec_())

window()