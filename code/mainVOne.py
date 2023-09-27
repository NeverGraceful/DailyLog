# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainVOne.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1058, 740)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SUBMIT = QtWidgets.QPushButton(self.centralwidget)
        self.SUBMIT.setGeometry(QtCore.QRect(450, 640, 141, 41))
        self.SUBMIT.setObjectName("SUBMIT")
        self.PAST_ENTRY = QtWidgets.QPushButton(self.centralwidget)
        self.PAST_ENTRY.setGeometry(QtCore.QRect(60, 560, 151, 101))
        self.PAST_ENTRY.setObjectName("PAST_ENTRY")
        self.AVATAR_BODY = QtWidgets.QLabel(self.centralwidget)
        self.AVATAR_BODY.setGeometry(QtCore.QRect(770, 90, 250, 500))
        self.AVATAR_BODY.setObjectName("AVATAR_BODY")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 171, 221))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.STREAK = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.STREAK.setFont(font)
        self.STREAK.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.STREAK.setObjectName("STREAK")
        self.verticalLayout.addWidget(self.STREAK)
        self.POINTS = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.POINTS.setFont(font)
        self.POINTS.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.POINTS.setObjectName("POINTS")
        self.verticalLayout.addWidget(self.POINTS)
        self.DRAW_INPUT = QtWidgets.QWidget(self.centralwidget)
        self.DRAW_INPUT.setGeometry(QtCore.QRect(290, 330, 451, 251))
        self.DRAW_INPUT.setObjectName("DRAW_INPUT")
        self.AVATAR_HAT = QtWidgets.QLabel(self.centralwidget)
        self.AVATAR_HAT.setGeometry(QtCore.QRect(770, 90, 250, 500))
        self.AVATAR_HAT.setObjectName("AVATAR_HAT")
        self.AVATAR_CLOTHES = QtWidgets.QLabel(self.centralwidget)
        self.AVATAR_CLOTHES.setGeometry(QtCore.QRect(770, 90, 250, 500))
        self.AVATAR_CLOTHES.setObjectName("AVATAR_CLOTHES")
        self.SHOP_BUTTON = QtWidgets.QPushButton(self.centralwidget)
        self.SHOP_BUTTON.setGeometry(QtCore.QRect(60, 460, 151, 101))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.SHOP_BUTTON.setFont(font)
        self.SHOP_BUTTON.setObjectName("SHOP_BUTTON")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(290, 40, 451, 281))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.CURRENT_DATE = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.CURRENT_DATE.setFont(font)
        self.CURRENT_DATE.setObjectName("CURRENT_DATE")
        self.verticalLayout_2.addWidget(self.CURRENT_DATE, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.TEXT_INPUT = QtWidgets.QPlainTextEdit(self.layoutWidget1)
        self.TEXT_INPUT.setObjectName("TEXT_INPUT")
        self.verticalLayout_2.addWidget(self.TEXT_INPUT)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1058, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SUBMIT.setText(_translate("MainWindow", "PushButton"))
        self.PAST_ENTRY.setText(_translate("MainWindow", "PushButton"))
        self.AVATAR_BODY.setText(_translate("MainWindow", " "))
        self.STREAK.setText(_translate("MainWindow", "Streak"))
        self.POINTS.setText(_translate("MainWindow", "Points:"))
        self.AVATAR_HAT.setText(_translate("MainWindow", " "))
        self.AVATAR_CLOTHES.setText(_translate("MainWindow", " "))
        self.SHOP_BUTTON.setText(_translate("MainWindow", "PushButton"))
        self.CURRENT_DATE.setText(_translate("MainWindow", "TextLabel"))