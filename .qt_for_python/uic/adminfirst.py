# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\HP\Desktop\Lessonpythonbase\lesson\projectpyqt5\designer\adminfirst.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.widget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(126, 126, 126, 255), stop:1 rgba(165, 165, 165, 255));")
        self.widget.setObjectName("widget")
        self.adminbtn = QtWidgets.QPushButton(self.widget)
        self.adminbtn.setGeometry(QtCore.QRect(320, 180, 150, 40))
        self.adminbtn.setStyleSheet("QPushButton#adminbtn{\n"
"    font: 10pt \"MS Shell Dlg 2\";    \n"
"    color: rgb(49, 49, 49);\n"
"    \n"
"    background-color: rgb(229, 229, 229);\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton#adminbtn:hover{\n"
"    font: 12pt \"MS Shell Dlg 2\";    \n"
"    color: rgb(49, 49, 49);\n"
"}\n"
"QPushButton#adminbtn:pressed{\n"
"    font: 6pt \"MS Shell Dlg 2\";    \n"
"    color: rgb(49, 49, 49);\n"
"}")
        self.adminbtn.setObjectName("adminbtn")
        self.studentbtn = QtWidgets.QPushButton(self.widget)
        self.studentbtn.setGeometry(QtCore.QRect(320, 250, 150, 40))
        self.studentbtn.setStyleSheet("QPushButton#studentbtn{\n"
"    font: 10pt \"MS Shell Dlg 2\";    \n"
"    color: rgb(49, 49, 490);\n"
"    \n"
"    background-color: rgb(229, 229, 229);\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton#studentbtn:hover{\n"
"    font: 12pt \"MS Shell Dlg 2\";    \n"
"    color: rgb(49, 49, 49);\n"
"}\n"
"QPushButton#studentbtn:pressed{\n"
"    font: 6pt \"MS Shell Dlg 2\";    \n"
"    color: rgb(49, 49, 49);\n"
"}")
        self.studentbtn.setObjectName("studentbtn")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(360, 120, 91, 41))
        self.label.setStyleSheet("color: rgb(49, 49, 49);\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: None\n"
"")
        self.label.setObjectName("label")
        self.backbtn = QtWidgets.QPushButton(self.widget)
        self.backbtn.setGeometry(QtCore.QRect(10, 10, 120, 30))
        self.backbtn.setStyleSheet("QPushButton#backbtn{\n"
"    font: 10pt \"MS Shell Dlg 2\";    \n"
"    color: rgb(49, 49, 49);\n"
"    \n"
"    background-color: rgb(229, 229, 229);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton#backbtn:hover{\n"
"    font: 12pt \"MS Shell Dlg 2\";    \n"
"    color: rgb(49, 49, 49);\n"
"}\n"
"QPushButton#backbtn:pressed{\n"
"    font: 6pt \"MS Shell Dlg 2\";    \n"
"    color: rgb(49, 49, 49);\n"
"}")
        self.backbtn.setObjectName("backbtn")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(325, 155, 141, 16))
        self.label_2.setStyleSheet("color: rgb(49, 49, 49);\n"
"background-color: None\n"
"")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.adminbtn.setText(_translate("MainWindow", "login"))
        self.studentbtn.setText(_translate("MainWindow", "register"))
        self.label.setText(_translate("MainWindow", "Admin"))
        self.backbtn.setText(_translate("MainWindow", "back"))
        self.label_2.setText(_translate("MainWindow", "login or create your account"))
