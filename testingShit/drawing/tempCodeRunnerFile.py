import os,sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt


class Canvas(QtWidgets.QLabel):
     
    def __init__(self):
        super().__init__()
        pixmap = QtGui.QPixmap(600, 300)
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

    def save_image(self):
        file_path, _=  QtWidgets.QFileDialog.getSaveFileName(self, "Save Image", "",
                         "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")
        

        if file_path  == "":
            return

        # toImage() const
        # p = self.pixmap.toImage()
        self.pixmap().save(file_path)

    

COLORS = ['#000000', '#FA8072', '#008080', '#FFFFFF']


class QPaletteButton(QtWidgets.QPushButton):

    def __init__(self, color):
        super().__init__()
        self.setFixedSize(QtCore.QSize(24,24))
        self.color = color
        self.setStyleSheet("background-color: %s;" % color)

# class PicButton(QtWidgets.QAbstractButton):
#     def __init__(self, pixmap, parent=None):
#         super(PicButton, self).__init__(parent)
#         self.pixmap = pixmap

#     def paintEvent(self, event):
#         painter = QtGui.QPainter(self)
#         painter.drawPixmap(event.rect(), self.pixmap)

#     def sizeHint(self):
#         return self.pixmap.size()
    
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        

        self.canvas = Canvas() # Create a canvas
        main_menu = self.menuBar()
        file_menu = main_menu.addMenu("File")
        saveAction = QtWidgets.QAction("Save", self)
        saveAction.setShortcut("Ctrl + S")
        file_menu.addAction(saveAction)
        saveAction.triggered.connect(self.canvas.save_image)

        w = QtWidgets.QWidget() # Create widget
        l = QtWidgets.QVBoxLayout() # Vertical box layout
        w.setLayout(l)
        l.addWidget(self.canvas) # Add canvas to layout

        palette = QtWidgets.QHBoxLayout() # Horizontal box layout
        self.add_palette_buttons(palette) 
        l.addLayout(palette)

        self.setCentralWidget(w)

    def add_palette_buttons(self, layout):
        for c in COLORS:
            b = QPaletteButton(c)
            b.pressed.connect(lambda c=c: self.canvas.set_pen_color(c))
            layout.addWidget(b)
    
    # def save_image(self):
    #     file_path, _=  QtWidgets.QFileDialog.getSaveFileName(self, "Save Image", "",
    #                      "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")
        

    #     if file_path  == "":
    #         return

    #     # toImage() const
    #     # p = self.pixmap.toImage()
    #     self.pixmap().save(file_path)

        # picPath = os.getcwd() + "C:\somedirectory\image.png"
        # print (picPath)
        # picMap = QtGui.QPixmap(picPath) 
    



app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()