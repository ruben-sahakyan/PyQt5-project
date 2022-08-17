from PyQt5 import QtCore, QtGui, QtWidgets
from studentlogin import StudentLoginPage
from studentregister import StudentRegisterPage


class StudentFirstPage(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setFixedSize(800, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.widget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(126, 126, 126, 255), stop:1 rgba(165, 165, 165, 255));")
        self.widget.setObjectName("widget")
        self.loginbtn = QtWidgets.QPushButton(self.widget)
        self.loginbtn.setGeometry(QtCore.QRect(320, 180, 150, 40))
        self.loginbtn.setStyleSheet("QPushButton#adminbtn{\n"
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
        self.loginbtn.setObjectName("adminbtn")
        self.registerbtn = QtWidgets.QPushButton(self.widget)
        self.registerbtn.setGeometry(QtCore.QRect(320, 250, 150, 40))
        self.registerbtn.setStyleSheet("QPushButton#studentbtn{\n"
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
        self.registerbtn.setObjectName("studentbtn")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(350, 120, 91, 41))
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
        self.loginbtn.setText(_translate("MainWindow", "login"))
        self.registerbtn.setText(_translate("MainWindow", "register"))
        self.label.setText(_translate("MainWindow", "Student"))
        self.backbtn.setText(_translate("MainWindow", "back"))
        self.label_2.setText(_translate("MainWindow", "login or create your account"))


        self.loginbtn.clicked.connect(self.loginbutton)
        self.loginbtn.clicked.connect(MainWindow.close)


        self.registerbtn.clicked.connect(self.registerbutton)
        self.registerbtn.clicked.connect(MainWindow.close)


        self.backbtn.clicked.connect(self.backbutton)
        self.backbtn.clicked.connect(MainWindow.close)



    def loginbutton(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = StudentLoginPage()
        self.ui.setupUi (self.MainWindow)
        self.MainWindow.show()


    def registerbutton(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = StudentRegisterPage()
        self.ui.setupUi (self.MainWindow)
        self.MainWindow.show()


    def backbutton(self):
        from firstpage import FirstPage
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = FirstPage()
        self.ui.setupUi (self.MainWindow)
        self.MainWindow.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = StudentFirstPage()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
