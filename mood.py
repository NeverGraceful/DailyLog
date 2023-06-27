from data_structures import Mood_Entry, dictionary
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel
from uiOne import Ui_MainWindow

class MoodApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MoodApp, self).__init__()
        self.setWindowTitle("Mood Thingy")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.ENTER.clicked.connect(self.do_something)
        self.ui.RETRIEVE.clicked.connect(self.do_something)

    def do_something(self):

        if self.sender().text() == 'ENTER':
            print("Enter")
            #add to our hashmap
            dictionary.update({self.ui.DATE.text():self.ui.MOOD.toPlainText()})


        elif dictionary.get(self.ui.DATE.text()) == None:
        #elif self.ui.DATE.text() in dictionary:
            print("you havent inputed anything for this stupid!!!!!")

        else:
            #print from our hasmap
            self.ui.label.setText("RESULT: " + str(dictionary[self.ui.DATE.text()]))






def window():
    app = QApplication(sys.argv)
    win = MoodApp()
    win.show()
    sys.exit(app.exec_())


window()

