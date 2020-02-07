# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\code\remotework\pyqt_player\player.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(587, 447)
        self.playbtn = QtWidgets.QPushButton(Form)
        self.playbtn.setGeometry(QtCore.QRect(10, 400, 75, 23))
        self.playbtn.setObjectName("playbtn")
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(170, 400, 160, 19))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(220, 170, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        self.playbtn.clicked.connect(Form.play)
        self.horizontalSlider.valueChanged['int'].connect(Form.valuechanged)
        self.pushButton.clicked.connect(Form.fileopen)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "音乐播放器by梦回故里"))
        self.playbtn.setText(_translate("Form", "播放"))
        self.pushButton.setText(_translate("Form", "添加文件+"))
