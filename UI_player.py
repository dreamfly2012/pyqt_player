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
        Form.setStyleSheet("")
        self.playbtn = QtWidgets.QPushButton(Form)
        self.playbtn.setGeometry(QtCore.QRect(90, 400, 31, 31))
        self.playbtn.setStyleSheet("#playbtn{\n"
"    border-radius:15px;\n"
"background-color:red;\n"
"    font: 10pt \"楷体\";\n"
"color:#fff;\n"
"}")
        self.playbtn.setObjectName("playbtn")
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(240, 400, 160, 19))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(20, 90, 131, 241))
        self.listView.setObjectName("listView")
        self.durantionSlider = QtWidgets.QSlider(Form)
        self.durantionSlider.setGeometry(QtCore.QRect(30, 360, 501, 19))
        self.durantionSlider.setOrientation(QtCore.Qt.Horizontal)
        self.durantionSlider.setObjectName("durantionSlider")
        self.prevbtn = QtWidgets.QPushButton(Form)
        self.prevbtn.setGeometry(QtCore.QRect(0, 400, 75, 23))
        self.prevbtn.setObjectName("prevbtn")
        self.nextbtn = QtWidgets.QPushButton(Form)
        self.nextbtn.setGeometry(QtCore.QRect(130, 400, 75, 23))
        self.nextbtn.setObjectName("nextbtn")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(200, 120, 361, 111))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        self.playbtn.clicked.connect(Form.play)
        self.horizontalSlider.valueChanged['int'].connect(Form.valuechanged)
        self.pushButton.clicked.connect(Form.fileopen)
        self.nextbtn.released.connect(Form.next)
        self.prevbtn.released.connect(Form.prev)
        self.durantionSlider.sliderMoved['int'].connect(Form.slidermoved)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "音乐播放器by梦回故里"))
        self.playbtn.setText(_translate("Form", "||"))
        self.pushButton.setText(_translate("Form", "添加文件+"))
        self.prevbtn.setText(_translate("Form", "<"))
        self.nextbtn.setText(_translate("Form", ">"))
        self.label.setText(_translate("Form", "歌词"))
