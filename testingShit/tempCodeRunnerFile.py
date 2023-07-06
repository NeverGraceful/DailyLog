import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel
from huh import Ui_MainWindow

class OurApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(OurApp, self).__init__()
        self.setWindowTitle("hannibal")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Slut.stateChanged.connect(self.do_something)
        self.ui.Bitch.stateChanged.connect(self.do_something)
        self.ui.Whore.stateChanged.connect(self.do_something) # QtWidgets.Qlabel,  self.lbl_name = QtWidgets.QLabel(self)

    def do_something(self, value):
        check_state = self.sender()
        label = QLabel(self)
        if check_state.text() == 'Whore':
            pixmap = QPixmap('hannibal.jpg')
            label.setPixmap(pixmap)
            self.setCentralWidget(label)
            self.resize(pixmap.width(), pixmap.height())
        elif check_state.text() == 'Slut':
            pixmap = QPixmap('will.png')
            label.setPixmap(pixmap)
            self.setCentralWidget(label)
            self.resize(pixmap.width(), pixmap.height())
        else:
            print("safe...for now")

def window():
    app = QApplication(sys.argv)
    win = OurApp()
    win.show()
    sys.exit(app.exec_())

window()