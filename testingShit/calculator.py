# import sys
# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QApplication, QMainWindow
# from PyQt5.QtGui import QIcon

# class calcWin(QMainWindow):
#     def __init__(self):
#         super(calcWin, self).__init__()
#         self.setGeometry(1200, 300, 700, 700)
#         self.setWindowTitle("Calculator OwO")
#         self.sol = "0"
#         self.prev_button = 'y';
#         self.init_UI()
    
#     def init_UI(self):
        
#         self.result = QtWidgets.QLabel(self)
#         self.result.setText('RESULT: ')
#         self.result.move(50, 50)
        
#         self.but_one = QtWidgets.QPushButton(self)
#         self.but_one.setText('1')
#         self.but_one.clicked.connect(self.clickedUwU('1'))
#         self.but_one.move(200, 130)  

#         self.but_two = QtWidgets.QPushButton(self)
#         self.but_two.setText('2')
#         self.but_two.clicked.connect(self.clickedUwU, '2')
#         self.but_two.move(250, 130)  

#         self.but_three = QtWidgets.QPushButton(self)
#         self.but_three.setText('3')
#         self.but_three.clicked.connect(self.clickedUwU, '3')
#         self.but_three.move(300, 130)  

#         self.but_four = QtWidgets.QPushButton(self)
#         self.but_four.setText('4')
#         self.but_four.clicked.connect(self.clickedUwU, '4')
#         self.but_four.move(350, 130)  

#         self.but_five = QtWidgets.QPushButton(self)
#         self.but_five.setText('5')
#         self.but_five.clicked.connect(self.clickedUwU, '5')
#         self.but_five.move(400, 130)  

#         self.but_six = QtWidgets.QPushButton(self)
#         self.but_six.setText('6')
#         self.but_six.clicked.connect(self.clickedUwU, '6')
#         self.but_six.move(450, 130)  

#         self.but_seven = QtWidgets.QPushButton(self)
#         self.but_seven.setText('7')
#         self.but_seven.clicked.connect(self.clickedUwU, '7')
#         self.but_seven.move(500, 130)  

#         self.but_eight = QtWidgets.QPushButton(self)
#         self.but_eight.setText('8')
#         self.but_eight.clicked.connect(self.clickedUwU, '8')
#         self.but_eight.move(550, 130)  

#         self.but_nine = QtWidgets.QPushButton(self)
#         self.but_nine.setText('9')
#         self.but_nine.clicked.connect(self.clickedUwU, '9')
#         self.but_nine.move(600, 130)  

#         self.but_zero = QtWidgets.QPushButton(self)
#         self.but_zero.setText('0')
#         self.but_zero.clicked.connect(self.clickedUwU, '0')
#         self.but_zero.move(650, 130)  

#         self.but_subtract = QtWidgets.QPushButton(self)
#         self.but_subtract.setText('-')
#         self.but_subtract.clicked.connect(self.clickedUwU, '-')
#         self.but_subtract.move(200, 230) 

#         self.but_plus = QtWidgets.QPushButton(self)
#         self.but_plus.setText('+')
#         self.but_plus.clicked.connect(self.clickedUwU, '+')
#         self.but_plus.move(250, 230)  

#         self.but_equals = QtWidgets.QPushButton(self)
#         self.but_equals.setText('+')
#         self.but_equals.clicked.connect(self.clickedUwU('='))
#         self.but_equals.move(250, 230)

#         self.but_clear = QtWidgets.QPushButton(self)
#         self.but_clear.setText('c')
#         self.but_clear.clicked.connect(self.clickedUwU('c'))
#         self.but_clear.move(250, 230)

#     def clickedUwU(self, symbol): # 3 + 4 = 7, "3" + "4" = 34
#         if (self.prev_button == "-" or self.prev_button == "+" or self.prev_button == "c") and (symbol == "-" or symbol == "+" or symbol == "c"):
#             #incorrect input, say so and disregard wha the user just put in
#             print("INCORRECT INPUT\n")
        
#         elif self.sol == 0:
#             self.sol = symbol

#         else:
#             #appending here, making one of the numbers
#             self.sol += symbol

            
       
# def window():
#     app = QApplication(sys.argv)
#     win = calcWin()
#     win.show()
#     sys.exit(app.exec_())


# window()