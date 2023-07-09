import typing
from data_structuresBig import Mood_Entry, dictionary
from drawBig import Canvas, COLORS, QPaletteButton
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from mainVOne import Ui_MainWindow
from datetime import date
from pathlib import Path

class MoodApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MoodApp, self).__init__()
        self.setWindowTitle("Mood Thingy")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.SUBMIT.clicked.connect(self.submitted)
        
        self.canvas = Canvas()
        l = QtWidgets.QVBoxLayout() # Vertical box layout
        self.ui.DRAW_INPUT.setLayout(l)
        l.addWidget(self.canvas) # Add canvas to layout
        palette = QtWidgets.QHBoxLayout() # Horizontal box layout
        self.add_palette_buttons(palette) 
        l.addLayout(palette)

        self.ui.CURRENT_DATE.setText(date.today().strftime("%d/%m/%Y"))
        self.ui.SUBMIT.setText("Submit Entry")
        self.ui.PAST_ENTRY.setText("View past entrys")

    def submitted(self):
        #add to our hashmap
        today = date.today().strftime("%d/%m/%Y") # d1 = today.strftime("%d/%m/%Y") "dd/mm/YY"
        dictionary.update({today:self.ui.TEXT_INPUT.toPlainText()})
        self.canvas.save_image()
        # dictionary.update({self.ui.CALENDAR.selectedDate().toString():self.ui.MOOD.toPlainText()})

    def add_palette_buttons(self, layout):
        for c in COLORS:
            b = QPaletteButton(c)
            b.pressed.connect(lambda c=c: self.canvas.set_pen_color(c))
            layout.addWidget(b)

    # def open_past_entries(self):
        


class PastWindow(QtWidgets.QDialog):
    def __init__(self):
        super(PastWindow, self).__init__()
        self.setWindowTitle("Past Entries")




def window():
    app = QApplication(sys.argv)
    win = MoodApp()
    win.show()
    sys.exit(app.exec_())



class Display(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        

        self.canvas = Canvas() # Create a canvas
        
        # main_menu = self.menuBar()
        # file_menu = main_menu.addMenu("File")
        # saveAction = QtWidgets.QAction("Save", self)
        # saveAction.setShortcut("Ctrl + S")
        # file_menu.addAction(saveAction)
        # saveAction.triggered.connect(self.canvas.save_image)

        self.ui.DRAW_INPUT = QtWidgets.QWidget() # Create widget
        l = QtWidgets.QVBoxLayout() # Vertical box layout
        self.ui.DRAW_INPUT.setLayout(l)
        l.addWidget(self.canvas) # Add canvas to layout

        palette = QtWidgets.QHBoxLayout() # Horizontal box layout
        self.add_palette_buttons(palette) 
        l.addLayout(palette)

        # self.setCentralWidget(self.ui.DRAW_INPUT)






window()

