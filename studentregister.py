from PyQt5 import QtCore, QtGui, QtWidgets
from studentpanel import StudentPanel
from main_db import student_register_db
from studentlogin import StudentLoginPage


class StudentRegisterPage(object):
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
        self.registerbtn = QtWidgets.QPushButton(self.widget)
        self.registerbtn.setGeometry(QtCore.QRect(320, 390, 150, 40))
        self.registerbtn.setStyleSheet("QPushButton#registerbtn{\n"
        "    font: 10pt \"MS Shell Dlg 2\";    \n"
        "    color: rgb(49, 49, 49);\n"
        "    \n"
        "    background-color: rgb(229, 229, 229);\n"
        "    border-radius: 15px;\n"
        "}\n"
        "QPushButton#registerbtn:hover{\n"
        "    font: 12pt \"MS Shell Dlg 2\";    \n"
        "    color: rgb(49, 49, 49);\n"
        "}\n"
        "QPushButton#registerbtn:pressed{\n"
        "    font: 6pt \"MS Shell Dlg 2\";    \n"
        "    color: rgb(49, 49, 49);\n"
        "}")
        self.registerbtn.setObjectName("registerbtn")
        self.studentlabel = QtWidgets.QLabel(self.widget)
        self.studentlabel.setGeometry(QtCore.QRect(350, 50, 91, 41))
        self.studentlabel.setStyleSheet("color: rgb(49, 49, 49);\n"
        "font: 18pt \"MS Shell Dlg 2\";\n"
        "background-color: None\n"
        "")
        self.studentlabel.setObjectName("studentlabel")
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
        self.username = QtWidgets.QLineEdit(self.widget)
        self.username.setGeometry(QtCore.QRect(320, 120, 150, 30))
        self.username.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
        "border:none;\n"
        "border-bottom: 2px solid rgba(53, 53, 53, 200);\n"
        "color: rgba(0, 0, 0, 240);\n"
        "padding-bottom: 7px;\n"
        "\n"
        "")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setGeometry(QtCore.QRect(320, 320, 150, 30))
        self.password.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
        "border:none;\n"
        "border-bottom: 2px solid rgba(53, 53, 53, 200);\n"
        "color: rgba(0, 0, 0, 240);\n"
        "padding-bottom: 7px;\n"
        "\n"
        "")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.errortext = QtWidgets.QLabel(self.widget)
        self.errortext.setGeometry(QtCore.QRect(320, 270, 151, 16))
        self.errortext.setStyleSheet("color: rgb(204, 6, 0);\n"
        "background-color: None\n"
        "")
        self.errortext.setText("")
        self.errortext.setObjectName("errortext")
        self.firstname = QtWidgets.QLineEdit(self.widget)
        self.firstname.setGeometry(QtCore.QRect(320, 170, 150, 30))
        self.firstname.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
        "border:none;\n"
        "border-bottom: 2px solid rgba(53, 53, 53, 200);\n"
        "color: rgba(0, 0, 0, 240);\n"
        "padding-bottom: 7px;\n"
        "\n"
        "")
        self.firstname.setObjectName("firstname")
        self.lastname = QtWidgets.QLineEdit(self.widget)
        self.lastname.setGeometry(QtCore.QRect(320, 220, 150, 30))
        self.lastname.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
        "border:none;\n"
        "border-bottom: 2px solid rgba(53, 53, 53, 200);\n"
        "color: rgba(0, 0, 0, 240);\n"
        "padding-bottom: 7px;\n"
        "\n"
        "")
        self.lastname.setObjectName("lastname")
        self.prolanguage = QtWidgets.QLineEdit(self.widget)
        self.prolanguage.setGeometry(QtCore.QRect(320, 270, 150, 30))
        self.prolanguage.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
        "border:none;\n"
        "border-bottom: 2px solid rgba(53, 53, 53, 200);\n"
        "color: rgba(0, 0, 0, 240);\n"
        "padding-bottom: 7px;\n"
        "\n"
        "")
        self.prolanguage.setObjectName("prolanguage")
        self.errortext_2 = QtWidgets.QLabel(self.widget)
        self.errortext_2.setGeometry(QtCore.QRect(320, 360, 151, 16))
        self.errortext_2.setStyleSheet("color: rgb(204, 6, 0);\n"
        "background-color: None\n"
        "")
        self.errortext_2.setText("")
        self.errortext_2.setObjectName("errortext_2")
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
        self.registerbtn.setText(_translate("MainWindow", "register"))
        self.studentlabel.setText(_translate("MainWindow", "Student"))
        self.backbtn.setText(_translate("MainWindow", "back"))
        self.username.setPlaceholderText(_translate("MainWindow", "user name"))
        self.password.setPlaceholderText(_translate("MainWindow", "password"))
        self.firstname.setPlaceholderText(_translate("MainWindow", "first name"))
        self.lastname.setPlaceholderText(_translate("MainWindow", "last name"))
        self.prolanguage.setPlaceholderText(_translate("MainWindow", "programing language"))


        #student register - button --> def registerbutton line = 163
        self.registerbtn.clicked.connect(self.registerbutton)
        self.registerbtn.clicked.connect(MainWindow.close)
        
        
        #back - button --> def backbutton line = 185
        self.backbtn.clicked.connect(self.backbutton)
        self.backbtn.clicked.connect(MainWindow.close)


    #student_register_db (main_db.py import student_register_db)
    #button registerbtn --> line = 152
    def registerbutton(self, values):
        username = self.username.text()
        first_name = self.firstname.text()
        last_name = self.lastname.text()
        programing_language = self.prolanguage.text()
        password = self.password.text()
        if len(username) == 0 or len(password) == 0:
            self.MainWindow = QtWidgets.QMainWindow()
            self.ui = StudentRegisterPage()
            self.ui.setupUi (self.MainWindow)
            self.MainWindow.show()
        else:
            self.MainWindow = QtWidgets.QMainWindow()
            self.ui = StudentLoginPage()
            self.ui.setupUi (self.MainWindow)
            self.MainWindow.show()
            values = (username, first_name, last_name, programing_language, password)
            student_register_db(values)



    #button backbtn --> line = 157
    def backbutton(self):
        from studentfirst import StudentFirstPage
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = StudentFirstPage()
        self.ui.setupUi (self.MainWindow)
        self.MainWindow.show()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = StudentRegisterPage()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
