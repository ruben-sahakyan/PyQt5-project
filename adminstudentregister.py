from PyQt5 import QtCore, QtGui, QtWidgets
from main_db import student_register_db


class Admin_St_Register(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 500)
        MainWindow.setFixedSize(400, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 400, 500))
        self.widget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(126, 126, 126, 255), stop:1 rgba(165, 165, 165, 255));")
        self.widget.setObjectName("widget")
        self.registerbtn = QtWidgets.QPushButton(self.widget)
        self.registerbtn.setGeometry(QtCore.QRect(145, 370, 110, 30))
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
        self.studentlabel.setGeometry(QtCore.QRect(90, 50, 241, 41))
        self.studentlabel.setStyleSheet("color: rgb(49, 49, 49);\n"
        "font: 18pt \"MS Shell Dlg 2\";\n"
        "background-color: None\n"
        "")
        self.studentlabel.setObjectName("studentlabel")
        self.username = QtWidgets.QLineEdit(self.widget)
        self.username.setGeometry(QtCore.QRect(130, 110, 150, 30))
        self.username.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
        "border:none;\n"
        "border-bottom: 2px solid rgba(53, 53, 53, 200);\n"
        "color: rgba(0, 0, 0, 240);\n"
        "padding-bottom: 7px;\n"
        "\n"
        "")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setGeometry(QtCore.QRect(130, 310, 150, 30))
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
        self.firstname.setGeometry(QtCore.QRect(130, 160, 150, 30))
        self.firstname.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
        "border:none;\n"
        "border-bottom: 2px solid rgba(53, 53, 53, 200);\n"
        "color: rgba(0, 0, 0, 240);\n"
        "padding-bottom: 7px;\n"
        "\n"
        "")
        self.firstname.setObjectName("firstname")
        self.lastname = QtWidgets.QLineEdit(self.widget)
        self.lastname.setGeometry(QtCore.QRect(130, 210, 150, 30))
        self.lastname.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
        "border:none;\n"
        "border-bottom: 2px solid rgba(53, 53, 53, 200);\n"
        "color: rgba(0, 0, 0, 240);\n"
        "padding-bottom: 7px;\n"
        "\n"
        "")
        self.lastname.setObjectName("lastname")
        self.prolanguage = QtWidgets.QLineEdit(self.widget)
        self.prolanguage.setGeometry(QtCore.QRect(130, 260, 150, 30))
        self.prolanguage.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
        "border:none;\n"
        "border-bottom: 2px solid rgba(53, 53, 53, 200);\n"
        "color: rgba(0, 0, 0, 240);\n"
        "padding-bottom: 7px;\n"
        "\n"
        "")
        self.prolanguage.setObjectName("prolanguage")
        self.errortext_2 = QtWidgets.QLabel(self.widget)
        self.errortext_2.setGeometry(QtCore.QRect(130, 350, 151, 16))
        self.errortext_2.setStyleSheet("color: rgb(204, 6, 0);\n"
        "background-color: None\n"
        "")
        self.errortext_2.setText("")
        self.errortext_2.setObjectName("errortext_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
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
        self.studentlabel.setText(_translate("MainWindow", "Student register panel"))
        self.username.setPlaceholderText(_translate("MainWindow", "user name"))
        self.password.setPlaceholderText(_translate("MainWindow", "password"))
        self.firstname.setPlaceholderText(_translate("MainWindow", "first name"))
        self.lastname.setPlaceholderText(_translate("MainWindow", "last name"))
        self.prolanguage.setPlaceholderText(_translate("MainWindow", "programing language"))


        #new student register - button --> def register_btn line = 135
        self.registerbtn.clicked.connect(self.register_btn)

    #student_register_db (main_db.py import student_register_db)
    #button registerbtn --> line = 131
    def register_btn(self, values):
        username = self.username.text()
        first_name = self.firstname.text()
        last_name = self.lastname.text()
        programing_language = self.prolanguage.text()
        password = self.password.text()
        if len(username) == 0 or len(password) == 0:
            self.MainWindow = QtWidgets.QMainWindow()
            self.ui = Admin_St_Register()
            self.ui.setupUi (self.MainWindow)
            self.MainWindow.show()
        else:
            values = (username, first_name, last_name, programing_language, password)
            student_register_db(values)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Admin_St_Register()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
