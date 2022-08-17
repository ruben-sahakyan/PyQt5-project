from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem
from main_db import student_login, student_tasks, student_task_sh, del_task, change_task
from adminstudentregister import Admin_St_Register


class AdminPanel(object):
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
        self.adminlabel = QtWidgets.QLabel(self.widget)
        self.adminlabel.setGeometry(QtCore.QRect(330, 10, 130, 30))
        self.adminlabel.setStyleSheet("color: rgb(49, 49, 49);\n"
        "font: 18pt \"MS Shell Dlg 2\";\n"
        "background-color: None\n"
        "")
        self.adminlabel.setObjectName("adminlabel")
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
        self.username.setGeometry(QtCore.QRect(30, 80, 150, 30))
        self.username.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
        "border:none;\n"
        "border-bottom: 2px solid rgba(53, 53, 53, 200);\n"
        "color: rgba(0, 0, 0, 240);\n"
        "padding-bottom: 7px;\n"
        "\n"
        "")
        self.username.setObjectName("username")
        self.errortext = QtWidgets.QLabel(self.widget)
        self.errortext.setGeometry(QtCore.QRect(320, 270, 151, 16))
        self.errortext.setStyleSheet("color: rgb(204, 6, 0);\n"
        "background-color: None\n"
        "")
        self.errortext.setText("")
        self.errortext.setObjectName("errortext")
        self.titletxt = QtWidgets.QLineEdit(self.widget)
        self.titletxt.setGeometry(QtCore.QRect(30, 120, 150, 30))
        self.titletxt.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
        "border:none;\n"
        "border-bottom: 2px solid rgba(53, 53, 53, 200);\n"
        "color: rgba(0, 0, 0, 240);\n"
        "padding-bottom: 7px;\n"
        "\n"
        "")
        self.titletxt.setObjectName("titletxt")
        self.contenttxt = QtWidgets.QTextEdit(self.widget)
        self.contenttxt.setGeometry(QtCore.QRect(20, 160, 361, 241))
        self.contenttxt.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
        "border-radius: 8px;\n"
        "border:none;\n"
        "border: 2px solid rgba(53, 53, 53, 200);\n"
        "color: rgba(0, 0, 0, 240);\n"
        "padding-bottom: 7px;")
        self.contenttxt.setObjectName("contenttxt")
        self.deletetaskbtn = QtWidgets.QPushButton(self.widget)
        self.deletetaskbtn.setGeometry(QtCore.QRect(220, 410, 111, 31))
        self.deletetaskbtn.setStyleSheet("QPushButton#deletetaskbtn{\n"
        "    font: 8pt \"MS Shell Dlg 2\";    \n"
        "    color: rgb(49, 49, 49);\n"
        "    border: 2px solid rgba(53, 53, 53, 200);\n"
        "    color: rgba(0, 0, 0, 240);\n"
        "    padding-bottom: 7px;\n"
        "    \n"
        "    background-color: rgb(229, 229, 229);\n"
        "    border-radius: 10px;\n"
        "}\n"
        "QPushButton#deletetaskbtn:hover{\n"
        "    font: 10pt \"MS Shell Dlg 2\";    \n"
        "    color: rgb(49, 49, 49);\n"
        "}\n"
        "QPushButton#deletetaskbtn:pressed{\n"
        "    font: 6pt \"MS Shell Dlg 2\";    \n"
        "    color: rgb(49, 49, 49);\n"
        "}")
        self.deletetaskbtn.setObjectName("deletetaskbtn")
        self.taskslist = QtWidgets.QListWidget(self.widget)
        self.taskslist.setGeometry(QtCore.QRect(640, 70, 141, 331))
        self.taskslist.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
        "border-radius: 8px;\n"
        "border:none;\n"
        "border: 2px solid rgba(53, 53, 53, 200);\n"
        "color: rgba(0, 0, 0, 240);\n"
        "padding-bottom: 7px;")
        self.taskslist.setObjectName("taskslist")
        self.studentslist = QtWidgets.QListWidget(self.widget)
        self.studentslist.setGeometry(QtCore.QRect(490, 70, 141, 331))
        self.studentslist.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
        "border-radius: 8px;\n"
        "border:none;\n"
        "border: 2px solid rgba(53, 53, 53, 200);\n"
        "color: rgba(0, 0, 0, 240);\n"
        "padding-bottom: 7px;")
        self.studentslist.setObjectName("studentslist")
        self.strefreshbtn = QtWidgets.QPushButton(self.widget)
        self.strefreshbtn.setGeometry(QtCore.QRect(505, 410, 111, 31))
        self.strefreshbtn.setStyleSheet("QPushButton#strefreshbtn{\n"
        "    font: 8pt \"MS Shell Dlg 2\";    \n"
        "    color: rgb(49, 49, 49);\n"
        "    border: 2px solid rgba(53, 53, 53, 200);\n"
        "    color: rgba(0, 0, 0, 240);\n"
        "    padding-bottom: 7px;\n"
        "    \n"
        "    background-color: rgb(229, 229, 229);\n"
        "    border-radius: 10px;\n"
        "}\n"
        "QPushButton#strefreshbtn:hover{\n"
        "    font: 10pt \"MS Shell Dlg 2\";    \n"
        "    color: rgb(49, 49, 49);\n"
        "}\n"
        "QPushButton#strefreshbtn:pressed{\n"
        "    font: 6pt \"MS Shell Dlg 2\";    \n"
        "    color: rgb(49, 49, 49);\n"
        "}")
        self.strefreshbtn.setObjectName("strefreshbtn")
        self.taskrefreshbtn = QtWidgets.QPushButton(self.widget)
        self.taskrefreshbtn.setGeometry(QtCore.QRect(655, 410, 111, 31))
        self.taskrefreshbtn.setStyleSheet("QPushButton#taskrefreshbtn{\n"
        "    font: 8pt \"MS Shell Dlg 2\";    \n"
        "    color: rgb(49, 49, 49);\n"
        "    border: 2px solid rgba(53, 53, 53, 200);\n"
        "    color: rgba(0, 0, 0, 240);\n"
        "    padding-bottom: 7px;\n"
        "    \n"
        "    background-color: rgb(229, 229, 229);\n"
        "    border-radius: 10px;\n"
        "}\n"
        "QPushButton#taskrefreshbtn:hover{\n"
        "    font: 10pt \"MS Shell Dlg 2\";    \n"
        "    color: rgb(49, 49, 49);\n"
        "}\n"
        "QPushButton#taskrefreshbtn:pressed{\n"
        "    font: 6pt \"MS Shell Dlg 2\";    \n"
        "    color: rgb(49, 49, 49);\n"
        "}")
        self.taskrefreshbtn.setObjectName("taskrefreshbtn")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(525, 40, 61, 21))
        self.label.setStyleSheet("color: rgb(49, 49, 49);\n"
        "font: 12pt \"MS Shell Dlg 2\";\n"
        "background-color: None")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(680, 40, 41, 21))
        self.label_2.setStyleSheet("color: rgb(49, 49, 49);\n"
        "font: 12pt \"MS Shell Dlg 2\";\n"
        "background-color: None")
        self.label_2.setObjectName("label_2")
        self.changetaskbtn = QtWidgets.QPushButton(self.widget)
        self.changetaskbtn.setGeometry(QtCore.QRect(60, 410, 111, 31))
        self.changetaskbtn.setStyleSheet("QPushButton#changetaskbtn{\n"
        "    font: 8pt \"MS Shell Dlg 2\";    \n"
        "    color: rgb(49, 49, 49);\n"
        "    border: 2px solid rgba(53, 53, 53, 200);\n"
        "    color: rgba(0, 0, 0, 240);\n"
        "    padding-bottom: 7px;\n"
        "    \n"
        "    background-color: rgb(229, 229, 229);\n"
        "    border-radius: 10px;\n"
        "}\n"
        "QPushButton#changetaskbtn:hover{\n"
        "    font: 10pt \"MS Shell Dlg 2\";    \n"
        "    color: rgb(49, 49, 49);\n"
        "}\n"
        "QPushButton#changetaskbtn:pressed{\n"
        "    font: 6pt \"MS Shell Dlg 2\";    \n"
        "    color: rgb(49, 49, 49);\n"
        "}")
        self.changetaskbtn.setObjectName("changetaskbtn")
        self.taskdone = QtWidgets.QLineEdit(self.widget)
        self.taskdone.setGeometry(QtCore.QRect(220, 80, 150, 30))
        self.taskdone.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
        "border:none;\n"
        "border-bottom: 2px solid rgba(53, 53, 53, 200);\n"
        "color: rgba(0, 0, 0, 240);\n"
        "padding-bottom: 7px;\n"
        "\n"
        "")
        self.taskdone.setObjectName("taskdone")
        self.assessment = QtWidgets.QLineEdit(self.widget)
        self.assessment.setGeometry(QtCore.QRect(220, 120, 150, 30))
        self.assessment.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
        "border:none;\n"
        "border-bottom: 2px solid rgba(53, 53, 53, 200);\n"
        "color: rgba(0, 0, 0, 240);\n"
        "padding-bottom: 7px;\n"
        "\n"
        "")
        self.assessment.setObjectName("assessment")
        self.addstbtn = QtWidgets.QPushButton(self.widget)
        self.addstbtn.setGeometry(QtCore.QRect(150, 10, 120, 30))
        self.addstbtn.setStyleSheet("QPushButton#addstbtn{\n"
        "    font: 8pt \"MS Shell Dlg 2\";    \n"
        "    color: rgb(49, 49, 49);\n"
        "    \n"
        "    background-color: rgb(229, 229, 229);\n"
        "    border-radius: 10px;\n"
        "}\n"
        "QPushButton#addstbtn:hover{\n"
        "    font: 10pt \"MS Shell Dlg 2\";    \n"
        "    color: rgb(49, 49, 49);\n"
        "}\n"
        "QPushButton#addstbtn:pressed{\n"
        "    font: 6pt \"MS Shell Dlg 2\";    \n"
        "    color: rgb(49, 49, 49);\n"
        "}")
        self.addstbtn.setObjectName("addstbtn")
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
        self.adminlabel.setText(_translate("MainWindow", "Admin panel"))
        self.backbtn.setText(_translate("MainWindow", "back"))
        self.username.setPlaceholderText(_translate("MainWindow", "user name"))
        self.titletxt.setPlaceholderText(_translate("MainWindow", "title"))
        self.contenttxt.setPlaceholderText(_translate("MainWindow", "content"))
        self.deletetaskbtn.setText(_translate("MainWindow", "delete"))
        self.strefreshbtn.setText(_translate("MainWindow", "refresh"))
        self.taskrefreshbtn.setText(_translate("MainWindow", "refresh"))
        self.label.setText(_translate("MainWindow", "Students"))
        self.label_2.setText(_translate("MainWindow", "Tasks"))
        self.changetaskbtn.setText(_translate("MainWindow", "change"))
        self.taskdone.setPlaceholderText(_translate("MainWindow", "task done"))
        self.assessment.setPlaceholderText(_translate("MainWindow", "assessment"))
        self.addstbtn.setText(_translate("MainWindow", "add student"))

        #back-button --> def backbutton line = 347
        self.backbtn.clicked.connect(self.backbutton)
        self.backbtn.clicked.connect(MainWindow.close)

        #change task - button --> def change_task_btn  line = 327
        self.changetaskbtn.clicked.connect(self.change_task_btn)

        #student list refresh -button --> def student_refresh_btn line = 284
        self.strefreshbtn.clicked.connect(self.student_refresh_btn)

        #tasks list refresh - button --> def task_refresh_btn  line = 318
        self.taskrefreshbtn.clicked.connect(self.task_refresh_btn)

        #delete task - button --> def delete_task_btn line = 339
        self.deletetaskbtn.clicked.connect(self.delete_task_btn)

        #add student - button --> def add_student_btn line = 357
        self.addstbtn.clicked.connect(self.add_student_btn)

    #st_lst (main_db.py def student_login)
    #st_lst (main_db.py import st_lst)
    #button strefreshbtn --> line = 270
    def student_refresh_btn(self):
        st_lst = student_login()
        self.studentslist.clear()
        student_login()
        for i in st_lst:
            self.studentslist.addItem(i[0])
        self.studentslist.itemDoubleClicked.connect(self.student_tasks_btn)



    #Double clicked - button --> line = 290
    def student_tasks_btn(self, item):
        self.taskslist.clear()
        self.current_user = item
        st_tasks = student_tasks(self.current_user.data(0))
        for it in st_tasks:
            self.taskslist.addItem(it[1])
        self.taskslist.itemDoubleClicked.connect(self.show_sts_task)



    #Double clicked - button --> line = 301
    def show_sts_task(self, item):
        self.current_tasks = item
        one_task_student = student_task_sh(self.current_user.data(0), self.current_tasks.data(0))
        self.titletxt.setText(one_task_student[0][1])
        self.contenttxt.setText(one_task_student[0][4])
        self.assessment.setText(one_task_student[0][3])
        self.taskdone.setText(one_task_student[0][2])
        self.username.setText(one_task_student[0][5])

    #st_tasks (main_db.py def student_tasks)
    #st_tasks (main_db.py import st_tasks)
    #tasks list refresh - button --> line = 273
    def task_refresh_btn(self):
        self.taskslist.clear()
        st_tasks = student_tasks(self.current_user.data(0))
        for i in st_tasks:
            self.taskslist.addItem(i[1])



    #change student task - button --> line = 267
    def change_task_btn(self):
        username = self.username.text()
        titletxt = self.titletxt.text()
        taskdone = self.taskdone.text()
        assessment = self.assessment.text()
        contenttxt = self.contenttxt.toPlainText()
        values = (titletxt, taskdone, assessment, contenttxt, username, username, titletxt)
        change_task(values)



    # delete student task - button --> line = 276
    def delete_task_btn(self):
        username = self.current_user.data(0)
        title = self.current_tasks.data(0)
        del_task(title, username)



    #button backbtn --> line = 263
    def backbutton(self):
        from adminlogin import AdminLoginPanel
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = AdminLoginPanel()
        self.ui.setupUi (self.MainWindow)
        self.MainWindow.show()



    #admin add new student - button --> line = 279
    def add_student_btn(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Admin_St_Register()
        self.ui.setupUi (self.MainWindow)
        self.MainWindow.show()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = AdminPanel()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
