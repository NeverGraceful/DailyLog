import sys, os
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
import pastVOne
import shutil

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