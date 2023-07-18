from drawBig import Canvas, COLORS, QPaletteButton
import sys, os
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from mainVOne import Ui_MainWindow
from pastVOne import Ui_Dialog
from datetime import date
from pathlib import Path
import shutil
import re
from datetime import date, timedelta
import math
#main window where the user draws and writes fo rthe days entrys

class MoodApp(QtWidgets.QMainWindow):
    #sets up UI, does the formatting for the canvas
    def __init__(self):
        super(MoodApp, self).__init__()       

        self.setWindowTitle("Daliy Log")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.SUBMIT.clicked.connect(self.submitted)
        self.ui.PAST_ENTRY.clicked.connect(self.open_past_entries)
        
        self.canvas = Canvas()
        l = QtWidgets.QVBoxLayout() # Vertical box layout
        self.ui.DRAW_INPUT.setLayout(l)
        l.addWidget(self.canvas) # Add canvas to layout
        w = self.ui.DRAW_INPUT.width()
        h = self.ui.DRAW_INPUT.height()
        print(str(w) + " " + str(h))
        palette = QtWidgets.QHBoxLayout() # Horizontal box layout
        self.add_palette_buttons(palette) 
        l.addLayout(palette)

        self.ui.CURRENT_DATE.setText(date.today().strftime("%d/%m/%Y"))
        self.ui.SUBMIT.setText("Submit Entry")
        self.ui.PAST_ENTRY.setText("View past entrys")

        self.load_info()
        self.check_streak()
        self.ui.STREAK.setText("Streak: " + str(self.streak))
        self.ui.POINTS.setText("Points: " + str(self.user_points))
        

    #once the user is ready, hits submit button - ends up here
    #saves the drawing as a .png and the text as a .txt
    def submitted(self):
        #add to our hashmap#
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

    def add_palette_buttons(self, layout):
        for c in COLORS:
            b = QPaletteButton(c)
            b.pressed.connect(lambda c=c: self.canvas.set_pen_color(c))
            layout.addWidget(b)

    def open_past_entries(self):
        box = PastWindow()
        box.exec_()

    def load_info(self):
        wanted_path = os.path.join(self.find_path(),'info.txt')
        # print("CURRENT CWD: "+str(os.getcwd()))
        # os.chdir(Path(os.path.abspath(__file__) + "\\" + 'info.txt'))
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
        info_file.close()

    def calulate_points_streak(self):
        self.streak = int(self.streak) + 1
        self.ui.STREAK.setText("Streak: " + str(self.streak))
        points_calculated = 5 * math.log(self.streak*2)
        self.user_points = round(points_calculated + float(self.user_points))
        self.ui.POINTS.setText("Points: " + str(self.user_points))     

    def check_streak(self):
        yesterday = date.today() - timedelta(days=1)
        yesterday = yesterday.strftime("%m-%d-%Y")
        wanted_path = Path(os.path.join(self.find_path(),'pastText') +"\\" + yesterday + ".txt")
        if not wanted_path.is_file():
            #streak is broken awwwww man
            print("we are getting here! sad!: "+ str(wanted_path))
            self.streak = 0

    def save_info(self):
        print("Saved")
        wanted_path = os.path.join(self.find_path(),'info.txt')
        info_file = open(wanted_path, 'w')
        info_file.write("streak:" + str(self.streak) + "\nava_hat:"+ str(self.ava_hat) + "\npoints:"+ str(self.user_points) + "\n")
        info_file.close()

    def find_path(self):
        
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        else:
           application_path = os.path.dirname(os.path.abspath(__file__))

        return application_path

# window that shows past entries  
class PastWindow(QtWidgets.QDialog):
    def __init__(self):
        super(PastWindow, self).__init__()
        #sets up the UI
        self.setWindowTitle("hahah")
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.PAST_DRAWING.setText(" ")
        self.ui.RETURN.setText("Return")
        self.ui.RETURN.clicked.connect(self.close_past)
        self.ui.SAVE_DRAWING.setText("Save Drawing")
        self.ui.SAVE_DRAWING.clicked.connect(self.export_drawing)
        self.ui.SAVE_TEXT.setText("Save Text")
        self.ui.SAVE_TEXT.clicked.connect(self.export_text)
        self.ui.CALENDAR.clicked.connect(self.display_entry)


    #displays past entries
    def display_entry(self):
        selectedDate = self.ui.CALENDAR.selectedDate().toString("MM-dd-yyyy")
        wanted_path = os.path.join(self.find_path(),'pastDrawings') +"\\" + selectedDate + ".png"
        print("JUST CHECKING OMg: "+wanted_path)
        #checking if the file exists
        self.im = QPixmap(wanted_path)
        self.ui.PAST_DRAWING.setPixmap(self.im)
        wanted_text_path =  os.path.join(self.find_path(),'pastText') +"\\" + selectedDate + ".txt"
        print("past drawing path: "+ wanted_path)
        
        if not os.path.isfile(wanted_text_path):
            self.ui.PAST_TEXT.setText("No entry in storage")
            return
            
        text_file = open(wanted_text_path, "r")
        self.ui.PAST_TEXT.setWordWrap(True) #formating text
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
                  


def window():
    app = QApplication(sys.argv)
    win = MoodApp()
    win.show()
    sys.exit(app.exec_())

window()
