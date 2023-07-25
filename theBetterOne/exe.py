import drawBig
import sys, os
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QLineEdit, QLabel , QPushButton, QHBoxLayout, QVBoxLayout, QMainWindow
import mainVOne, pastVOne, shop
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
        pixmap = QPixmap("avatar" + "\\" + "body" + "\\" + self.ava_body + '.png')
        self.ui.AVATAR_BODY.setPixmap(pixmap)
        pixmap = QPixmap("avatar" + "\\" + "hat" + "\\" + self.ava_body + self.ava_hat + '.png')
        self.ui.AVATAR_HAT.setPixmap(pixmap)
        
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
        info_file.close()

    def add_palette_buttons(self, layout):
        for c in drawBig.COLORS:
            b = drawBig.QPaletteButton(c)
            b.pressed.connect(lambda c=c: self.canvas.set_pen_color(c))
            layout.addWidget(b)

    def open_dialog(self):
        name = self.sender()
        if name.text() == "View past entrys":
            box = PastWindow()
        else:
            box = ShopWindow()
        
        box.exec_()
    
    # find path based off of .py or .exe
    def find_path(self):
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        else:
           application_path = os.path.dirname(os.path.abspath(__file__))

        return application_path

class PastWindow(QtWidgets.QDialog):
    def __init__(self):
        super(PastWindow, self).__init__()
        self.ui = pastVOne.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Past Entrys")
        self.ui.PAST_DRAWING.setText(" ")
        self.ui.RETURN.setText("Return")
        self.ui.RETURN.clicked.connect(self.close_past)
        self.ui.SAVE_DRAWING.setText("Save Drawing")
        self.ui.SAVE_DRAWING.clicked.connect(self.export_drawing)
        self.ui.SAVE_TEXT.setText("Save Text")
        self.ui.SAVE_TEXT.clicked.connect(self.export_text)
        self.ui.CALENDAR.clicked.connect(self.display_entry)

    def display_entry(self):
        selectedDate = self.ui.CALENDAR.selectedDate().toString("MM-dd-yyyy")
        wanted_path = os.path.join(self.find_path(),'pastDrawings') +"\\" + selectedDate + ".png"
        print("JUST CHECKING OMg: "+wanted_path)
        self.im = QPixmap(wanted_path)
        self.ui.PAST_DRAWING.setPixmap(self.im)
        wanted_text_path =  os.path.join(self.find_path(),'pastText') +"\\" + selectedDate + ".txt"
        print("past drawing path: "+ wanted_path)
        
        if not os.path.isfile(wanted_text_path):
            self.ui.PAST_TEXT.setText("No entry in storage")
            return
            
        text_file = open(wanted_text_path, "r")
        self.ui.PAST_TEXT.setWordWrap(True)
        self.ui.PAST_TEXT.setText(text_file.read())
        self.ui.DATE_DISPLAYED.setText(selectedDate)
        text_file.close()
        self.show()

    def export_drawing(self):
        selectedDate = self.ui.CALENDAR.selectedDate().toString("MM-dd-yyyy")
        wanted_path = os.path.join(self.find_path(),'pastDrawings') +"\\" + selectedDate + ".png"
        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save Image", "",
                         "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")
        if file_name == "":
            return
    
        shutil.copyfile(wanted_path, file_name)

    def export_text(self):
        selectedDate = self.ui.CALENDAR.selectedDate().toString("MM-dd-yyyy")
        wanted_path = os.path.join(self.find_path(),'pastText') +"\\" + selectedDate + ".txt"
        file_name, _ =QtWidgets.QFileDialog.getSaveFileName(self, "Save Image", "",
                         "TXT(*.txt);;All Files(*.*) ")
        
        if file_name == "":
            return

        shutil.copyfile(wanted_path, file_name)

    def find_path(self):
        print(os.path.dirname(sys.executable))
        application_path = 0
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        else:
            print("making it here lolol")
            application_path = os.path.dirname(os.path.abspath(__file__))
            print("application path "+ application_path)

        return application_path

        
    def close_past(self):
        self.close()

class ShopWindow(QtWidgets.QDialog):
    def __init__(self):
        super(ShopWindow, self).__init__()
        self.ui = shop.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Shop')
        self.ui.SCROLL = QtWidgets.QScrollArea(self)
        self.vbox = QVBoxLayout()

        for i in range(1,40):
            object = QPushButton("haha")
            self.vbox.addWidget(object)

        self.ui.SHOP.setLayout(self.vbox)

        self.ui.SCROLL.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ui.SCROLL.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.SCROLL.setWidgetResizable(True)
        self.ui.SCROLL.setWidget(self.ui.SHOP)
        self.ui.SCROLL.setGeometry(210, 40, 261, 351)

def window():
    app = QApplication(sys.argv)
    win = MoodApp()
    win.show()
    sys.exit(app.exec_())

window()