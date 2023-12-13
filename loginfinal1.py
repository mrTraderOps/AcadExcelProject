from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from hmpRevfinal2 import Ui_MainWindow
from signupfinal import Ui_signup
from recover import Ui_Recover
import sys, resfinal1, sqlite3


class Ui_LoginWindow(object):
    def loginUi(self, login):
        login.setObjectName("login")
        login.resize(1040, 617)
        login.setMinimumSize(QtCore.QSize(1040, 617))
        login.setMaximumSize(QtCore.QSize(1040, 617))
        login.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        login.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        self.centralwidget = QtWidgets.QWidget(login)
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
        self.registBtn.setGeometry(QtCore.QRect(665, 131, 51, 21))
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
        self.passL.setGeometry(QtCore.QRect(540, 310, 201, 31))
        self.passL.setStyleSheet("QLineEdit{\n"
"    color:rgb(0, 0, 0)\n"
"}")
        self.passL.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passL.setObjectName("passL")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(540, 130, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.userL = QtWidgets.QLineEdit(self.widget)
        self.userL.setGeometry(QtCore.QRect(540, 230, 201, 31))
        self.userL.setStyleSheet("QLineEdit{\n"
"    color:rgb(0, 0, 0)\n"
"}")
        self.userL.setText("")
        self.userL.setObjectName("userL")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(550, 70, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(540, 190, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(540, 270, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.loginBtn = QtWidgets.QPushButton(self.widget)
        self.loginBtn.setGeometry(QtCore.QRect(540, 380, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        self.loginBtn.setFont(font)
        self.loginBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginBtn.setStyleSheet("QPushButton {\n"
"    background-color:rgb(121, 149, 212);\n"
"    border: None;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: None;\n"
"    color: rgb(75, 110, 189)\n"
"}")
        self.loginBtn.setObjectName("loginBtn")
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
        self.forgot = QtWidgets.QPushButton(self.widget)
        self.forgot.setGeometry(QtCore.QRect(640, 340, 111, 21))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.forgot.setFont(font)
        self.forgot.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.forgot.setStyleSheet("QPushButton{\n"
"    border : None;\n"
"    background: None;\n"
"\n"
"}")
        self.forgot.setObjectName("forgot")
        self.label_2.raise_()
        self.label.raise_()
        self.registBtn.raise_()
        self.passL.raise_()
        self.label_4.raise_()
        self.userL.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.loginBtn.raise_()
        self.exitBtn.raise_()
        self.forgot.raise_()
        login.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(login)
        self.statusbar.setObjectName("statusbar")
        login.setStatusBar(self.statusbar)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

# ========================== Action and Event Signals ====================================================
        self.registBtn.clicked.connect(lambda: self.signup_screen(login))
        self.exitBtn.clicked.connect(login.close)
        self.loginBtn.clicked.connect(lambda: self.loginfunction(login))
        self.forgot.clicked.connect(lambda: self.recover(login))
# ========================== Action and Event Signals ================================================================
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.registBtn.setText(_translate("MainWindow", "Signup"))
        self.label_4.setText(_translate("MainWindow", "Don\'t have account Yet?"))
        self.label_3.setText(_translate("MainWindow", "Good Day!"))
        self.label_5.setText(_translate("MainWindow", "Username"))
        self.label_6.setText(_translate("MainWindow", "Password"))
        self.loginBtn.setText(_translate("MainWindow", "Login"))
        self.forgot.setText(_translate("MainWindow", "Forgot Password?"))

    def recover(self, login):
        try:
            self.recoverWindow = QtWidgets.QMainWindow()
            self.ui = Ui_Recover()
            self.ui.recoverUi(self.recoverWindow)
            self.recoverWindow.show()

            login.hide()

            self.ui.bcktolog.clicked.connect(lambda : self.backtolog(login))
            self.ui.registBtn.clicked.connect(lambda: self.signup_screen(login))
        except Exception as e:
            print("error :", str(e))
    def signup_screen(self, login):
        try:
            self.SignUpWindow = QtWidgets.QMainWindow()
            self.ui1 = Ui_signup()
            self.ui1.SignUpUi(self.SignUpWindow)
            self.SignUpWindow.show()

            login.hide()

            self.ui1.backtoLogin.clicked.connect(lambda : self.backtolog(login))
        except Exception as e:
            print("error :", str(e))
    def loginfunction(self, login):
        username = self.userL.text()
        password = self.passL.text()

        conn = sqlite3.connect("hmp.db")
        cur = conn.cursor()
        query = 'SELECT password FROM userAccount WHERE username = ?'

        try:
            cur.execute(query, (username,))
            result_pass = cur.fetchone()

            if result_pass and result_pass[0] == password:
                msg = QMessageBox()
                msg.setWindowTitle("AcadExcel")
                msg.setIcon(QMessageBox.Information)
                msg.setText("Log-In Successfully")
                msg.exec_()

                self.mainWindow = QtWidgets.QMainWindow()
                self.uiHomepage = Ui_MainWindow()
                self.uiHomepage.setupUi(self.mainWindow)
                self.mainWindow.show()

                conn1 = sqlite3.connect("hmp.db")
                cur1 = conn1.cursor()
                cur1.execute("SELECT screenName FROM userAccount WHERE username=? AND password=?", (username, password))
                result1 = cur1.fetchone()

                if result1:
                    scrn = result1[0]
                    self.uiHomepage.screenName.setText(scrn)
                else:
                    return None

                conn1.close()

                self.uiHomepage.exitBtn.clicked.connect(lambda: self.closelogin(login))
                self.uiHomepage.LogoutBtn.clicked.connect(self.showSure)


                self.userL.clear()
                self.passL.clear()

                self.hidelogin(login)
            else:
                warning = QMessageBox()
                warning.setIcon(QMessageBox.Warning)
                warning.setWindowTitle("Warning")
                warning.setText("Invalid Username or Password")
                warning.setStandardButtons(QMessageBox.Retry)
                warning.exec_()

        except Exception as e:
            print("Error Login:", str(e))

        conn.close()
    def showSure(self):
        warning = QMessageBox()
        warning.setIcon(QMessageBox.Warning)
        warning.setWindowTitle("Warning")
        warning.setText("Sure you want to Log-Out?")
        warning.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        warning.setDefaultButton(QMessageBox.No)
        result = warning.exec_()

        if result == QMessageBox.Yes:
            self.showlogin(login,self.mainWindow)
        else:
            pass
    def closelogin(self, login):
        login.close()
    def hidelogin(self, login):
        login.hide()
    def showlogin(self, login, mainwindow):
        mainwindow.close()
        login.show()
    def backtolog(self,login):
        login.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.loginUi(login)
    login.show()
    sys.exit(app.exec_())
