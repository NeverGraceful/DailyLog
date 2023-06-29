import sys
# from dummy import Ui_MainWindow #import dummy window
# from splash import 
from PyQt5 import QtWidgets 
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QSplashScreen, QProgressBar
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
import time


class SplashScreen(QSplashScreen):

    def __init__(self):
        super(QSplashScreen, self).__init__()
        loadUi("splashTwo.ui", self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        pixmap = QPixmap("wilson.png")
        self.setPixmap(pixmap)

    def progress(self):
        for i in range(100):
            time.sleep(0.1)
            self.PROGRESS.setValue(i)

class MainPage(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        loadUi('dummyTwo.ui', self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    splash = SplashScreen()
    splash.show()
    splash.progress()
    

    win = MainPage()
    win.show()

    splash.finish(win)
    
    sys.exit(app.exec_())

