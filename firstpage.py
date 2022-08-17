from PyQt5 import QtCore, QtGui, QtWidgets
from adminfirst import AdminFirstPage
from studentfirst import StudentFirstPage


class FirstPage(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 801, 481))
        self.widget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(126, 126, 126, 255), stop:1 rgba(165, 165, 165, 255));")
        self.widget.setObjectName("widget")
        self.adminbtn = QtWidgets.QPushButton(self.widget)
        self.adminbtn.setGeometry(QtCore.QRect(320, 180, 150, 40))
        self.adminbtn.setStyleSheet("QPushButton#adminbtn{\n"
        "    font: 10pt \"MS Shell Dlg 2\";    \n"
        "    color: rgb(49, 49, 490);\n"
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
        self.adminbtn.setText(_translate("MainWindow", "Admin"))
        self.studentbtn.setText(_translate("MainWindow", "Student"))

        #admin-button --> def adminbutton line = 80
        self.adminbtn.clicked.connect(self.adminbutton)
        self.adminbtn.clicked.connect(MainWindow.close)

        #student-button --> def studentbutton line = 88
        self.studentbtn.clicked.connect(self.studentbutton)
        self.studentbtn.clicked.connect(MainWindow.close)


    #button adminbtn --> line = 71
    def adminbutton(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = AdminFirstPage()
        self.ui.setupUi (self.MainWindow)
        self.MainWindow.show()


    #button studentbtn --> line = 75
    def studentbutton(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = StudentFirstPage()
        self.ui.setupUi (self.MainWindow)
        self.MainWindow.show()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = FirstPage()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
