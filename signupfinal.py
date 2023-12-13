from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import resfinal, sqlite3

class Ui_signup(object):
    def SignUpUi(self, signup):
        signup.setObjectName("signup")
        signup.resize(1040, 617)
        signup.setMinimumSize(QtCore.QSize(1040, 617))
        signup.setMaximumSize(QtCore.QSize(1040, 617))
        signup.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        signup.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.centralwidget = QtWidgets.QWidget(signup)
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
"    border-image: url(:/image/AcadExcel logo.png);\n"
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
        self.backtoLogin = QtWidgets.QPushButton(self.widget)
        self.backtoLogin.setGeometry(QtCore.QRect(600, 131, 91, 21))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.backtoLogin.setFont(font)
        self.backtoLogin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backtoLogin.setStyleSheet("QPushButton{\n"
"    border : None;\n"
"    background: None;\n"
"\n"
"}")
        self.backtoLogin.setObjectName("backtoLogin")
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

        self.newUserL = QtWidgets.QLineEdit(self.widget)
        self.newUserL.setGeometry(QtCore.QRect(540, 280, 201, 31))
        self.newUserL.setStyleSheet("QLineEdit{\n"
"    color:rgb(0, 0, 0)\n"
"}")
        self.newUserL.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newUserL.setObjectName("newUserL")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(540, 130, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.newPassL = QtWidgets.QLineEdit(self.widget)
        self.newPassL.setGeometry(QtCore.QRect(540, 210, 201, 31))
        self.newPassL.setStyleSheet("QLineEdit{\n"
"    color:rgb(0, 0, 0)\n"
"}")
        self.newPassL.setText("")
        self.newPassL.setObjectName("newPassL")
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
        self.label_5.setGeometry(QtCore.QRect(540, 170, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(540, 250, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.registerBtn = QtWidgets.QPushButton(self.widget)
        self.registerBtn.setGeometry(QtCore.QRect(540, 410, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        self.registerBtn.setFont(font)
        self.registerBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.registerBtn.setStyleSheet("QPushButton {\n"
"    background-color:rgb(121, 149, 212);\n"
"    border: None;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: None;\n"
"    color: rgb(75, 110, 189)\n"
"}")
        self.registerBtn.setObjectName("registerBtn")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(540, 320, 121, 31))
        font = QtGui.QFont()

        font.setFamily("Gadugi")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.accNameL = QtWidgets.QLineEdit(self.widget)
        self.accNameL.setGeometry(QtCore.QRect(540, 350, 201, 31))
        self.accNameL.setStyleSheet("QLineEdit{\n"
"    color:rgb(0, 0, 0)\n"
"}")
        self.accNameL.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.accNameL.setObjectName("accNameL")


        self.exitBtn.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.backtoLogin.raise_()
        self.newUserL.raise_()
        self.label_4.raise_()
        self.newPassL.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.registerBtn.raise_()
        self.label_7.raise_()
        self.accNameL.raise_()
        signup.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(signup)
        self.statusbar.setObjectName("statusbar")
        signup.setStatusBar(self.statusbar)

        self.retranslateUi(signup)
        QtCore.QMetaObject.connectSlotsByName(signup)

    # =============================================== Action and Events Signals =========================================================================
        self.backtoLogin.clicked.connect(lambda: self.closescr(signup))
        self.registerBtn.clicked.connect(self.registfunction)
        self.exitBtn.clicked.connect(signup.close)
    # =============================================== Action and Events Signals ==========================================================================

    def closescr(self, signup):
        signup.close()

    def registfunction(self):
        uR = self.newPassL.text().strip()
        pwR = self.newUserL.text().strip()
        accN = self.accNameL.text().strip()

        if not uR or not pwR or not accN:
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Please fill in the empty fields")
            msg.exec_()
        else:
            conn = sqlite3.connect("hmp.db")
            cur = conn.cursor()
            query = 'SELECT username, screenName FROM userAccount WHERE username=? OR screenName = ?'

            try:
                cur.execute(query, (uR,accN))
                result = cur.fetchone()

                if result is not None:
                    if result[0] == uR:
                        msg = QMessageBox()
                        msg.setWindowTitle("Login Status")
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText("The Username is already exist")
                        msg.exec_()
                    elif result[1] == accN:
                        msg = QMessageBox()
                        msg.setWindowTitle("Login Status")
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText("The Account Name is already exist")
                        msg.exec_()
                    elif result[0] == uR and result[1] == accN:
                        msg = QMessageBox()
                        msg.setWindowTitle("Login Status")
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText("Account is already exist")
                        msg.exec_()
                else:
                    cur.execute("INSERT INTO userAccount VALUES (?, ?, ?)", (uR, pwR, accN))
                    conn.commit()
                    msg = QMessageBox()
                    msg.setWindowTitle("Login Status")
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("The Account is successfully registered!")
                    msg.exec_()

            except Exception as e:
                print("error", str(e))
            conn.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.backtoLogin.setText(_translate("MainWindow", "Back to Login"))
        self.label_4.setText(_translate("MainWindow", "Registered?"))
        self.label_3.setText(_translate("MainWindow", "Sign Up"))
        self.label_5.setText(_translate("MainWindow", "Username"))
        self.label_6.setText(_translate("MainWindow", "Password"))
        self.registerBtn.setText(_translate("MainWindow", "Register"))
        self.label_7.setText(_translate("MainWindow", "Account Name"))



