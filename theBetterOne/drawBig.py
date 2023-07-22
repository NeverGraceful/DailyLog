import os,sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
from datetime import date
from pathlib import Path

class Canvas(QtWidgets.QLabel):
     
    def __init__(self):
        super().__init__()
        pixmap = QtGui.QPixmap(451, 200)
        
        pixmap.fill(Qt.white)
        self.setPixmap(pixmap)
        

        self.last_x, self.last_y = None, None
        self.pen_color = QtGui.QColor('#000000')

    def set_pen_color(self, c):
        self.pen_color = QtGui.QColor(c)

    def mouseMoveEvent(self, e):
        if self.last_x is None: #first event
           self.last_x = e.x()
           self.last_y = e.y()
           return # ignore the first time   

        painter = QtGui.QPainter(self.pixmap())
        p = painter.pen()
        if (self.pen_color.name() == '#ffffff'):
            p.setWidth(8)
        else:
            p.setWidth(4)
        
        p.setColor(self.pen_color)
        painter.setPen(p)
        painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
        painter.end()
        self.update()

        #update the origin fo next time
        self.last_x = e.x()
        self.last_y = e.y()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None

    def save_image(self): #C:\Users\ajime\OneDrive\Desktop\Code\Summer\SummerProj\pastDrawings
        dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),'pastDrawings')
        today = date.today().strftime("%m-%d-%Y")
        new_file = dir +"\\" + today +".png"
        self.pixmap().save(new_file)
    

COLORS = ['#000000', '#FA8072', '#008080', '#FFFFFF']


class QPaletteButton(QtWidgets.QPushButton):

    def __init__(self, color):
        super().__init__()
        self.setFixedSize(QtCore.QSize(24,24))
        self.color = color
        self.setStyleSheet("background-color: %s;" % color)

