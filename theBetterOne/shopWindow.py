import sys, os
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QPushButton
import shop, dataStructures
import re
from pathlib import Path

class ShopWindow(QtWidgets.QDialog):
    def __init__(self):
        super(ShopWindow, self).__init__()
        self.ui = shop.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Shop')
        self.ui.WEAR.setText("Put this on!")
        self.load_info()
        print("Current hat: "+ str(self.ava_hat))
        self.setup_avatar()
        self.fill_shop()
        
    def setup_avatar(self):
        cur_path = Path(os.path.join(self.find_path(),'avatar'))
        pixmap = QPixmap(os.path.join(cur_path, "bodies" + "\\" + self.ava_body + '.png'))
        self.ui.AVATAR_BODY.setPixmap(pixmap)
        pixmap = QPixmap(os.path.join(cur_path, "hats" + "\\" + self.ava_hat + '.png'))
        self.ui.AVATAR_HAT.setPixmap(pixmap)
        pixmap = QPixmap(os.path.join(cur_path, "clothes" + "\\" + self.ava_clothes + '.png'))
        self.ui.AVATAR_CLOTHES.setPixmap(pixmap)

    def fill_shop(self):
        self.ui.SCROLL = QtWidgets.QScrollArea(self)
        self.vbox = QtWidgets.QGridLayout()
        
        #get num of total shop items
        for custom in dataStructures.customize:
            dir_path = os.path.join(self.find_path(),'avatar') +"\\" + custom
            count = 0
            for path in os.listdir(dir_path):
                if os.path.isfile(os.path.join(dir_path, path)):
                    count += 1
            
            if custom == "bodies":
                array = dataStructures.bodies
            elif custom == "hats":
                array = dataStructures.hats
            else:
                array = dataStructures.clothes
            
            for cur_thingy in array:
                cur_thingy_path =  dir_path + cur_thingy
                #TODO: include spaces 
                button = QPushButton(cur_thingy)
                button.clicked.connect(self.get_item)
                self.vbox.addWidget(button)
                
        self.ui.SHOP.setLayout(self.vbox)

        self.ui.SCROLL.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ui.SCROLL.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.SCROLL.setWidgetResizable(True)
        self.ui.SCROLL.setWidget(self.ui.SHOP)
        self.ui.SCROLL.setGeometry(210, 40, 261, 351)

    def get_item(self):
        #show the price somewhere
        #see if the user can buy it 
        #maybe user can try it on????/ idk
        current_thingy = self.sender().text()
        if current_thingy in dataStructures.hats:
            self.try_on("hats", current_thingy)
            self.selected_item = current_thingy
        elif current_thingy in dataStructures.clothes:
            self.try_on("clothes", current_thingy)
            self.selected_item = current_thingy
        else:
            self.try_on("bodies", current_thingy)
            self.selected_item = current_thingy
        #get rid of space here?????
        
    def try_on(self, shop_type, current_thingy):
        cur_path = cur_path = Path(os.path.join(self.find_path(),'avatar'))
        pixmap = QPixmap(os.path.join(cur_path, shop_type + "\\" + str(current_thingy) + '.png'))
        if shop_type == "hats":
            self.ui.AVATAR_HAT.setPixmap(pixmap)
            self.ui.AVATAR_BODY.setPixmap(QPixmap(os.path.join(cur_path, "bodies" + "\\" + self.ava_body + '.png')))
            self.ui.AVATAR_CLOTHES.setPixmap(QPixmap(os.path.join(cur_path, "clothes" + "\\" + self.ava_clothes + '.png')))
        elif shop_type == "clothes":
            self.ui.AVATAR_CLOTHES.setPixmap(pixmap)
            self.ui.AVATAR_BODY.setPixmap(QPixmap(os.path.join(cur_path, "bodies" + "\\" + self.ava_body + '.png')))
            self.ui.AVATAR_HAT.setPixmap(QPixmap(os.path.join(cur_path, "hats" + "\\" + self.ava_hat + '.png')))
        else:
            self.ui.AVATAR_BODY.setPixmap(pixmap)
            self.ui.AVATAR_CLOTHES.setPixmap(QPixmap(os.path.join(cur_path, "clothes" + "\\" + self.ava_clothes + '.png')))
            self.ui.AVATAR_HAT.setPixmap(QPixmap(os.path.join(cur_path, "hats" + "\\" + self.ava_hat + '.png')))

    def wear(self):
        #only can do if streak is high enough!
        if self.selected_item is None:
            print("idk do nothing.")
        elif self.selected_item in dataStructures.hats:
            self.ava_hat = str(self.selected_item)
        elif self.selected_item in dataStructures.clothes:
            self.ava_clothes = str(self.selected_item)
        else:
            self.ava_body = str(self.selected_item)



    def load_info(self):
        wanted_path = os.path.join(self.find_path(),'info.txt')
        with open(wanted_path) as info_file:
            for line in info_file:
                list = (re.split(':|\n', line))
                print(list)
                match list[0]:
                    case "ava_hat":
                        self.ava_hat = list[1]
                    case "ava_body":
                        self.ava_body = list[1]
                    case "ava_clothes":
                        self.ava_clothes = list[1]
                    case "streak":
                        self.streak = list[1]
        info_file.close()
    
    def find_path(self):
        print(os.path.dirname(sys.executable))
        application_path = 0
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        else:
            application_path = os.path.dirname(os.path.abspath(__file__))

        return application_path
