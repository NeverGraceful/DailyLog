# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shop.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(518, 450)
        self.AVATAR_BODY = QtWidgets.QLabel(Dialog)
        self.AVATAR_BODY.setGeometry(QtCore.QRect(-10, 40, 211, 350))
        self.AVATAR_BODY.setObjectName("AVATAR_BODY")
        self.AVATAR_HAT = QtWidgets.QLabel(Dialog)
        self.AVATAR_HAT.setGeometry(QtCore.QRect(-10, 40, 211, 350))
        self.AVATAR_HAT.setObjectName("AVATAR_HAT")
        self.AVATAR_CLOTHES = QtWidgets.QLabel(Dialog)
        self.AVATAR_CLOTHES.setGeometry(QtCore.QRect(-10, 40, 211, 350))
        self.AVATAR_CLOTHES.setObjectName("AVATAR_CLOTHES")
        self.SHOP = QtWidgets.QWidget(Dialog)
        self.SHOP.setGeometry(QtCore.QRect(210, 40, 261, 351))
        self.SHOP.setObjectName("SHOP")
        self.SCROLL = QtWidgets.QWidget(Dialog)
        self.SCROLL.setGeometry(QtCore.QRect(480, 40, 21, 351))
        self.SCROLL.setObjectName("SCROLL")
        self.PRICE = QtWidgets.QLabel(Dialog)
        self.PRICE.setGeometry(QtCore.QRect(40, 400, 141, 31))
        self.PRICE.setText("")
        self.PRICE.setObjectName("PRICE")
        self.OWNED = QtWidgets.QLabel(Dialog)
        self.OWNED.setGeometry(QtCore.QRect(80, 10, 47, 41))
        self.OWNED.setText("")
        self.OWNED.setObjectName("OWNED")
        self.WEAR = QtWidgets.QPushButton(Dialog)
        self.WEAR.setGeometry(QtCore.QRect(260, 410, 151, 23))
        self.WEAR.setObjectName("WEAR")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.AVATAR_BODY.setText(_translate("Dialog", "TextLabel"))
        self.AVATAR_HAT.setText(_translate("Dialog", "TextLabel"))
        self.AVATAR_CLOTHES.setText(_translate("Dialog", "TextLabel"))
        self.WEAR.setText(_translate("Dialog", "PushButton"))
