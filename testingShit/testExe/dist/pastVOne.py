# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pastVOne.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(891, 754)
        self.CALENDAR = QtWidgets.QCalendarWidget(Dialog)
        self.CALENDAR.setGeometry(QtCore.QRect(20, 20, 312, 183))
        self.CALENDAR.setObjectName("CALENDAR")
        self.DATE_DISPLAYED = QtWidgets.QLabel(Dialog)
        self.DATE_DISPLAYED.setGeometry(QtCore.QRect(70, 230, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.DATE_DISPLAYED.setFont(font)
        self.DATE_DISPLAYED.setText("")
        self.DATE_DISPLAYED.setAlignment(QtCore.Qt.AlignCenter)
        self.DATE_DISPLAYED.setObjectName("DATE_DISPLAYED")
        self.RETURN = QtWidgets.QPushButton(Dialog)
        self.RETURN.setGeometry(QtCore.QRect(40, 640, 141, 81))
        self.RETURN.setObjectName("RETURN")
        self.PAST_TEXT = QtWidgets.QLabel(Dialog)
        self.PAST_TEXT.setGeometry(QtCore.QRect(370, 40, 451, 251))
        self.PAST_TEXT.setFrameShape(QtWidgets.QFrame.Box)
        self.PAST_TEXT.setAlignment(QtCore.Qt.AlignCenter)
        self.PAST_TEXT.setWordWrap(True)
        self.PAST_TEXT.setObjectName("PAST_TEXT")
        self.SAVE_DRAWING = QtWidgets.QPushButton(Dialog)
        self.SAVE_DRAWING.setGeometry(QtCore.QRect(460, 640, 241, 31))
        self.SAVE_DRAWING.setObjectName("SAVE_DRAWING")
        self.PAST_DRAWING = QtWidgets.QLabel(Dialog)
        self.PAST_DRAWING.setGeometry(QtCore.QRect(370, 300, 451, 261))
        self.PAST_DRAWING.setObjectName("PAST_DRAWING")
        self.SAVE_TEXT = QtWidgets.QPushButton(Dialog)
        self.SAVE_TEXT.setGeometry(QtCore.QRect(460, 670, 241, 31))
        self.SAVE_TEXT.setObjectName("SAVE_TEXT")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.RETURN.setText(_translate("Dialog", "PushButton"))
        self.PAST_TEXT.setText(_translate("Dialog", "TextLabel"))
        self.SAVE_DRAWING.setText(_translate("Dialog", "PushButton"))
        self.PAST_DRAWING.setText(_translate("Dialog", "TextLabel"))
        self.SAVE_TEXT.setText(_translate("Dialog", "PushButton"))