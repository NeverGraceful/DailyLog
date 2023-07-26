import drawBig
import sys, os
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QLineEdit, QLabel , QPushButton, QLayout, QMainWindow
import mainVOne, shopWindow, pastWindow, dataStructures
from datetime import date
from pathlib import Path
import shutil
import re
from datetime import date, timedelta
import math

class MoodApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MoodApp, self).__init__()       
        self.ui = mainVOne.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Daliy Log")

        self.ui.SUBMIT.clicked.connect(self.submitted)
        self.ui.PAST_ENTRY.clicked.connect(self.open_dialog)
        self.ui.SHOP_BUTTON.clicked.connect(self.open_dialog)

        self.load_info()
        self.check_streak()
        
        self.ui.POINTS.setText("Points: " + str(self.user_points))
        self.ui.STREAK.setText("Streak: " + str(self.streak))
        self.ui.CURRENT_DATE.setText(date.today().strftime("%m/%d/%Y"))
        self.ui.SUBMIT.setText("Submit Entry")
        self.ui.PAST_ENTRY.setText("View past entrys")
        self.ui.SHOP_BUTTON.setText("Shop")
        self.setup_avatar()
        self.setup_canvas()

    def setup_canvas(self):
        self.canvas = drawBig.Canvas()
        l = QtWidgets.QVBoxLayout()
        self.ui.DRAW_INPUT.setLayout(l)
        l.addWidget(self.canvas) 
        palette = QtWidgets.QHBoxLayout() 
        self.add_palette_buttons(palette) 
        l.addLayout(palette)

    def setup_avatar(self):
        cur_path = Path(os.path.join(self.find_path(),'avatar'))
        pixmap = QPixmap(os.path.join(cur_path, "bodies" + "\\" + self.ava_body + '.png'))
        self.ui.AVATAR_BODY.setPixmap(pixmap)
        pixmap = QPixmap(os.path.join(cur_path, "hats" + "\\" + self.ava_hat + '.png'))
        self.ui.AVATAR_HAT.setPixmap(pixmap)
        pixmap = QPixmap(os.path.join(cur_path, "clothes" + "\\" + self.ava_clothes + '.png'))
        self.ui.AVATAR_CLOTHES.setPixmap(pixmap)

    def check_streak(self):
        yesterday = date.today() - timedelta(days=1)
        yesterday = yesterday.strftime("%m-%d-%Y")
        yesterday_path = Path(os.path.join(self.find_path(),'pastText') +"\\" + yesterday + ".txt")
        today_path = Path(os.path.join(self.find_path(),'pastText') +"\\" + date.today().strftime("%m-%d-%Y") + ".txt")
        if not yesterday_path.is_file() and not today_path.is_file():
            self.streak = 0
    
    def submitted(self):
        today = date.today().strftime("%m-%d-%Y")
        dir = os.path.join(self.find_path(),'pastText')
        file_name = dir +"\\" + today +".txt"
        today_file = Path(dir +"\\" + today + ".txt")
        if not today_file.is_file():
            self.calulate_points_streak()
            
        file = open(file_name, 'w')
        text = self.ui.TEXT_INPUT.toPlainText()
        file.write(text)
        file.close()
        self.save_info()
        self.canvas.save_image()

    def calulate_points_streak(self):
        self.streak = int(self.streak) + 1
        self.ui.STREAK.setText("Streak: " + str(self.streak))
        points_calculated = 5 * math.log(self.streak*2)
        self.user_points = round(points_calculated + float(self.user_points))
        self.ui.POINTS.setText("Points: " + str(self.user_points)) 

    def save_info(self):
        print("Saved")
        wanted_path = os.path.join(self.find_path(),'info.txt')
        info_file = open(wanted_path, 'w')
        info_file.write("streak:" + str(self.streak) 
                        + "\nava_hat:" + str(self.ava_hat) 
                        + "\nava_body:" + str(self.ava_body) 
                        + "\nava_clothes:" + str(self.ava_clothes) 
                        + "\npoints:"+ str(self.user_points) + "\n")
        info_file.close()

    def load_info(self):
        wanted_path = os.path.join(self.find_path(),'info.txt')
        with open(wanted_path) as info_file:
            for line in info_file:
                list = (re.split(':|\n', line))
                print(list)
                match list[0]:
                    case "streak":
                        self.streak = list[1]
                    case "points":
                        self.user_points = list[1]
                    case "ava_hat":
                        self.ava_hat = list[1]
                    case "ava_body":
                        self.ava_body = list[1]
                    case "ava_clothes":
                        self.ava_clothes = list[1]
        info_file.close()

    def add_palette_buttons(self, layout):
        for c in drawBig.COLORS:
            b = drawBig.QPaletteButton(c)
            b.pressed.connect(lambda c=c: self.canvas.set_pen_color(c))
            layout.addWidget(b)

    def open_dialog(self):
        name = self.sender()
        if name.text() == "View past entrys":
            box = pastWindow.PastWindow()
        else:
            box = shopWindow.ShopWindow()
        
        box.exec_()
    
    # find path based off of .py or .exe
    def find_path(self):
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        else:
           application_path = os.path.dirname(os.path.abspath(__file__))

        return application_path

def window():
    app = QApplication(sys.argv)
    win = MoodApp()
    win.show()
    sys.exit(app.exec_())

window()