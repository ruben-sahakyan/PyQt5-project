from PyQt5 import QtCore, QtGui, QtWidgets
from main_db import tasks_done_db, student_tasks, student_task_sh
from PyQt5.QtWidgets import QListWidgetItem
import settings

class StudentPanel(object):
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
        self.addtaskbtn = QtWidgets.QPushButton(self.widget)
        self.addtaskbtn.setGeometry(QtCore.QRect(140, 410, 111, 31))
        self.addtaskbtn.setStyleSheet("QPushButton#addtaskbtn{\n"
        "    font: 8pt \"MS Shell Dlg 2\";    \n"
        "    color: rgb(49, 49, 49);\n"
        "    border: 2px solid rgba(53, 53, 53, 200);\n"
        "    color: rgba(0, 0, 0, 240);\n"
        "    padding-bottom: 7px;\n"
        "    \n"
        "    background-color: rgb(229, 229, 229);\n"
        "    border-radius: 10px;\n"
        "}\n"
        "QPushButton#addtaskbtn:hover{\n"
        "    font: 10pt \"MS Shell Dlg 2\";    \n"
        "    color: rgb(49, 49, 49);\n"
        "}\n"
        "QPushButton#addtaskbtn:pressed{\n"
        "    font: 6pt \"MS Shell Dlg 2\";    \n"
        "    color: rgb(49, 49, 49);\n"
        "}")
        self.addtaskbtn.setObjectName("addtaskbtn")
        self.adminlabel = QtWidgets.QLabel(self.widget)
        self.adminlabel.setGeometry(QtCore.QRect(330, 10, 151, 30))
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
        self.taskslist = QtWidgets.QListWidget(self.widget)
        self.taskslist.setGeometry(QtCore.QRect(640, 70, 141, 331))
        self.taskslist.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
        "border-radius: 8px;\n"
        "border:none;\n"
        "border: 2px solid rgba(53, 53, 53, 200);\n"
        "color: rgba(0, 0, 0, 240);\n"
        "padding-bottom: 7px;")
        self.taskslist.setObjectName("taskslist")
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
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(680, 40, 41, 21))
        self.label_2.setStyleSheet("color: rgb(49, 49, 49);\n"
        "font: 12pt \"MS Shell Dlg 2\";\n"
        "background-color: None")
        self.label_2.setObjectName("label_2")
        self.taskdone = QtWidgets.QComboBox(self.widget)
        self.taskdone.setGeometry(QtCore.QRect(190, 128, 91, 22))
        self.taskdone.setObjectName("taskdone")
        self.taskdone.addItem("")
        self.taskdone.addItem("")
        self.assessment = QtWidgets.QComboBox(self.widget)
        self.assessment.setGeometry(QtCore.QRect(300, 128, 69, 22))
        self.assessment.setObjectName("assessment")
        self.assessment.addItem("")
        self.assessment.addItem("")
        self.assessment.addItem("")
        self.assessment.addItem("")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(190, 110, 47, 13))
        self.label.setStyleSheet("color: rgb(49, 49, 49);\n"
        "font: 8pt \"MS Shell Dlg 2\";\n"
        "background-color: None")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(300, 108, 71, 16))
        self.label_3.setStyleSheet("color: rgb(49, 49, 49);\n"
        "font: 8pt \"MS Shell Dlg 2\";\n"
        "background-color: None")
        self.label_3.setObjectName("label_3")
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
        self.taskdonetext = QtWidgets.QLineEdit(self.widget)
        self.taskdonetext.setGeometry(QtCore.QRect(390, 170, 61, 30))
        self.taskdonetext.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
        "border:none;\n"
        "border-bottom: 2px solid rgba(53, 53, 53, 200);\n"
        "color: rgba(0, 0, 0, 240);\n"
        "padding-bottom: 7px;\n"
        "\n"
        "")
        self.taskdonetext.setObjectName("taskdonetext")
        self.assessmenttext = QtWidgets.QLineEdit(self.widget)
        self.assessmenttext.setGeometry(QtCore.QRect(390, 230, 61, 30))
        self.assessmenttext.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
        "border:none;\n"
        "border-bottom: 2px solid rgba(53, 53, 53, 200);\n"
        "color: rgba(0, 0, 0, 240);\n"
        "padding-bottom: 7px;\n"
        "\n"
        "")
        self.assessmenttext.setObjectName("assessmenttext")
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
        self.addtaskbtn.setText(_translate("MainWindow", "add task"))
        self.adminlabel.setText(_translate("MainWindow", "Student panel"))
        self.backbtn.setText(_translate("MainWindow", "back"))
        self.titletxt.setPlaceholderText(_translate("MainWindow", "title"))
        self.contenttxt.setPlaceholderText(_translate("MainWindow", "content"))
        self.taskrefreshbtn.setText(_translate("MainWindow", "refresh"))
        self.label_2.setText(_translate("MainWindow", "Tasks"))
        self.taskdone.setItemText(0, _translate("MainWindow", "yes"))
        self.taskdone.setItemText(1, _translate("MainWindow", "no"))
        self.assessment.setItemText(0, _translate("MainWindow", "2"))
        self.assessment.setItemText(1, _translate("MainWindow", "3"))
        self.assessment.setItemText(2, _translate("MainWindow", "4"))
        self.assessment.setItemText(3, _translate("MainWindow", "5"))
        self.label.setText(_translate("MainWindow", "task done"))
        self.label_3.setText(_translate("MainWindow", "assessment"))
        self.username.setPlaceholderText(_translate("MainWindow", "username"))
        self.taskdonetext.setPlaceholderText(_translate("MainWindow", "task done"))
        self.assessmenttext.setPlaceholderText(_translate("MainWindow", "assessment"))



        self.addtaskbtn.clicked.connect(self.add_task)
        self.addtaskbtn.clicked.connect(MainWindow.close)

        self.taskrefreshbtn.clicked.connect(self.task_refresh)

        self.backbtn.clicked.connect(self.back_button)
        self.backbtn.clicked.connect(MainWindow.close)



    def add_task(self, values_2):
        username = self.username.text()
        title = self.titletxt.text()
        content = self.contenttxt.toPlainText()
        task_done = self.taskdone.currentText()
        assessment = self.assessment.currentText()
        if len(username) == 0 or len(title) == 0:
            self.MainWindow = QtWidgets.QMainWindow()
            self.ui = StudentPanel()
            self.ui.setupUi (self.MainWindow)
            self.MainWindow.show()
        else:
            self.MainWindow = QtWidgets.QMainWindow()
            self.ui = StudentPanel()
            self.ui.setupUi (self.MainWindow)
            self.MainWindow.show()
            values_2 = (title, task_done, assessment, content, username)
            tasks_done_db(values_2)



    def task_refresh(self):
        self.taskslist.clear()
        user = settings.user[0]
        tasklist = student_tasks(user)
        for i in tasklist:
            self.taskslist.addItem(i[1])
        self.taskslist.itemDoubleClicked.connect(self.one_task)


    def one_task(self, item):
        self.current_user = item
        one_task_student = student_task_sh(settings.user[0], self.current_user.data(0))
        self.titletxt.setText(one_task_student[0][1])
        self.contenttxt.setText(one_task_student[0][4])
        self.taskdonetext.setText(one_task_student[0][2])
        self.assessmenttext.setText(one_task_student[0][3])
        self.username.setText(one_task_student[0][5])




    def back_button(self):
        from studentlogin import StudentLoginPage
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = StudentLoginPage()
        self.ui.setupUi (self.MainWindow)
        self.MainWindow.show()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = StudentPanel()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
