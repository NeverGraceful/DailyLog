from drawBig import Canvas, COLORS, QPaletteButton
import sys, os
from PyQt5 import QtCore, QtWidgets, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QDialog
from mainVOne import Ui_MainWindow
from pastVOne import Ui_Dialog
from datetime import date
from pathlib import Path


#main window where the user draws and writes fo rthe days entrys

class MoodApp(QtWidgets.QMainWindow):
    #sets up UI, does the formatting for the canvas
    def __init__(self):
        super(MoodApp, self).__init__()
        self.setWindowTitle("Mood Thingy")
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
        #scaling the pixmap to the DRAW_INPUT label
        self.ui.DRAW_INPUT.setPixmap(self.canvas.pixmap().scaled(w,h,QtCore.Qt.KeepAspectRatio))

        palette = QtWidgets.QHBoxLayout() # Horizontal box layout
        self.add_palette_buttons(palette) 
        l.addLayout(palette)

        self.ui.CURRENT_DATE.setText(date.today().strftime("%d/%m/%Y"))
        self.ui.SUBMIT.setText("Submit Entry")
        self.ui.PAST_ENTRY.setText("View past entrys")

    #once the user is ready, hits submit button - ends up here
    #saves the drawing as a .png and the text as a .txt
    def submitted(self):
        #add to our hashmap# today = date.today().strftime("%d/%m/%Y") # d1 = today.strftime("%d/%m/%Y") "dd/mm/YY"
        today = date.today().strftime("%d-%m-%Y")
        dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),'pastText')
        file_name = dir +"\\" + today +".txt"
        file = open(file_name, 'w')
        text = self.ui.TEXT_INPUT.toPlainText()
        file.write(text)
        file.close()
        self.canvas.save_image()

    def add_palette_buttons(self, layout):
        for c in COLORS:
            b = QPaletteButton(c)
            b.pressed.connect(lambda c=c: self.canvas.set_pen_color(c))
            layout.addWidget(b)

    def open_past_entries(self):
        box = PastWindow()
        box.exec_()
        

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
        self.ui.SAVE_PAST.setText("Save Drawing")
        self.ui.CALENDAR.clicked.connect(self.display_entry)


    #displays past entries
    def display_entry(self):
        selectedDate = self.ui.CALENDAR.selectedDate().toString("MM-dd-yyyy")
        wanted_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'pastDrawings') +"\\" + selectedDate + ".png"
        #checking if the file exists
        self.im = QPixmap(wanted_path)
        self.ui.PAST_DRAWING.setPixmap(self.im)
        wanted_text_path =  os.path.join(os.path.dirname(os.path.abspath(__file__)),'pastText') +"\\" + selectedDate + ".txt"
        
        if not os.path.isfile(wanted_text_path):
            self.ui.PAST_TEXT.setText("No entry in storage")
            return
            
        text_file = open(wanted_text_path, "r")
        self.ui.PAST_TEXT.setWordWrap(True) #formating text
        self.ui.PAST_TEXT.setText(text_file.read())
        self.ui.DATE_DISPLAYED.setText(selectedDate)
        text_file.close()
        self.show()
        
        
 
    def close_past(self):
        self.close()


def window():
    app = QApplication(sys.argv)
    win = MoodApp()
    win.show()
    sys.exit(app.exec_())

window()

