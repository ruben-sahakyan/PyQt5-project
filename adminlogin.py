import imp
from PyQt5 import QtCore, QtGui, QtWidgets
from adminpanel import AdminPanel
from main_db import admin_dict


class AdminLoginPanel(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.widget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(126, 126, 126, 255), stop:1 rgba(165, 165, 165, 255));")
        self.widget.setObjectName("widget")
        self.loginbtn = QtWidgets.QPushButton(self.widget)
        self.loginbtn.setGeometry(QtCore.QRect(320, 300, 150, 40))
        self.loginbtn.setStyleSheet("QPushButton#loginbtn{\n"
        "    font: 10pt \"MS Shell Dlg 2\";    \n"
        "    color: rgb(49, 49, 49);\n"
        "    \n"
        "    background-color: rgb(229, 229, 229);\n"
        "    border-radius: 15px;\n"
        "}\n"
        "QPushButton#loginbtn:hover{\n"
        "    font: 12pt \"MS Shell Dlg 2\";    \n"
        "    color: rgb(49, 49, 49);\n"
        "}\n"
        "QPushButton#loginbtn:pressed{\n"
        "    font: 6pt \"MS Shell Dlg 2\";    \n"
        "    color: rgb(49, 49, 49);\n"
        "}")
        self.loginbtn.setObjectName("loginbtn")
        self.Adminlabel = QtWidgets.QLabel(self.widget)
        self.Adminlabel.setGeometry(QtCore.QRect(360, 80, 91, 41))
        self.Adminlabel.setStyleSheet("color: rgb(49, 49, 49);\n"
        "font: 18pt \"MS Shell Dlg 2\";\n"
        "background-color: None\n"
        "")
        self.Adminlabel.setObjectName("Adminlabel")
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
        self.username.setGeometry(QtCore.QRect(320, 160, 150, 30))
        self.username.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
        "border:none;\n"
        "border-bottom: 2px solid rgba(53, 53, 53, 200);\n"
        "color: rgba(0, 0, 0, 240);\n"
        "padding-bottom: 7px;\n"
        "\n"
        "")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setGeometry(QtCore.QRect(320, 220, 150, 30))
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
        self.Adminlabel.setText(_translate("MainWindow", "Admin"))
        self.backbtn.setText(_translate("MainWindow", "back"))
        self.username.setPlaceholderText(_translate("MainWindow", "user name"))
        self.password.setPlaceholderText(_translate("MainWindow", "password"))



        self.loginbtn.clicked.connect(self.loginbutton)
        self.loginbtn.clicked.connect(MainWindow.close)

        self.backbtn.clicked.connect(self.backbutton)
        self.backbtn.clicked.connect(MainWindow.close)



    def loginbutton(self):
        if admin_dict.get(self.username.text(), None) == self.password.text():
            self.MainWindow = QtWidgets.QMainWindow()
            self.ui = AdminPanel()
            self.ui.setupUi (self.MainWindow)
            self.MainWindow.show()
        else:
            self.MainWindow = QtWidgets.QMainWindow()
            self.ui = AdminLoginPanel()
            self.ui.setupUi (self.MainWindow)
            self.MainWindow.show()



    def backbutton(self):
        from adminfirst import AdminFirstPage
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = AdminFirstPage()
        self.ui.setupUi (self.MainWindow)
        self.MainWindow.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = AdminLoginPanel()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
