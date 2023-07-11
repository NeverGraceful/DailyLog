from data_structuresBig import Mood_Entry, dictionary, drawing_dictionary
from drawBig import Canvas, COLORS, QPaletteButton
import sys, os
from PyQt5 import QtCore, QtWidgets, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QDialog
from mainVOne import Ui_MainWindow
from pastVOne import Ui_Dialog
from datetime import date
from pathlib import Path

class MoodApp(QtWidgets.QMainWindow):
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
        self.ui.DRAW_INPUT.setPixmap(self.canvas.pixmap().scaled(w,h,QtCore.Qt.KeepAspectRatio))

        # palette = QtWidgets.QHBoxLayout() # Horizontal box layout
        # self.add_palette_buttons(palette) 
        # l.addLayout(palette)

        self.ui.CURRENT_DATE.setText(date.today().strftime("%d/%m/%Y"))
        self.ui.SUBMIT.setText("Submit Entry")
        self.ui.PAST_ENTRY.setText("View past entrys")


    def submitted(self):
        #add to our hashmap
        today = date.today().strftime("%d/%m/%Y") # d1 = today.strftime("%d/%m/%Y") "dd/mm/YY"
        dictionary.update({today:self.ui.TEXT_INPUT.toPlainText()})
        self.canvas.save_image()


    def add_palette_buttons(self, layout):
        for c in COLORS:
            b = QPaletteButton(c)
            b.pressed.connect(lambda c=c: self.canvas.set_pen_color(c))
            layout.addWidget(b)

    def open_past_entries(self):
        box = PastWindow()
        box.exec_()
        

class PastWindow(QtWidgets.QDialog):
    def __init__(self):
        super(PastWindow, self).__init__()
        self.setWindowTitle("hahah")
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.RETURN.setText("Return")
        self.ui.RETURN.clicked.connect(self.close_past)
        self.ui.SAVE_PAST.setText("Save Drawing")
        self.ui.CALENDAR.clicked.connect(self.display_drawing)


    def display_drawing(self):
        selectedDate = self.ui.CALENDAR.selectedDate().toString("dd-MM-yyyy")
        print("KEY WE ARE TRYING " + selectedDate)
        wanted_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'pastDrawings') +"\\" + selectedDate + ".png"
        print("wanted path: " + wanted_path)
        self.im = QPixmap(wanted_path)
       # pixmap_resized = self.im.scaled(451, 2, QtCore.Qt.KeepAspectRatio)
        self.ui.PAST_DRAWING.setPixmap(self.im)
        self.show()
 
    def close_past(self):
        self.close()


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

