from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys, resfinal1, sqlite3

class Ui_Recover(object):
    def recoverUi(self, recover):
        recover.setObjectName("MainWindow")
        recover.resize(1040, 617)
        recover.setMinimumSize(QtCore.QSize(1040, 617))
        recover.setMaximumSize(QtCore.QSize(1040, 617))
        recover.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        recover.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        self.centralwidget = QtWidgets.QWidget(recover)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(70, 50, 861, 501))
        self.widget.setStyleSheet("QWidget {\n"
"        color: rgb(255, 255, 255)\n"
"}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 441, 491))
        self.label.setStyleSheet("QLabel {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-image: url(:/image/images/AcadExcel logo.png);\n"
"}\n"
"    \n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(420, 0, 441, 491))
        self.label_2.setStyleSheet("QLabel {\n"
"    background-color: rgb(76, 111, 191)\n"
"}")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.registBtn = QtWidgets.QPushButton(self.widget)
        self.registBtn.setGeometry(QtCore.QRect(630, 111, 51, 21))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.registBtn.setFont(font)
        self.registBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.registBtn.setStyleSheet("QPushButton{\n"
"    border : None;\n"
"    background: None;\n"
"\n"
"}")
        self.registBtn.setObjectName("registBtn")
        self.passL = QtWidgets.QLineEdit(self.widget)
        self.passL.setGeometry(QtCore.QRect(550, 230, 201, 31))
        self.passL.setStyleSheet("QLineEdit{\n"
"    color:rgb(0, 0, 0)\n"
"}")
        self.passL.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.passL.setObjectName("passL")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(520, 110, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.userL = QtWidgets.QLineEdit(self.widget)
        self.userL.setGeometry(QtCore.QRect(550, 170, 201, 31))
        self.userL.setStyleSheet("QLineEdit{\n"
"    color:rgb(0, 0, 0)\n"
"}")
        self.userL.setText("")
        self.userL.setObjectName("userL")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(520, 60, 291, 61))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(550, 134, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(550, 200, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.recBtn = QtWidgets.QPushButton(self.widget)
        self.recBtn.setGeometry(QtCore.QRect(550, 410, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        self.recBtn.setFont(font)
        self.recBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.recBtn.setStyleSheet("QPushButton {\n"
"    background-color:rgb(121, 149, 212);\n"
"    border: None;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: None;\n"
"    color: rgb(75, 110, 189)\n"
"}")
        self.recBtn.setObjectName("loginBtn")
        self.exitBtn = QtWidgets.QPushButton(self.widget)
        self.exitBtn.setGeometry(QtCore.QRect(820, 0, 41, 31))
        self.exitBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitBtn.setStyleSheet("QPushButton {\n"
"    \n"
"border: rgb(0, 0, 0);\n"
"background-color:rgb(76, 111, 191);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #ff2c2c;\n"
"    border: rgb(0, 0, 0);\n"
"}\n"
"")
        self.exitBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/images/x icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitBtn.setIcon(icon)
        self.exitBtn.setObjectName("exitBtn")
        self.passL_2 = QtWidgets.QLineEdit(self.widget)
        self.passL_2.setGeometry(QtCore.QRect(550, 290, 201, 31))
        self.passL_2.setStyleSheet("QLineEdit{\n"
"    color:rgb(0, 0, 0)\n"
"}")
        self.passL_2.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.passL_2.setObjectName("passL_2")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(550, 260, 121, 25))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.passL_3 = QtWidgets.QLineEdit(self.widget)
        self.passL_3.setGeometry(QtCore.QRect(550, 350, 201, 31))
        self.passL_3.setStyleSheet("QLineEdit{\n"
"    color:rgb(0, 0, 0)\n"
"}")
        self.passL_3.setText("")
        self.passL_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passL_3.setObjectName("passL_3")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(550, 323, 121, 25))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(550, 323, 121, 25))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.bcktolog = QtWidgets.QPushButton(self.widget)
        self.bcktolog.setGeometry(QtCore.QRect(685, 111, 91, 21))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.bcktolog.setFont(font)
        self.bcktolog.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bcktolog.setStyleSheet("QPushButton{\n"
                                    "    border : None;\n"
                                    "    background: None;\n"
                                    "\n"
                                    "}")
        self.bcktolog.setObjectName("bcktolog")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(680, 110, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_2.raise_()
        self.label.raise_()
        self.registBtn.raise_()
        self.passL.raise_()
        self.label_4.raise_()
        self.userL.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.recBtn.raise_()
        self.exitBtn.raise_()
        self.passL_2.raise_()
        self.label_7.raise_()
        self.passL_3.raise_()
        self.label_8.raise_()
        self.bcktolog.raise_()
        self.label_9.raise_()
        recover.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(recover)
        self.statusbar.setObjectName("statusbar")
        recover.setStatusBar(self.statusbar)

        self.retranslateUi(recover)
        QtCore.QMetaObject.connectSlotsByName(recover)

        self.exitBtn.clicked.connect(lambda :self.closeRec(recover))
        self.bcktolog.clicked.connect(lambda : self.closeRec(recover))
        self.registBtn.clicked.connect(lambda : self.closeRec(recover))
        self.recBtn.clicked.connect(self.func)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.registBtn.setText(_translate("MainWindow", "Signup"))
        self.label_4.setText(_translate("MainWindow", "Create New Account?"))
        self.label_3.setText(_translate("MainWindow", "Account Recovery"))
        self.label_5.setText(_translate("MainWindow", "Username"))
        self.label_6.setText(_translate("MainWindow", "Account Name"))
        self.recBtn.setText(_translate("MainWindow", "Recover"))
        self.label_7.setText(_translate("MainWindow", "New Password"))
        self.label_8.setText(_translate("MainWindow", "Confirm Password"))
        self.bcktolog.setText(_translate("MainWindow", "Back to Login"))
        self.label_9.setText(_translate("MainWindow", "or"))

    def func(self):
        try:
            u = self.userL.text()
            acN = self.passL.text()
            p1 = self.passL_2.text()
            p2 = self.passL_3.text()


            if not u or not acN or not p1 or not p2:
                self.msgBoxWarn("Please fill all empty field/s")
                return

            if p1 != p2:
                self.msgBoxWarn("Password not match")
                return

            conn = sqlite3.connect("hmp.db")
            cur = conn.cursor()
            cur.execute('SELECT username, screenName FROM userAccount WHERE username = ? AND screenName = ?',
                        (u,acN))
            result = cur.fetchall()

            if result:
                self.msgBwYN("Sure you want to change Password?")
                if self.showWYN == QMessageBox.Yes:
                    cur.execute('UPDATE userAccount SET password = ? WHERE username = ?',
                                (p2, u))
                    conn.commit()
                    self.msgBoxInfo(f"The Account Name - {acN} successfully changed the Password")
                    self.userL.clear()
                    self.passL.clear()
                    self.passL_2.clear()
                    self.passL_3.clear()
                else:
                    return
            else:
                self.msgBoxWarn(f"Account Doesn't Exist")

            conn.close()

        except Exception as e:
            print("error : ", str(e))


    def msgBoxInfo(self, msg):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("AcadExcel")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(msg)
        self.showInfo = msgBox.exec()

    def msgBoxWarn(self, msg1):
        msgBox1 = QMessageBox()
        msgBox1.setWindowTitle("Warning")
        msgBox1.setIcon(QMessageBox.Warning)
        msgBox1.setText(msg1)
        self.showWarn = msgBox1.exec()

    def msgBwYN(self, msg2):
        warning = QMessageBox()
        warning.setIcon(QMessageBox.Question)
        warning.setWindowTitle("Question")
        warning.setText(msg2)
        warning.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        warning.setDefaultButton(QMessageBox.No)
        self.showWYN = warning.exec_()


    def closeRec(self, recover):
        recover.close()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    recMain = QtWidgets.QMainWindow()
    ui = Ui_Recover()
    ui.recoverUi(recMain)
    recMain.show()
    sys.exit(app.exec_())
