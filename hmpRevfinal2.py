from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QFileDialog
from overviewFormfinal1 import over_Form
from formfinal import Ui_Form
import resfinal1, sqlite3, sys, os
import pandas as pd


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1324, 687)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.menu_widget = QtWidgets.QWidget(self.centralwidget)
        self.menu_widget.setGeometry(QtCore.QRect(90, 10, 1211, 661))
        self.menu_widget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.menu_widget.setAutoFillBackground(False)
        self.menu_widget.setStyleSheet("background-color:rgb(248, 249, 250);\n"
                                       "")
        self.menu_widget.setObjectName("menu_widget")
        self.widget_2 = QtWidgets.QWidget(self.menu_widget)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 181, 661))
        self.widget_2.setStyleSheet("background-color:rgb(76, 111, 191)")
        self.widget_2.setObjectName("widget_2")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(70, 50, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255)\n"
                                   "")
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(35, 150, 111, 111))
        self.label.setMinimumSize(QtCore.QSize(90, 90))
        self.label.setStyleSheet("border-image: url(:/image/images/user.png);\n"
                                 "")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.screenName = QtWidgets.QLabel(self.widget_2)
        self.screenName.setGeometry(QtCore.QRect(20, 270, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.screenName.setFont(font)
        self.screenName.setAutoFillBackground(False)
        self.screenName.setStyleSheet("color:rgb(240, 246, 255)")
        self.screenName.setAlignment(QtCore.Qt.AlignCenter)
        self.screenName.setObjectName("screenName")
        self.LogoutBtn = QtWidgets.QPushButton(self.widget_2)
        self.LogoutBtn.setGeometry(QtCore.QRect(10, 580, 159, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.LogoutBtn.setFont(font)
        self.LogoutBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LogoutBtn.setStyleSheet("QPushButton {color:rgb(236, 242, 251);\n"
                                     "border: none;\n"
                                     "\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover{\n"
                                     "background-color:rgb(254, 138, 141);\n"
                                     "border-radius: 20%;\n"
                                     "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LogoutBtn.setIcon(icon)
        self.LogoutBtn.setObjectName("LogoutBtn")
        self.layoutWidget = QtWidgets.QWidget(self.widget_2)
        self.layoutWidget.setGeometry(QtCore.QRect(15, 340, 156, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.GradelBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.GradelBtn.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.GradelBtn.setFont(font)
        self.GradelBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GradelBtn.setStyleSheet("QPushButton {\n"
                                     "color:rgb(238, 244, 253);\n"
                                     "border: none;\n"
                                     "padding: 10px 15px;\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "background-color:rgb(255, 255, 255);\n"
                                     "color: rgb(76, 111, 191);\n"
                                     "border-radius: 15%;\n"
                                     "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/table calculation.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.GradelBtn.setIcon(icon1)
        self.GradelBtn.setObjectName("GradelBtn")
        self.verticalLayout.addWidget(self.GradelBtn)
        self.CreatorBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.CreatorBtn.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.CreatorBtn.setFont(font)
        self.CreatorBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CreatorBtn.setStyleSheet("QPushButton {\n"
                                      "color:rgb(238, 244, 253);\n"
                                      "border: none;\n"
                                      "padding: 10px 15px;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color:rgb(255, 255, 255);\n"
                                      "color: rgb(76, 111, 191);\n"
                                      "border-radius: 15%;\n"
                                      "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/table creator.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CreatorBtn.setIcon(icon2)
        self.CreatorBtn.setShortcut("")
        self.CreatorBtn.setCheckable(False)
        self.CreatorBtn.setObjectName("CreatorBtn")
        self.verticalLayout.addWidget(self.CreatorBtn)
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(30, 55, 41, 31))
        self.pushButton.setStyleSheet("border: None;")
        self.pushButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/image/images/AcadExcel_Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.stackedWidget = QtWidgets.QStackedWidget(self.menu_widget)
        self.stackedWidget.setGeometry(QtCore.QRect(190, 30, 1021, 631))
        self.stackedWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.stackedWidget.setStyleSheet("background-color:rgb(248, 249, 250)")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_87 = QtWidgets.QLabel(self.page_3)
        self.label_87.setGeometry(QtCore.QRect(20, 30, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_87.setFont(font)
        self.label_87.setStyleSheet("")
        self.label_87.setObjectName("label_87")
        self.label_86 = QtWidgets.QLabel(self.page_3)
        self.label_86.setGeometry(QtCore.QRect(60, 330, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_86.setFont(font)
        self.label_86.setObjectName("label_86")
        self.layoutWidget_42 = QtWidgets.QWidget(self.page_3)
        self.layoutWidget_42.setGeometry(QtCore.QRect(40, 170, 301, 118))
        self.layoutWidget_42.setObjectName("layoutWidget_42")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.layoutWidget_42)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.verticalLayout_42 = QtWidgets.QVBoxLayout()
        self.verticalLayout_42.setObjectName("verticalLayout_42")
        self.label_123 = QtWidgets.QLabel(self.layoutWidget_42)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_123.setFont(font)
        self.label_123.setAlignment(QtCore.Qt.AlignCenter)
        self.label_123.setObjectName("label_123")
        self.verticalLayout_42.addWidget(self.label_123)
        self.label_119 = QtWidgets.QLabel(self.layoutWidget_42)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_119.setFont(font)
        self.label_119.setAlignment(QtCore.Qt.AlignCenter)
        self.label_119.setObjectName("label_119")
        self.verticalLayout_42.addWidget(self.label_119)
        self.label_120 = QtWidgets.QLabel(self.layoutWidget_42)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_120.setFont(font)
        self.label_120.setAlignment(QtCore.Qt.AlignCenter)
        self.label_120.setObjectName("label_120")
        self.verticalLayout_42.addWidget(self.label_120)
        self.label_121 = QtWidgets.QLabel(self.layoutWidget_42)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_121.setFont(font)
        self.label_121.setAlignment(QtCore.Qt.AlignCenter)
        self.label_121.setObjectName("label_121")
        self.verticalLayout_42.addWidget(self.label_121)
        self.horizontalLayout_18.addLayout(self.verticalLayout_42)
        self.verticalLayout_43 = QtWidgets.QVBoxLayout()
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        self.studID = QtWidgets.QLineEdit(self.layoutWidget_42)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(9)
        self.studID.setFont(font)
        self.studID.setStyleSheet("QLineEdit {\n"
                                  "    background-color:rgb(255, 255, 255)\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:focus {\n"
                                  "    border: 1px solid e5de00\n"
                                  "}")
        self.studID.setMaxLength(9)
        self.studID.setObjectName("studID")
        self.verticalLayout_43.addWidget(self.studID)
        self.lastN = QtWidgets.QLineEdit(self.layoutWidget_42)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(9)
        self.lastN.setFont(font)
        self.lastN.setStyleSheet("QLineEdit {\n"
                                 "    background-color:rgb(255, 255, 255)\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit:focus {\n"
                                 "    border: 1px solid e5de00\n"
                                 "}")
        self.lastN.setText("")
        self.lastN.setObjectName("lastN")
        self.verticalLayout_43.addWidget(self.lastN)
        self.firstN = QtWidgets.QLineEdit(self.layoutWidget_42)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(9)
        self.firstN.setFont(font)
        self.firstN.setStyleSheet("QLineEdit {\n"
                                  "    background-color:rgb(255, 255, 255)\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:focus {\n"
                                  "    border: 1px solid e5de00\n"
                                  "}")
        self.firstN.setObjectName("firstN")
        self.verticalLayout_43.addWidget(self.firstN)
        self.MidN = QtWidgets.QLineEdit(self.layoutWidget_42)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(9)
        self.MidN.setFont(font)
        self.MidN.setStyleSheet("QLineEdit {\n"
                                "    background-color:rgb(255, 255, 255)\n"
                                "}\n"
                                "\n"
                                "QLineEdit:focus {\n"
                                "    border: 1px solid e5de00\n"
                                "}")
        self.MidN.setObjectName("MidN")
        self.verticalLayout_43.addWidget(self.MidN)
        self.horizontalLayout_18.addLayout(self.verticalLayout_43)
        self.label_122 = QtWidgets.QLabel(self.page_3)
        self.label_122.setGeometry(QtCore.QRect(20, 130, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_122.setFont(font)
        self.label_122.setAlignment(QtCore.Qt.AlignCenter)
        self.label_122.setObjectName("label_122")
        self.import2 = QtWidgets.QPushButton(self.page_3)
        self.import2.setGeometry(QtCore.QRect(790, 210, 121, 31))
        self.import2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.import2.setStyleSheet("QPushButton {\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "background-color:rgb(76, 111, 191);\n"
                                   "border-radius: 15%;\n"
                                   "border: None;\n"
                                   "font: 25 8pt \"Bahnschrift Light\";\n"
                                   "}\n"
                                   "QPushButton:hover{\n"
                                   "background-color:rgb(202, 240, 248);\n"
                                   "color:rgb(0, 0, 0);\n"
                                   "border-radius: 15%;\n"
                                   "border: None;\n"
                                   "font: 25 8pt \"Bahnschrift Light\";\n"
                                   "}")
        self.import2.setObjectName("import2")
        self.label_115 = QtWidgets.QLabel(self.page_3)
        self.label_115.setGeometry(QtCore.QRect(410, 130, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_115.setFont(font)
        self.label_115.setStyleSheet("")
        self.label_115.setObjectName("label_115")
        self.term = QtWidgets.QLabel(self.page_3)
        self.term.setGeometry(QtCore.QRect(830, 130, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.term.setFont(font)
        self.term.setStyleSheet("")
        self.term.setObjectName("term")
        self.SvIm_2 = QtWidgets.QPushButton(self.page_3)
        self.SvIm_2.setGeometry(QtCore.QRect(630, 210, 121, 31))
        self.SvIm_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SvIm_2.setStyleSheet("QPushButton {\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "background-color:rgb(76, 111, 191);\n"
                                  "border-radius: 15%;\n"
                                  "border: None;\n"
                                  "font: 25 8pt \"Bahnschrift Light\";\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background-color:rgb(202, 240, 248);\n"
                                  "color:rgb(0, 0, 0);\n"
                                  "border-radius: 15%;\n"
                                  "border: None;\n"
                                  "font: 25 8pt \"Bahnschrift Light\";\n"
                                  "}")
        self.SvIm_2.setObjectName("SvIm_2")
        self.SvIm_3 = QtWidgets.QPushButton(self.page_3)
        self.SvIm_3.setGeometry(QtCore.QRect(470, 210, 121, 31))
        self.SvIm_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SvIm_3.setStyleSheet("QPushButton {\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "background-color:rgb(76, 111, 191);\n"
                                  "border-radius: 15%;\n"
                                  "border: None;\n"
                                  "font: 25 8pt \"Bahnschrift Light\";\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background-color:rgb(202, 240, 248);\n"
                                  "color:rgb(0, 0, 0);\n"
                                  "border-radius: 15%;\n"
                                  "border: None;\n"
                                  "font: 25 8pt \"Bahnschrift Light\";\n"
                                  "}")
        self.SvIm_3.setObjectName("SvIm_3")
        self.widget = QtWidgets.QWidget(self.page_3)
        self.widget.setGeometry(QtCore.QRect(50, 400, 201, 221))
        self.widget.setStyleSheet("font: 12pt \"Bahnschrift SemiBold\";\n"
                                  "")
        self.widget.setObjectName("widget")
        self.layoutWidget1 = QtWidgets.QWidget(self.widget)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 10, 131, 31))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.quizChk = QtWidgets.QCheckBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.quizChk.setFont(font)
        self.quizChk.setObjectName("quizChk")
        self.horizontalLayout_9.addWidget(self.quizChk)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.assPct1_3 = QtWidgets.QLineEdit(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assPct1_3.sizePolicy().hasHeightForWidth())
        self.assPct1_3.setSizePolicy(sizePolicy)
        self.assPct1_3.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.assPct1_3.setObjectName("assPct1_3")
        self.horizontalLayout.addWidget(self.assPct1_3)
        self.label_179 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_179.setFont(font)
        self.label_179.setObjectName("label_179")
        self.horizontalLayout.addWidget(self.label_179)
        self.horizontalLayout_9.addLayout(self.horizontalLayout)
        self.layoutWidget2 = QtWidgets.QWidget(self.widget)
        self.layoutWidget2.setGeometry(QtCore.QRect(140, 50, 20, 151))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_16 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_5.addWidget(self.label_16)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_5.addWidget(self.label_13)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_5.addWidget(self.label_15)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_5.addWidget(self.label_14)
        self.qL1 = QtWidgets.QLineEdit(self.widget)
        self.qL1.setGeometry(QtCore.QRect(100, 60, 29, 21))
        self.qL1.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.qL1.setObjectName("qL1")
        self.qL2 = QtWidgets.QLineEdit(self.widget)
        self.qL2.setGeometry(QtCore.QRect(100, 100, 31, 21))
        self.qL2.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.qL2.setObjectName("qL2")
        self.qL3 = QtWidgets.QLineEdit(self.widget)
        self.qL3.setGeometry(QtCore.QRect(100, 140, 29, 20))
        self.qL3.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.qL3.setObjectName("qL3")
        self.qL4 = QtWidgets.QLineEdit(self.widget)
        self.qL4.setGeometry(QtCore.QRect(100, 180, 31, 21))
        self.qL4.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.qL4.setObjectName("qL4")
        self.pctQ1 = QtWidgets.QLineEdit(self.widget)
        self.pctQ1.setGeometry(QtCore.QRect(160, 60, 31, 21))
        self.pctQ1.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.pctQ1.setObjectName("pctQ1")
        self.pctQ2 = QtWidgets.QLineEdit(self.widget)
        self.pctQ2.setGeometry(QtCore.QRect(160, 100, 31, 21))
        self.pctQ2.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.pctQ2.setObjectName("pctQ2")
        self.pctQ3 = QtWidgets.QLineEdit(self.widget)
        self.pctQ3.setGeometry(QtCore.QRect(160, 139, 31, 21))
        self.pctQ3.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.pctQ3.setObjectName("pctQ3")
        self.pctQ4 = QtWidgets.QLineEdit(self.widget)
        self.pctQ4.setGeometry(QtCore.QRect(160, 180, 31, 21))
        self.pctQ4.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.pctQ4.setObjectName("pctQ4")
        self.q1 = QtWidgets.QCheckBox(self.widget)
        self.q1.setGeometry(QtCore.QRect(11, 60, 64, 23))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.q1.setFont(font)
        self.q1.setCheckable(True)
        self.q1.setChecked(False)
        self.q1.setTristate(False)
        self.q1.setObjectName("q1")
        self.q2 = QtWidgets.QCheckBox(self.widget)
        self.q2.setGeometry(QtCore.QRect(11, 100, 67, 23))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.q2.setFont(font)
        self.q2.setCheckable(True)
        self.q2.setChecked(False)
        self.q2.setTristate(False)
        self.q2.setObjectName("q2")
        self.q3 = QtWidgets.QCheckBox(self.widget)
        self.q3.setGeometry(QtCore.QRect(11, 140, 67, 23))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.q3.setFont(font)
        self.q3.setCheckable(True)
        self.q3.setObjectName("q3")
        self.q4 = QtWidgets.QCheckBox(self.widget)
        self.q4.setGeometry(QtCore.QRect(11, 180, 68, 23))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.q4.setFont(font)
        self.q4.setCheckable(True)
        self.q4.setChecked(False)
        self.q4.setTristate(False)
        self.q4.setObjectName("q4")
        self.widget_3 = QtWidgets.QWidget(self.page_3)
        self.widget_3.setGeometry(QtCore.QRect(250, 390, 251, 241))
        self.widget_3.setStyleSheet("font: 63 12pt \"Bahnschrift SemiBold\";")
        self.widget_3.setObjectName("widget_3")
        self.prL4pct = QtWidgets.QLineEdit(self.widget_3)
        self.prL4pct.setGeometry(QtCore.QRect(210, 190, 31, 20))
        self.prL4pct.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.prL4pct.setObjectName("prL4pct")
        self.prL2 = QtWidgets.QLineEdit(self.widget_3)
        self.prL2.setGeometry(QtCore.QRect(150, 110, 31, 20))
        self.prL2.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.prL2.setObjectName("prL2")
        self.prL3pct = QtWidgets.QLineEdit(self.widget_3)
        self.prL3pct.setGeometry(QtCore.QRect(210, 150, 31, 20))
        self.prL3pct.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.prL3pct.setObjectName("prL3pct")
        self.prL4 = QtWidgets.QLineEdit(self.widget_3)
        self.prL4.setGeometry(QtCore.QRect(150, 190, 31, 20))
        self.prL4.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.prL4.setObjectName("prL4")
        self.pr3 = QtWidgets.QCheckBox(self.widget_3)
        self.pr3.setGeometry(QtCore.QRect(30, 140, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pr3.setFont(font)
        self.pr3.setObjectName("pr3")
        self.pr1 = QtWidgets.QCheckBox(self.widget_3)
        self.pr1.setGeometry(QtCore.QRect(30, 60, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pr1.setFont(font)
        self.pr1.setObjectName("pr1")
        self.prL3 = QtWidgets.QLineEdit(self.widget_3)
        self.prL3.setGeometry(QtCore.QRect(150, 150, 31, 20))
        self.prL3.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.prL3.setObjectName("prL3")
        self.prL1pct = QtWidgets.QLineEdit(self.widget_3)
        self.prL1pct.setGeometry(QtCore.QRect(210, 70, 31, 20))
        self.prL1pct.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.prL1pct.setObjectName("prL1pct")
        self.pr2 = QtWidgets.QCheckBox(self.widget_3)
        self.pr2.setGeometry(QtCore.QRect(30, 100, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pr2.setFont(font)
        self.pr2.setObjectName("pr2")
        self.pr4 = QtWidgets.QCheckBox(self.widget_3)
        self.pr4.setGeometry(QtCore.QRect(30, 180, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pr4.setFont(font)
        self.pr4.setObjectName("pr4")
        self.prL1 = QtWidgets.QLineEdit(self.widget_3)
        self.prL1.setGeometry(QtCore.QRect(150, 70, 31, 20))
        self.prL1.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.prL1.setObjectName("prL1")
        self.prL2pct = QtWidgets.QLineEdit(self.widget_3)
        self.prL2pct.setGeometry(QtCore.QRect(210, 110, 31, 20))
        self.prL2pct.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.prL2pct.setObjectName("prL2pct")
        self.layoutWidget_2 = QtWidgets.QWidget(self.widget_3)
        self.layoutWidget_2.setGeometry(QtCore.QRect(190, 60, 20, 151))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_17 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_6.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_6.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_6.addWidget(self.label_19)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_6.addWidget(self.label_20)
        self.layoutWidget3 = QtWidgets.QWidget(self.widget_3)
        self.layoutWidget3.setGeometry(QtCore.QRect(40, 20, 161, 30))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.prChk = QtWidgets.QCheckBox(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prChk.sizePolicy().hasHeightForWidth())
        self.prChk.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.prChk.setFont(font)
        self.prChk.setObjectName("prChk")
        self.horizontalLayout_6.addWidget(self.prChk)
        self.assPct1_4 = QtWidgets.QLineEdit(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assPct1_4.sizePolicy().hasHeightForWidth())
        self.assPct1_4.setSizePolicy(sizePolicy)
        self.assPct1_4.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.assPct1_4.setObjectName("assPct1_4")
        self.horizontalLayout_6.addWidget(self.assPct1_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_180 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_180.setFont(font)
        self.label_180.setObjectName("label_180")
        self.horizontalLayout_3.addWidget(self.label_180)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)
        self.widget_4 = QtWidgets.QWidget(self.page_3)
        self.widget_4.setGeometry(QtCore.QRect(500, 390, 271, 231))
        self.widget_4.setStyleSheet("font: 63 12pt \"Bahnschrift SemiBold\";")
        self.widget_4.setObjectName("widget_4")
        self.assPct4 = QtWidgets.QLineEdit(self.widget_4)
        self.assPct4.setGeometry(QtCore.QRect(220, 190, 31, 20))
        self.assPct4.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.assPct4.setObjectName("assPct4")
        self.assign2 = QtWidgets.QCheckBox(self.widget_4)
        self.assign2.setGeometry(QtCore.QRect(20, 100, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.assign2.setFont(font)
        self.assign2.setObjectName("assign2")
        self.assPct1 = QtWidgets.QLineEdit(self.widget_4)
        self.assPct1.setGeometry(QtCore.QRect(220, 70, 31, 20))
        self.assPct1.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.assPct1.setObjectName("assPct1")
        self.assign3 = QtWidgets.QCheckBox(self.widget_4)
        self.assign3.setGeometry(QtCore.QRect(20, 140, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.assign3.setFont(font)
        self.assign3.setObjectName("assign3")
        self.assL1 = QtWidgets.QLineEdit(self.widget_4)
        self.assL1.setGeometry(QtCore.QRect(160, 70, 31, 20))
        self.assL1.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.assL1.setObjectName("assL1")
        self.assign4 = QtWidgets.QCheckBox(self.widget_4)
        self.assign4.setGeometry(QtCore.QRect(20, 180, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.assign4.setFont(font)
        self.assign4.setObjectName("assign4")
        self.assL4 = QtWidgets.QLineEdit(self.widget_4)
        self.assL4.setGeometry(QtCore.QRect(160, 190, 31, 20))
        self.assL4.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.assL4.setObjectName("assL4")
        self.assPct3 = QtWidgets.QLineEdit(self.widget_4)
        self.assPct3.setGeometry(QtCore.QRect(220, 150, 31, 20))
        self.assPct3.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.assPct3.setObjectName("assPct3")
        self.assL2 = QtWidgets.QLineEdit(self.widget_4)
        self.assL2.setGeometry(QtCore.QRect(160, 110, 31, 20))
        self.assL2.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.assL2.setObjectName("assL2")
        self.assPct2 = QtWidgets.QLineEdit(self.widget_4)
        self.assPct2.setGeometry(QtCore.QRect(220, 110, 31, 20))
        self.assPct2.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.assPct2.setObjectName("assPct2")
        self.assign1 = QtWidgets.QCheckBox(self.widget_4)
        self.assign1.setGeometry(QtCore.QRect(20, 60, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.assign1.setFont(font)
        self.assign1.setObjectName("assign1")
        self.assL3 = QtWidgets.QLineEdit(self.widget_4)
        self.assL3.setGeometry(QtCore.QRect(160, 150, 31, 20))
        self.assL3.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.assL3.setObjectName("assL3")
        self.layoutWidget_3 = QtWidgets.QWidget(self.widget_4)
        self.layoutWidget_3.setGeometry(QtCore.QRect(200, 60, 20, 151))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_21 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_7.addWidget(self.label_21)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_7.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_7.addWidget(self.label_23)
        self.label_24 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_7.addWidget(self.label_24)
        self.layoutWidget4 = QtWidgets.QWidget(self.widget_4)
        self.layoutWidget4.setGeometry(QtCore.QRect(20, 20, 181, 30))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.assignCHK = QtWidgets.QCheckBox(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.assignCHK.setFont(font)
        self.assignCHK.setObjectName("assignCHK")
        self.horizontalLayout_7.addWidget(self.assignCHK)
        self.assPct1_2 = QtWidgets.QLineEdit(self.layoutWidget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assPct1_2.sizePolicy().hasHeightForWidth())
        self.assPct1_2.setSizePolicy(sizePolicy)
        self.assPct1_2.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.assPct1_2.setObjectName("assPct1_2")
        self.horizontalLayout_7.addWidget(self.assPct1_2)
        self.label_178 = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_178.setFont(font)
        self.label_178.setObjectName("label_178")
        self.horizontalLayout_7.addWidget(self.label_178)
        self.widget_5 = QtWidgets.QWidget(self.page_3)
        self.widget_5.setGeometry(QtCore.QRect(360, 280, 641, 101))
        self.widget_5.setStyleSheet("font: 63 12pt \"Bahnschrift SemiBold\";")
        self.widget_5.setObjectName("widget_5")
        self.atn1 = QtWidgets.QLineEdit(self.widget_5)
        self.atn1.setGeometry(QtCore.QRect(60, 70, 31, 20))
        self.atn1.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.atn1.setObjectName("atn1")
        self.atn1Pct = QtWidgets.QLineEdit(self.widget_5)
        self.atn1Pct.setGeometry(QtCore.QRect(120, 70, 31, 20))
        self.atn1Pct.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.atn1Pct.setObjectName("atn1Pct")
        self.label_26 = QtWidgets.QLabel(self.widget_5)
        self.label_26.setGeometry(QtCore.QRect(100, 70, 20, 21))
        self.label_26.setObjectName("label_26")
        self.layoutWidget5 = QtWidgets.QWidget(self.widget_5)
        self.layoutWidget5.setGeometry(QtCore.QRect(240, 30, 171, 30))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.rctChk = QtWidgets.QCheckBox(self.layoutWidget5)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.rctChk.setFont(font)
        self.rctChk.setObjectName("rctChk")
        self.horizontalLayout_10.addWidget(self.rctChk)
        self.rctPct = QtWidgets.QLineEdit(self.layoutWidget5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rctPct.sizePolicy().hasHeightForWidth())
        self.rctPct.setSizePolicy(sizePolicy)
        self.rctPct.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.rctPct.setObjectName("rctPct")
        self.horizontalLayout_10.addWidget(self.rctPct)
        self.label_176 = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_176.setFont(font)
        self.label_176.setObjectName("label_176")
        self.horizontalLayout_10.addWidget(self.label_176)
        self.rct1Pct = QtWidgets.QLineEdit(self.widget_5)
        self.rct1Pct.setGeometry(QtCore.QRect(320, 70, 31, 20))
        self.rct1Pct.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.rct1Pct.setObjectName("rct1Pct")
        self.rct1 = QtWidgets.QLineEdit(self.widget_5)
        self.rct1.setGeometry(QtCore.QRect(260, 70, 31, 20))
        self.rct1.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.rct1.setObjectName("rct1")
        self.label_27 = QtWidgets.QLabel(self.widget_5)
        self.label_27.setGeometry(QtCore.QRect(300, 70, 20, 21))
        self.label_27.setObjectName("label_27")
        self.layoutWidget6 = QtWidgets.QWidget(self.widget_5)
        self.layoutWidget6.setGeometry(QtCore.QRect(440, 30, 161, 30))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.atdChk = QtWidgets.QCheckBox(self.layoutWidget6)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.atdChk.setFont(font)
        self.atdChk.setObjectName("atdChk")
        self.horizontalLayout_11.addWidget(self.atdChk)
        self.atdPct = QtWidgets.QLineEdit(self.layoutWidget6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.atdPct.sizePolicy().hasHeightForWidth())
        self.atdPct.setSizePolicy(sizePolicy)
        self.atdPct.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.atdPct.setObjectName("atdPct")
        self.horizontalLayout_11.addWidget(self.atdPct)
        self.label_177 = QtWidgets.QLabel(self.layoutWidget6)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_177.setFont(font)
        self.label_177.setObjectName("label_177")
        self.horizontalLayout_11.addWidget(self.label_177)
        self.atd1Pct = QtWidgets.QLineEdit(self.widget_5)
        self.atd1Pct.setGeometry(QtCore.QRect(520, 70, 31, 20))
        self.atd1Pct.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.atd1Pct.setObjectName("atd1Pct")
        self.atd1 = QtWidgets.QLineEdit(self.widget_5)
        self.atd1.setGeometry(QtCore.QRect(460, 70, 31, 20))
        self.atd1.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.atd1.setObjectName("atd1")
        self.label_28 = QtWidgets.QLabel(self.widget_5)
        self.label_28.setGeometry(QtCore.QRect(500, 70, 16, 21))
        self.label_28.setObjectName("label_28")
        self.layoutWidget7 = QtWidgets.QWidget(self.widget_5)
        self.layoutWidget7.setGeometry(QtCore.QRect(40, 30, 181, 31))
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget7)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.atnChk = QtWidgets.QCheckBox(self.layoutWidget7)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.atnChk.setFont(font)
        self.atnChk.setObjectName("atnChk")
        self.horizontalLayout_8.addWidget(self.atnChk)
        self.atnPct = QtWidgets.QLineEdit(self.layoutWidget7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.atnPct.sizePolicy().hasHeightForWidth())
        self.atnPct.setSizePolicy(sizePolicy)
        self.atnPct.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.atnPct.setObjectName("atnPct")
        self.horizontalLayout_8.addWidget(self.atnPct)
        self.label_128 = QtWidgets.QLabel(self.layoutWidget7)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_128.setFont(font)
        self.label_128.setObjectName("label_128")
        self.horizontalLayout_8.addWidget(self.label_128)
        self.widget_6 = QtWidgets.QWidget(self.page_3)
        self.widget_6.setGeometry(QtCore.QRect(780, 390, 211, 231))
        self.widget_6.setStyleSheet("font: 63 11pt \"Bahnschrift SemiBold\";")
        self.widget_6.setObjectName("widget_6")
        self.layoutWidget8 = QtWidgets.QWidget(self.widget_6)
        self.layoutWidget8.setGeometry(QtCore.QRect(20, 50, 121, 29))
        self.layoutWidget8.setObjectName("layoutWidget8")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.layoutWidget8)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget8)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_12.addWidget(self.label_4)
        self.assPct1_5 = QtWidgets.QLineEdit(self.layoutWidget8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assPct1_5.sizePolicy().hasHeightForWidth())
        self.assPct1_5.setSizePolicy(sizePolicy)
        self.assPct1_5.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.assPct1_5.setObjectName("assPct1_5")
        self.horizontalLayout_12.addWidget(self.assPct1_5)
        self.label_181 = QtWidgets.QLabel(self.layoutWidget8)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_181.setFont(font)
        self.label_181.setObjectName("label_181")
        self.horizontalLayout_12.addWidget(self.label_181)
        self.exWrPct = QtWidgets.QLineEdit(self.widget_6)
        self.exWrPct.setGeometry(QtCore.QRect(90, 190, 31, 20))
        self.exWrPct.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.exWrPct.setObjectName("exWrPct")
        self.exWrL = QtWidgets.QLineEdit(self.widget_6)
        self.exWrL.setGeometry(QtCore.QRect(30, 190, 31, 20))
        self.exWrL.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.exWrL.setObjectName("exWrL")
        self.exPrL = QtWidgets.QLineEdit(self.widget_6)
        self.exPrL.setGeometry(QtCore.QRect(30, 130, 31, 20))
        self.exPrL.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.exPrL.setObjectName("exPrL")
        self.exPrPct = QtWidgets.QLineEdit(self.widget_6)
        self.exPrPct.setGeometry(QtCore.QRect(90, 130, 31, 20))
        self.exPrPct.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.exPrPct.setObjectName("exPrPct")
        self.prelim = QtWidgets.QCheckBox(self.widget_6)
        self.prelim.setGeometry(QtCore.QRect(10, 10, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.prelim.setFont(font)
        self.prelim.setObjectName("prelim")
        self.label_29 = QtWidgets.QLabel(self.widget_6)
        self.label_29.setGeometry(QtCore.QRect(70, 130, 20, 21))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.widget_6)
        self.label_30.setGeometry(QtCore.QRect(70, 190, 20, 21))
        self.label_30.setObjectName("label_30")
        self.widget1 = QtWidgets.QWidget(self.widget_6)
        self.widget1.setGeometry(QtCore.QRect(20, 150, 141, 31))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_4.addWidget(self.checkBox_2)
        self.wrPct = QtWidgets.QLineEdit(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wrPct.sizePolicy().hasHeightForWidth())
        self.wrPct.setSizePolicy(sizePolicy)
        self.wrPct.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.wrPct.setObjectName("wrPct")
        self.horizontalLayout_4.addWidget(self.wrPct)
        self.label_183 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_183.setFont(font)
        self.label_183.setObjectName("label_183")
        self.horizontalLayout_4.addWidget(self.label_183)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.widget2 = QtWidgets.QWidget(self.widget_6)
        self.widget2.setGeometry(QtCore.QRect(20, 90, 151, 26))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.widget2)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.prPct = QtWidgets.QLineEdit(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prPct.sizePolicy().hasHeightForWidth())
        self.prPct.setSizePolicy(sizePolicy)
        self.prPct.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";")
        self.prPct.setObjectName("prPct")
        self.horizontalLayout_2.addWidget(self.prPct)
        self.label_182 = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_182.setFont(font)
        self.label_182.setObjectName("label_182")
        self.horizontalLayout_2.addWidget(self.label_182)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_2)
        self.label_116 = QtWidgets.QLabel(self.page_3)
        self.label_116.setGeometry(QtCore.QRect(690, 130, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_116.setFont(font)
        self.label_116.setStyleSheet("")
        self.label_116.setObjectName("label_116")
        self.subjC = QtWidgets.QPushButton(self.page_3)
        self.subjC.setGeometry(QtCore.QRect(550, 130, 121, 31))
        self.subjC.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.subjC.setStyleSheet("border: None;\n"
                                 "font: 63 13pt \"Bahnschrift SemiBold\";")
        self.subjC.setObjectName("subjC")
        self.stackedWidget.addWidget(self.page_3)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.export2Excel = QtWidgets.QPushButton(self.page)
        self.export2Excel.setGeometry(QtCore.QRect(880, 62, 121, 31))
        self.export2Excel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.export2Excel.setStyleSheet("QPushButton {\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color:rgb(76, 111, 191);\n"
                                        "border-radius: 15%;\n"
                                        "border: None;\n"
                                        "font: 25 8pt \"Bahnschrift Light\";\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "background-color:rgb(116, 198, 157);\n"
                                        "color:rgb(0, 0, 0);\n"
                                        "border-radius: 15%;\n"
                                        "font: 25 8pt \"Bahnschrift Light\";\n"
                                        "}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/image/images/xl icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.export2Excel.setIcon(icon4)
        self.export2Excel.setObjectName("export2Excel")
        self.removeBtn_2 = QtWidgets.QPushButton(self.page)
        self.removeBtn_2.setGeometry(QtCore.QRect(150, 62, 91, 31))
        self.removeBtn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.removeBtn_2.setStyleSheet("QPushButton {\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "background-color:rgb(76, 111, 191);\n"
                                       "border-radius: 15%;\n"
                                       "border: None;\n"
                                       "font: 25 8pt \"Bahnschrift Light\";\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "background-color:rgb(202, 240, 248);\n"
                                       "color:rgb(0, 0, 0);\n"
                                       "border-radius: 15%;\n"
                                       "border: None;\n"
                                       "font: 25 8pt \"Bahnschrift Light\";\n"
                                       "}")
        self.removeBtn_2.setObjectName("removeBtn_2")
        self.studentTbl = QtWidgets.QTableWidget(self.page)
        self.studentTbl.setGeometry(QtCore.QRect(30, 110, 971, 461))
        self.studentTbl.setObjectName("studentTbl")
        self.studentTbl.setColumnCount(0)
        self.studentTbl.setRowCount(0)
        self.term1 = QtWidgets.QLabel(self.page)
        self.term1.setGeometry(QtCore.QRect(430, 590, 191, 23))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.term1.setFont(font)
        self.term1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.term1.setObjectName("term1")
        self.backBtn = QtWidgets.QPushButton(self.page)
        self.backBtn.setGeometry(QtCore.QRect(30, 582, 91, 31))
        self.backBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backBtn.setStyleSheet("QPushButton {\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "background-color:rgb(76, 111, 191);\n"
                                   "border-radius: 15%;\n"
                                   "border: None;\n"
                                   "font: 25 8pt \"Bahnschrift Light\";\n"
                                   "}\n"
                                   "QPushButton:hover{\n"
                                   "background-color:rgb(202, 240, 248);\n"
                                   "color:rgb(0, 0, 0);\n"
                                   "border-radius: 15%;\n"
                                   "border: None;\n"
                                   "font: 25 8pt \"Bahnschrift Light\";\n"
                                   "}")
        self.backBtn.setObjectName("backBtn")
        self.Lbtn = QtWidgets.QPushButton(self.page)
        self.Lbtn.setGeometry(QtCore.QRect(30, 62, 91, 31))
        self.Lbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Lbtn.setStyleSheet("QPushButton {\n"
                                "color: rgb(255, 255, 255);\n"
                                "background-color:rgb(76, 111, 191);\n"
                                "border-radius: 15%;\n"
                                "border: None;\n"
                                "font: 25 8pt \"Bahnschrift Light\";\n"
                                "}\n"
                                "QPushButton:hover{\n"
                                "background-color:rgb(202, 240, 248);\n"
                                "color:rgb(0, 0, 0);\n"
                                "border-radius: 15%;\n"
                                "border: None;\n"
                                "font: 25 8pt \"Bahnschrift Light\";\n"
                                "}")
        self.Lbtn.setObjectName("Lbtn")
        self.labels = QtWidgets.QLabel(self.page)
        self.labels.setGeometry(QtCore.QRect(400, 70, 124, 28))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labels.setFont(font)
        self.labels.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.labels.setObjectName("labels")
        self.subjC1 = QtWidgets.QLabel(self.page)
        self.subjC1.setGeometry(QtCore.QRect(540, 70, 131, 28))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.subjC1.setFont(font)
        self.subjC1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.subjC1.setObjectName("subjC1")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 206, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.page_2)
        self.tableWidget.setGeometry(QtCore.QRect(15, 71, 981, 541))
        self.tableWidget.setStyleSheet("QTableWidget {\n"
                                       "    background-color: rgb(255, 255, 255)\n"
                                       "}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.label_10 = QtWidgets.QLabel(self.page_2)
        self.label_10.setGeometry(QtCore.QRect(160, 20, 31, 31))
        self.label_10.setStyleSheet("border-image: url(:/icons/table creator.png);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.addRowBtn = QtWidgets.QPushButton(self.page_2)
        self.addRowBtn.setGeometry(QtCore.QRect(440, 30, 91, 31))
        self.addRowBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addRowBtn.setStyleSheet("QPushButton {\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "background-color:rgb(76, 111, 191);\n"
                                     "border-radius: 15%;\n"
                                     "border: None;\n"
                                     "font: 25 8pt \"Bahnschrift Light\";\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "background-color:rgb(202, 240, 248);\n"
                                     "color:rgb(0, 0, 0);\n"
                                     "border-radius: 15%;\n"
                                     "border: None;\n"
                                     "font: 25 8pt \"Bahnschrift Light\";\n"
                                     "}")
        self.addRowBtn.setObjectName("addRowBtn")
        self.columnNBtn = QtWidgets.QPushButton(self.page_2)
        self.columnNBtn.setGeometry(QtCore.QRect(550, 30, 151, 31))
        self.columnNBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.columnNBtn.setStyleSheet("QPushButton {\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color:rgb(76, 111, 191);\n"
                                      "border-radius: 15%;\n"
                                      "border: None;\n"
                                      "font: 25 8pt \"Bahnschrift Light\";\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color:rgb(202, 240, 248);\n"
                                      "color:rgb(0, 0, 0);\n"
                                      "border-radius: 15%;\n"
                                      "border: None;\n"
                                      "font: 25 8pt \"Bahnschrift Light\";\n"
                                      "}")
        self.columnNBtn.setObjectName("columnNBtn")
        self.removeBtn = QtWidgets.QPushButton(self.page_2)
        self.removeBtn.setGeometry(QtCore.QRect(720, 30, 121, 31))
        self.removeBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.removeBtn.setStyleSheet("QPushButton {\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "background-color:rgb(76, 111, 191);\n"
                                     "border-radius: 15%;\n"
                                     "border: None;\n"
                                     "font: 25 8pt \"Bahnschrift Light\";\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "background-color:rgb(202, 240, 248);\n"
                                     "color:rgb(0, 0, 0);\n"
                                     "border-radius: 15%;\n"
                                     "border: None;\n"
                                     "font: 25 8pt \"Bahnschrift Light\";\n"
                                     "}")
        self.removeBtn.setObjectName("removeBtn")
        self.exportBtn = QtWidgets.QPushButton(self.page_2)
        self.exportBtn.setGeometry(QtCore.QRect(860, 30, 131, 31))
        self.exportBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exportBtn.setStyleSheet("QPushButton {\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "background-color:rgb(76, 111, 191);\n"
                                     "border-radius: 15%;\n"
                                     "border: None;\n"
                                     "font: 25 8pt \"Bahnschrift Light\";\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "background-color:rgb(116, 198, 157);\n"
                                     "color:rgb(0, 0, 0);\n"
                                     "border-radius: 15%;\n"
                                     "font: 25 8pt \"Bahnschrift Light\";\n"
                                     "}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/image/xl icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exportBtn.setIcon(icon5)
        self.exportBtn.setObjectName("exportBtn")
        self.stackedWidget.addWidget(self.page_2)
        self.exitBtn = QtWidgets.QPushButton(self.menu_widget)
        self.exitBtn.setGeometry(QtCore.QRect(1160, 0, 51, 31))
        self.exitBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitBtn.setStyleSheet("QPushButton {\n"
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
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/image/images/x icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitBtn.setIcon(icon6)
        self.exitBtn.setObjectName("exitBtn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.functions()
        self.dialog()
        self.subjC.clicked.connect(self.dialog)
        self.exitBtn.clicked.connect(lambda: self.exit(MainWindow))
        self.studentTbl.setColumnCount(20)

        column_names = ["StudentID", "LastName", "FirstName", "MiddleName",
                        f"Quiz(%)", "Quiz(Eq.)", f"Practical(%)", "Practical(Eq.)",
                        f"Assignment(%)", "Assignment(Eq.)", f"Exam(%)", "Exam(Eq.)",
                        f"Attendance(%)", "Attendance(Eq.)", f"Recitation(%)", "Recitation(Eq.)",
                        f"Attitude(%)", "Attitude(Eq.)", "Overall (Eq)", "Grade"]

        self.studentTbl.setHorizontalHeaderLabels(column_names)

        self.q1.setEnabled(False)
        self.q2.setEnabled(False)
        self.q3.setEnabled(False)
        self.q4.setEnabled(False)
        self.qL1.setEnabled(False)
        self.qL2.setEnabled(False)
        self.qL3.setEnabled(False)
        self.qL4.setEnabled(False)
        self.pctQ1.setEnabled(False)
        self.pctQ2.setEnabled(False)
        self.pctQ3.setEnabled(False)
        self.pctQ4.setEnabled(False)

        self.assign1.setEnabled(False)
        self.assign2.setEnabled(False)
        self.assign3.setEnabled(False)
        self.assign4.setEnabled(False)
        self.assL1.setEnabled(False)
        self.assL2.setEnabled(False)
        self.assL3.setEnabled(False)
        self.assL4.setEnabled(False)
        self.assPct1.setEnabled(False)
        self.assPct2.setEnabled(False)
        self.assPct3.setEnabled(False)
        self.assPct4.setEnabled(False)

        self.pr1.setEnabled(False)
        self.pr2.setEnabled(False)
        self.pr3.setEnabled(False)
        self.pr4.setEnabled(False)
        self.prL1.setEnabled(False)
        self.prL2.setEnabled(False)
        self.prL3.setEnabled(False)
        self.prL4.setEnabled(False)
        self.prL1pct.setEnabled(False)
        self.prL2pct.setEnabled(False)
        self.prL3pct.setEnabled(False)
        self.prL4pct.setEnabled(False)

        self.exPrL.setEnabled(False)
        self.exPrPct.setEnabled(False)
        self.exWrL.setEnabled(False)
        self.exWrPct.setEnabled(False)

        self.atnPct.setEnabled(False)
        self.atn1.setEnabled(False)
        self.atn1Pct.setEnabled(False)
        self.rct1.setEnabled(False)
        self.rctPct.setEnabled(False)
        self.rct1Pct.setEnabled(False)
        self.atd1.setEnabled(False)
        self.atd1Pct.setEnabled(False)
        self.atdPct.setEnabled(False)
        self.assPct1_3.setEnabled(False)
        self.assPct1_2.setEnabled(False)
        self.assPct1_4.setEnabled(False)
        self.assPct1_5.setEnabled(False)
        self.prPct.setEnabled(False)
        self.wrPct.setEnabled(False)
        self.checkBox.setEnabled(False)
        self.checkBox_2.setEnabled(False)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "AcadExcel"))
        self.screenName.setText(_translate("MainWindow", "Account Name"))
        self.LogoutBtn.setText(_translate("MainWindow", " Logout"))
        self.GradelBtn.setText(_translate("MainWindow", "Class Record"))
        self.CreatorBtn.setText(_translate("MainWindow", "Grade Sheet Table"))
        self.label_87.setText(_translate("MainWindow", "Class Record Management System"))
        self.label_86.setText(_translate("MainWindow", "Student Raw Score"))
        self.label_123.setText(_translate("MainWindow", "Student ID"))
        self.label_119.setText(_translate("MainWindow", "Last Name"))
        self.label_120.setText(_translate("MainWindow", "First Name"))
        self.label_121.setText(_translate("MainWindow", "Middle Name"))
        self.studID.setPlaceholderText(_translate("MainWindow", "Maximum of 8 digit only"))
        self.label_122.setText(_translate("MainWindow", "Student Information"))
        self.import2.setText(_translate("MainWindow", "Import to Table"))
        self.label_115.setText(_translate("MainWindow", "SUBJECT CODE :"))
        self.term.setText(_translate("MainWindow", "PRELIMINARY"))
        self.SvIm_2.setText(_translate("MainWindow", "Computation"))
        self.SvIm_3.setText(_translate("MainWindow", "Load"))
        self.quizChk.setText(_translate("MainWindow", "Quiz "))
        self.label_179.setText(_translate("MainWindow", "%"))
        self.label_16.setText(_translate("MainWindow", " / "))
        self.label_13.setText(_translate("MainWindow", " /"))
        self.label_15.setText(_translate("MainWindow", " /"))
        self.label_14.setText(_translate("MainWindow", " /"))
        self.q1.setText(_translate("MainWindow", "Quiz 1"))
        self.q2.setText(_translate("MainWindow", "Quiz 2"))
        self.q3.setText(_translate("MainWindow", "Quiz 3"))
        self.q4.setText(_translate("MainWindow", "Quiz 4"))
        self.pr3.setText(_translate("MainWindow", "Practical 3"))
        self.pr1.setText(_translate("MainWindow", "Practical 1"))
        self.pr2.setText(_translate("MainWindow", "Practical 2"))
        self.pr4.setText(_translate("MainWindow", "Practical 4"))
        self.label_17.setText(_translate("MainWindow", " / "))
        self.label_18.setText(_translate("MainWindow", " /"))
        self.label_19.setText(_translate("MainWindow", " /"))
        self.label_20.setText(_translate("MainWindow", " /"))
        self.prChk.setText(_translate("MainWindow", "Practical"))
        self.label_180.setText(_translate("MainWindow", "%"))
        self.assign2.setText(_translate("MainWindow", "Assignment 2"))
        self.assign3.setText(_translate("MainWindow", "Assignment 3"))
        self.assign4.setText(_translate("MainWindow", "Assignment 4"))
        self.assign1.setText(_translate("MainWindow", "Assignment 1"))
        self.label_21.setText(_translate("MainWindow", " / "))
        self.label_22.setText(_translate("MainWindow", " /"))
        self.label_23.setText(_translate("MainWindow", " /"))
        self.label_24.setText(_translate("MainWindow", " /"))
        self.assignCHK.setText(_translate("MainWindow", "Assignment"))
        self.label_178.setText(_translate("MainWindow", "%"))
        self.label_26.setText(_translate("MainWindow", " / "))
        self.rctChk.setText(_translate("MainWindow", "Recitation"))
        self.label_176.setText(_translate("MainWindow", "%"))
        self.label_27.setText(_translate("MainWindow", " / "))
        self.atdChk.setText(_translate("MainWindow", "Attitude"))
        self.label_177.setText(_translate("MainWindow", "%"))
        self.label_28.setText(_translate("MainWindow", " / "))
        self.atnChk.setText(_translate("MainWindow", "Attendance"))
        self.label_128.setText(_translate("MainWindow", "%"))
        self.label_4.setText(_translate("MainWindow", "Exam"))
        self.label_181.setText(_translate("MainWindow", "%"))
        self.prelim.setText(_translate("MainWindow", "PRELIMINARY"))
        self.label_29.setText(_translate("MainWindow", " / "))
        self.label_30.setText(_translate("MainWindow", " / "))
        self.checkBox_2.setText(_translate("MainWindow", "Written"))
        self.label_183.setText(_translate("MainWindow", "%"))
        self.checkBox.setText(_translate("MainWindow", "Practical"))
        self.label_182.setText(_translate("MainWindow", "%"))
        self.label_116.setText(_translate("MainWindow", "SUBJECT TERM :"))
        self.subjC.setText(_translate("MainWindow", "PL101"))
        self.export2Excel.setText(_translate("MainWindow", "Export"))
        self.removeBtn_2.setText(_translate("MainWindow", "Remove"))
        self.term1.setText(_translate("MainWindow", "PRELIMINARY - TERM"))
        self.backBtn.setText(_translate("MainWindow", "Back"))
        self.Lbtn.setText(_translate("MainWindow", "Load"))
        self.labels.setText(_translate("MainWindow", "Subject Code : "))
        self.subjC1.setText(_translate("MainWindow", "PL101"))
        self.label_3.setText(_translate("MainWindow", "Grade Sheet Table "))
        self.label_2.setText(_translate("MainWindow", "Table Creator"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Student List"))
        self.addRowBtn.setText(_translate("MainWindow", "Add Row/s"))
        self.columnNBtn.setText(_translate("MainWindow", "Add Column and Name"))
        self.removeBtn.setText(_translate("MainWindow", "Remove Selected"))
        self.exportBtn.setText(_translate("MainWindow", "Export to Excel"))

    def exit(self, homepage):
        homepage.close()
    def showmain(self):
        self.stackedWidget.setCurrentIndex(0)
    def tablecreator(self):
        self.stackedWidget.setCurrentIndex(1)
    def functions(self):
        self.enablefunc()

        self.CreatorBtn.clicked.connect(self.tablecreator)
        self.GradelBtn.clicked.connect(self.showmain)

        self.backBtn.clicked.connect(self.Back)
        self.studID.textChanged.connect(self.autofill)
        self.export2Excel.clicked.connect(self.xport2xcel)
        self.removeBtn_2.clicked.connect(self.removefunc)
        self.Lbtn.clicked.connect(self.loadsaved)
        self.SvIm_3.clicked.connect(self.loadfunc)

        self.import2.clicked.connect(self.SnI)
        self.SvIm_2.clicked.connect(self.showOverview)
        self.SvIm_3.clicked.connect(self.showOverview)

    def loadsaved(self):
        acntN = self.screenName.text().strip()
        subjC = self.subjC.text()
        term = self.term.text()

        conn = sqlite3.connect('hmp.db')
        cur = conn.cursor()
        try:
            cur.execute(
                "SELECT studentID, lastName, firstName, middleName, "
                "quizPct, quizEq, practicalPct, pracitcalEq, "
                "assPct, assEq, exPct, exEq, "
                "atnPct, atnEq, rctPct, rctEq, "
                "atdPct, atdEq, overallEq, Grade "
                "FROM finalLoadData "
                "WHERE accountName = ? AND subjectCode = ? AND term = ?",
                (acntN, subjC, term))

            data = cur.fetchall()

            if not data:
                self.msgBoxWarn("No data found.")
                return

            numcolumns = 20

            self.studentTbl.setRowCount(len(data))
            self.studentTbl.setColumnCount(numcolumns)

            for row_index, row_data in enumerate(data):
                for col_index, cell_data in enumerate(row_data):
                    item = QTableWidgetItem(str(cell_data))
                    self.studentTbl.setItem(row_index, col_index, item)

        except sqlite3.Error as e:
            print("Error in loadsaved fetching data from the database:", e)
        finally:
            conn.close()
    def autofill(self):
        stud = self.studID.text()

        con = sqlite3.connect("hmp.db")
        cur = con.cursor()
        cur.execute(f"SELECT LastName, FirstName, MiddleName FROM studentInfo WHERE studentID = ?", (stud,))

        result = cur.fetchone()

        if result:
            self.lastN.setText(result[0])
            self.firstN.setText(result[1])
            self.MidN.setText(result[2])
        else:
            self.lastN.clear()
            self.firstN.clear()
            self.MidN.clear()
            self.quizChk.setChecked(False)
            self.assignCHK.setChecked(False)
            self.prChk.setChecked(False)
            self.prelim.setChecked(False)
            self.atnChk.setChecked(False)
            self.rctChk.setChecked(False)
            self.atdChk.setChecked(False)

        con.close()
    def SnI(self):
        try:
            acntN = self.screenName.text()
            subjC = self.subjC.text()
            term = self.term.text()
            studId = self.studID.text()
            lastN = self.lastN.text()
            firstN = self.firstN.text()
            midN = self.MidN.text()
            q = self.assPct1_3.text() or '0'
            ass = self.assPct1_2.text() or '0'
            prac = self.assPct1_4.text() or '0'
            ex = self.assPct1_5.text() or '0'
            atn = self.atnPct.text() or '0'
            rec = self.rctPct.text() or '0'
            atd = self.atdPct.text() or '0'

            con = sqlite3.connect("hmp.db")
            cur = con.cursor()
            cur.execute(
                f"SELECT * FROM studentInfo WHERE studentID = ? AND LastName = ? AND FirstName = ? AND MiddleName = ?",
                (studId, lastN, firstN, midN))

            result = cur.fetchone()

            # if studentID in studentInfo Table is existed, execute this and criteria must 100%, if not 100% PASS
            # if criteria at 100% import to table, scan in finalLoadData if Subject+StudId+Term+Account existed = UPDATE, if not = INSERT
            if result:
                if (q and ass and prac and ex and atn and rec and atd):
                    numQ = float(q)
                    numAss = float(ass)
                    numPrac = float(prac)
                    numE = float(ex)
                    numAtn = float(atn)
                    numRec = float(rec)
                    numAtd = float(atd)

                    result = numQ + numPrac + numAtd + numE + numRec + numAss + numAtn

                    if result == 100:

                        row_position = self.studentTbl.rowCount()
                        self.studentTbl.insertRow(row_position)

                        self.studentTbl.setItem(row_position, 0, QTableWidgetItem(studId))
                        self.studentTbl.setItem(row_position, 1, QTableWidgetItem(lastN))
                        self.studentTbl.setItem(row_position, 2, QTableWidgetItem(firstN))
                        self.studentTbl.setItem(row_position, 3, QTableWidgetItem(midN))

                        self.studentTbl.setItem(row_position, 4, QTableWidgetItem(f"{self.qzPct:.2f}"))
                        self.studentTbl.setItem(row_position, 5, QTableWidgetItem(f"{self.quizEq:.2f}"))

                        if self.pracPct is not None:
                            self.studentTbl.setItem(row_position, 6, QTableWidgetItem(f"{self.pracPct:.2f}"))
                        else:
                            self.studentTbl.setItem(row_position, 6, QTableWidgetItem(f"0.00"))

                        self.studentTbl.setItem(row_position, 7, QTableWidgetItem(f"{self.pracEq:.2f}"))
                        self.studentTbl.setItem(row_position, 8, QTableWidgetItem(f"{self.assignPct:.2f}"))
                        self.studentTbl.setItem(row_position, 9, QTableWidgetItem(f"{self.assEq:.2f}"))
                        self.studentTbl.setItem(row_position, 10, QTableWidgetItem(f"{self.exPct}"))
                        self.studentTbl.setItem(row_position, 11, QTableWidgetItem(f"{self.exEq:.2f}"))
                        self.studentTbl.setItem(row_position, 12, QTableWidgetItem(f"{self.attendPct:.2f}"))
                        self.studentTbl.setItem(row_position, 13, QTableWidgetItem(f"{self.atnEq:.2f}"))
                        self.studentTbl.setItem(row_position, 14, QTableWidgetItem(f"{self.recPct:.2f}"))
                        self.studentTbl.setItem(row_position, 15, QTableWidgetItem(f"{self.recEq:.2f}"))
                        self.studentTbl.setItem(row_position, 16, QTableWidgetItem(f"{self.attPct:.2f}"))
                        self.studentTbl.setItem(row_position, 17, QTableWidgetItem(f"{self.attEq:.2f}"))
                        self.studentTbl.setItem(row_position, 18, QTableWidgetItem(f"{self.overEq:.2f}"))
                        self.studentTbl.setItem(row_position, 19, QTableWidgetItem(f"{self.grade_text}"))

                        try:
                            cur.execute(
                                f"SELECT * FROM finalLoadData WHERE accountName = ? AND subjectCode = ? AND term = ? AND studentID = ?",
                                (acntN, subjC, term, studId))

                            result = cur.fetchone()

                            if result:
                                cur.execute(
                                    "UPDATE finalLoadData SET "
                                    "lastName = ?, firstName = ?, middleName = ?, "
                                    "quizPct = ?, quizEq = ?, practicalPct = ?, pracitcalEq = ?, "
                                    "assPct = ?, assEq = ?, exPct = ?, exEq = ?, "
                                    "atnPct = ?, atnEq = ?, rctPct = ?, rctEq = ?, "
                                    "atdPct = ?, atdEq = ?, overallEq = ?, Grade = ? "
                                    "WHERE accountName = ? AND subjectCode = ? AND term = ? AND studentID = ?",
                                    (lastN, firstN, midN,
                                     f"{self.qzPct:.2f}", f"{self.quizEq:.2f}",
                                     f"{self.pracPct:.2f}", f"{self.pracEq:.2f}",
                                     f"{self.assignPct:.2f}", f"{self.assEq:.2f}",
                                     f"{self.exPct:.2f}", f"{self.exEq:.2f}",
                                     f"{self.attendPct:.2f}", f"{self.atnEq:.2f}",
                                     f"{self.recPct:.2f}", f"{self.recEq:.2f}",
                                     f"{self.attPct:.2f}", f"{self.attEq:.2f}",
                                     f"{self.overEq:.2f}", f"{self.grade_text}",
                                     acntN, subjC, term, studId)
                                )

                                con.commit()

                                self.msgBoxInfo(
                                    f"Student ID: {studId} - {lastN}, {firstN} {midN} Data has been Modified/Updated")
                            else:
                                cur.execute(
                                    "INSERT INTO finalLoadData (accountName, subjectCode, term, studentID, lastName, firstName, middleName, "
                                    "quizPct, quizEq, practicalPct, pracitcalEq, assPct, assEq, exPct, exEq, "
                                    "atnPct, atnEq, rctPct, rctEq, atdPct, atdEq, overallEq, Grade) "
                                    "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                    (
                                        acntN, subjC, term, studId, lastN, firstN, midN,
                                        f"{self.qzPct:.2f}", f"{self.quizEq:.2f}",
                                        f"{self.pracPct:.2f}", f"{self.pracEq:.2f}",
                                        f"{self.assignPct:.2f}", f"{self.assEq:.2f}",
                                        f"{self.exPct:.2f}", f"{self.exEq:.2f}",
                                        f"{self.attendPct:.2f}", f"{self.atnEq:.2f}",
                                        f"{self.recPct:.2f}", f"{self.recEq:.2f}",
                                        f"{self.attPct:.2f}", f"{self.attEq:.2f}",
                                        f"{self.overEq:.2f}", f"{self.grade_text}")
                                )

                                con.commit()

                                self.msgBoxInfo(f"Student ID: {studId} - {lastN}, {firstN} {midN} Successfully Added")

                                con.close()

                                self.stackedWidget.setCurrentIndex(1)

                        except sqlite3.Error as e:
                            print("Error SnI inserting data into the database: ", e)

                        self.msgBoxInfo(
                            "Informing that Percentage Criteria reached 100%")

                    else:
                        self.msgBoxWarn("The Percentage of Criteria must be at 100%, Please modify your Percentage/s")

                else:
                    pass

            # if studentID in studentInfo Table is not existed, execute this and criteria must 100%, if not 100% = PASS
            # if criteria at 100% import table, scan in finalLoadData if Subject+StudId+Term+Account existed = UPDATE, if not = INSERT
            else:
                if not studId or not lastN or not firstN or not midN:
                    self.msgBoxWarn("Please fill out all fields.")
                else:
                    cur.execute(
                        "INSERT INTO studentInfo (studentID, LastName, FirstName, MiddleName) VALUES (?, ?, ?, ?)",
                        (studId, lastN, firstN, midN))

                    con.commit()

                    if (q and ass and prac and ex and atn and rec and atd):
                        numQ = float(q)
                        numAss = float(ass)
                        numPrac = float(prac)
                        numE = float(ex)
                        numAtn = float(atn)
                        numRec = float(rec)
                        numAtd = float(atd)

                        result = numQ + numPrac + numAtd + numE + numRec + numAss + numAtn

                        if result == 100:

                            self.stackedWidget.setCurrentIndex(1)

                            row_position = self.studentTbl.rowCount()
                            self.studentTbl.insertRow(row_position)

                            self.studentTbl.setItem(row_position, 0, QTableWidgetItem(studId))
                            self.studentTbl.setItem(row_position, 1, QTableWidgetItem(lastN))
                            self.studentTbl.setItem(row_position, 2, QTableWidgetItem(firstN))
                            self.studentTbl.setItem(row_position, 3, QTableWidgetItem(midN))

                            self.studentTbl.setItem(row_position, 4,
                                                    QTableWidgetItem(f"{self.qzPct:.2f}"))
                            self.studentTbl.setItem(row_position, 5,
                                                    QTableWidgetItem(f"{self.quizEq:.2f}"))
                            self.studentTbl.setItem(row_position, 6,
                                                    QTableWidgetItem(f"{self.pracPct:.2f}"))
                            self.studentTbl.setItem(row_position, 7,
                                                    QTableWidgetItem(f"{self.pracEq:.2f}"))
                            self.studentTbl.setItem(row_position, 8,
                                                    QTableWidgetItem(f"{self.assignPct:.2f}"))
                            self.studentTbl.setItem(row_position, 9,
                                                    QTableWidgetItem(f"{self.assEq:.2f}"))
                            self.studentTbl.setItem(row_position, 10,
                                                    QTableWidgetItem(f"{self.exPct:.2f}"))
                            self.studentTbl.setItem(row_position, 11,
                                                    QTableWidgetItem(f"{self.exEq:.2f}"))
                            self.studentTbl.setItem(row_position, 12,
                                                    QTableWidgetItem(f"{self.attendPct:.2f}"))
                            self.studentTbl.setItem(row_position, 13,
                                                    QTableWidgetItem(f"{self.atnEq:.2f}"))
                            self.studentTbl.setItem(row_position, 14,
                                                    QTableWidgetItem(f"{self.recPct:.2f}"))
                            self.studentTbl.setItem(row_position, 15,
                                                    QTableWidgetItem(f"{self.recEq:.2f}"))
                            self.studentTbl.setItem(row_position, 16,
                                                    QTableWidgetItem(f"{self.attPct:.2f}"))
                            self.studentTbl.setItem(row_position, 17,
                                                    QTableWidgetItem(f"{self.attEq:.2f}"))
                            self.studentTbl.setItem(row_position, 18,
                                                    QTableWidgetItem(f"{self.overEq:.2f}"))
                            self.studentTbl.setItem(row_position, 19,
                                                    QTableWidgetItem(f"{self.grade_text}"))

                            try:
                                cur.execute(
                                    f"SELECT * FROM finalLoadData WHERE accountName = ? AND subjectCode = ? AND term = ? AND studentID = ?",
                                    (acntN, subjC, term, studId))

                                result = cur.fetchone()

                                if result:
                                    cur.execute(
                                        "UPDATE finalLoadData SET "
                                        "lastName = ?, firstName = ?, middleName = ?, "
                                        "quizPct = ?, quizEq = ?, practicalPct = ?, pracitcalEq = ?, "
                                        "assPct = ?, assEq = ?, exPct = ?, exEq = ?, "
                                        "atnPct = ?, atnEq = ?, rctPct = ?, rctEq = ?, "
                                        "atdPct = ?, atdEq = ?, overallEq = ?, Grade = ? "
                                        "WHERE accountName = ? AND subjectCode = ? AND term = ? AND studentID = ?",
                                        (lastN, firstN, midN,
                                         f"{self.qzPct:.2f}", f"{self.quizEq:.2f}",
                                         f"{self.pracPct:.2f}", f"{self.pracEq:.2f}",
                                         f"{self.assignPct:.2f}", f"{self.assEq:.2f}",
                                         f"{self.exPct:.2f}", f"{self.exEq:.2f}",
                                         f"{self.attendPct:.2f}", f"{self.atnEq:.2f}",
                                         f"{self.recPct:.2f}", f"{self.recEq:.2f}",
                                         f"{self.attPct:.2f}", f"{self.attEq:.2f}",
                                         f"{self.overEq:.2f}", f"{self.grade_text}",
                                         acntN, subjC, term, studId)
                                    )

                                    con.commit()

                                    self.msgBoxInfo(
                                        f"Student ID: {studId} - {lastN}, {firstN} {midN} Data has been Modified/Updated")

                                    con.close()

                                else:
                                    cur.execute(
                                        "INSERT INTO finalLoadData (accountName, subjectCode, term, studentID, lastName, firstName, middleName, "
                                        "quizPct, quizEq, practicalPct, pracitcalEq, assPct, assEq, exPct, exEq, "
                                        "atnPct, atnEq, rctPct, rctEq, atdPct, atdEq, overallEq, Grade) "
                                        "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                        (
                                            acntN, subjC, term, studId, lastN,
                                            firstN, midN,
                                            f"{self.qzPct:.2f}",
                                            f"{self.quizEq:.2f}",
                                            f"{self.pracPct:.2f}",
                                            f"{self.pracEq:.2f}",
                                            f"{self.assignPct:.2f}",
                                            f"{self.assEq:.2f}",
                                            f"{self.exPct:.2f}", f"{self.exEq:.2f}",
                                            f"{self.attendPct:.2f}",
                                            f"{self.atnEq:.2f}",
                                            f"{self.recPct:.2f}",
                                            f"{self.recEq:.2f}",
                                            f"{self.attPct:.2f}",
                                            f"{self.attEq:.2f}",
                                            f"{self.overEq:.2f}",
                                            f"{self.grade_text}")
                                    )

                                    con.commit()

                                    self.msgBoxInfo(
                                        f"Student ID: {studId} - {lastN}, {firstN} {midN} Successfully Added")

                                    con.close()

                            except sqlite3.Error as e:
                                print("Error SnI inserting data into the database: ", e)

                            self.msgBoxInfo(
                                "Informing that Percentage Criteria reached 100%")

                        else:
                            self.msgBoxWarn(
                                "The Percentage of Criteria must be at 100%, Please modify your Percentage/s")

                    else:
                        pass

                    self.msgBoxInfo(f"Student ID: {studId} - {lastN}, {firstN} {midN} is Successfully Added")

            con.close()


        except Exception as e:
            print("error SnI : ", str(e))
            self.msgBoxWarn("Invalid Data Input")
    def enablefunc(self):
        self.quizChk.stateChanged.connect(self.enbquiz)
        self.assignCHK.stateChanged.connect(self.enblassgn)
        self.prChk.stateChanged.connect(self.enblprac)

        self.prelim.stateChanged.connect(self.examfunc)
        self.atnChk.stateChanged.connect(self.atnfunc)
        self.rctChk.stateChanged.connect(self.rctfunc)
        self.atdChk.stateChanged.connect(self.atdfunc)
    def enbquiz(self, state):
        self.q1.setEnabled(state == 2)
        self.q2.setEnabled(state == 2)
        self.q3.setEnabled(state == 2)
        self.q4.setEnabled(state == 2)

        self.assPct1_3.setEnabled(self.quizChk.isChecked())
        self.qL1.setEnabled(self.q1.isChecked() and self.quizChk.isChecked())
        self.pctQ1.setEnabled(self.q1.isChecked() and self.quizChk.isChecked())
        self.qL2.setEnabled(self.q2.isChecked() and self.quizChk.isChecked())
        self.pctQ2.setEnabled(self.q2.isChecked() and self.quizChk.isChecked())
        self.qL3.setEnabled(self.q3.isChecked() and self.quizChk.isChecked())
        self.pctQ3.setEnabled(self.q3.isChecked() and self.quizChk.isChecked())
        self.qL4.setEnabled(self.q4.isChecked() and self.quizChk.isChecked())
        self.pctQ4.setEnabled(self.q4.isChecked() and self.quizChk.isChecked())

        self.qL1.clear()
        self.qL2.clear()
        self.qL3.clear()
        self.qL4.clear()
        self.pctQ1.clear()
        self.pctQ2.clear()
        self.pctQ3.clear()
        self.pctQ4.clear()
        self.assPct1_3.clear()

        self.q1.stateChanged.connect(lambda state: self.enbline(self.q1, self.qL1, self.pctQ1))
        self.q2.stateChanged.connect(lambda state: self.enbline(self.q2, self.qL2, self.pctQ2))
        self.q3.stateChanged.connect(lambda state: self.enbline(self.q3, self.qL3, self.pctQ3))
        self.q4.stateChanged.connect(lambda state: self.enbline(self.q4, self.qL4, self.pctQ4))

    def enblassgn(self, state):
        self.assign1.setEnabled(state == 2)
        self.assign2.setEnabled(state == 2)
        self.assign3.setEnabled(state == 2)
        self.assign4.setEnabled(state == 2)

        self.assPct1_2.setEnabled(self.assignCHK.isChecked())
        self.assL1.setEnabled(self.assign1.isChecked() and self.assignCHK.isChecked())
        self.assL2.setEnabled(self.assign2.isChecked() and self.assignCHK.isChecked())
        self.assL3.setEnabled(self.assign3.isChecked() and self.assignCHK.isChecked())
        self.assL4.setEnabled(self.assign4.isChecked() and self.assignCHK.isChecked())
        self.assPct1.setEnabled(self.assign1.isChecked() and self.assignCHK.isChecked())
        self.assPct2.setEnabled(self.assign2.isChecked() and self.assignCHK.isChecked())
        self.assPct3.setEnabled(self.assign3.isChecked() and self.assignCHK.isChecked())
        self.assPct4.setEnabled(self.assign4.isChecked() and self.assignCHK.isChecked())

        self.assL1.clear()
        self.assL2.clear()
        self.assL3.clear()
        self.assL4.clear()
        self.assPct1.clear()
        self.assPct2.clear()
        self.assPct3.clear()
        self.assPct4.clear()
        self.assPct1_2.clear()

        self.assign1.stateChanged.connect(lambda state: self.enbline(self.assign1, self.assL1, self.assPct1))
        self.assign2.stateChanged.connect(lambda state: self.enbline(self.assign2, self.assL2, self.assPct2))
        self.assign3.stateChanged.connect(lambda state: self.enbline(self.assign3, self.assL3, self.assPct3))
        self.assign4.stateChanged.connect(lambda state: self.enbline(self.assign4, self.assL4, self.assPct4))

    def enblprac(self, state):
        self.pr1.setEnabled(state == 2)
        self.pr2.setEnabled(state == 2)
        self.pr3.setEnabled(state == 2)
        self.pr4.setEnabled(state == 2)

        self.assPct1_4.setEnabled(self.prChk.isChecked())
        self.prL1.setEnabled(self.pr1.isChecked() and self.prChk.isChecked())
        self.prL2.setEnabled(self.pr2.isChecked() and self.prChk.isChecked())
        self.prL3.setEnabled(self.pr3.isChecked() and self.prChk.isChecked())
        self.prL4.setEnabled(self.pr4.isChecked() and self.prChk.isChecked())
        self.prL1pct.setEnabled(self.pr1.isChecked() and self.prChk.isChecked())
        self.prL2pct.setEnabled(self.pr2.isChecked() and self.prChk.isChecked())
        self.prL3pct.setEnabled(self.pr3.isChecked() and self.prChk.isChecked())
        self.prL4pct.setEnabled(self.pr4.isChecked() and self.prChk.isChecked())

        self.prL1.clear()
        self.prL2.clear()
        self.prL3.clear()
        self.prL4.clear()
        self.prL1pct.clear()
        self.prL2pct.clear()
        self.prL3pct.clear()
        self.prL4pct.clear()
        self.assPct1_4.clear()

        self.pr1.stateChanged.connect(lambda state: self.enbline(self.pr1, self.prL1, self.prL1pct))
        self.pr2.stateChanged.connect(lambda state: self.enbline(self.pr2, self.prL2, self.prL2pct))
        self.pr3.stateChanged.connect(lambda state: self.enbline(self.pr3, self.prL3, self.prL3pct))
        self.pr4.stateChanged.connect(lambda state: self.enbline(self.pr4, self.prL4, self.prL4pct))

    def examfunc(self, state):
        self.checkBox.setEnabled(state == 2)
        self.checkBox_2.setEnabled(state == 2)
        self.assPct1_5.setEnabled(self.prelim.isChecked())

        self.checkBox.stateChanged.connect(
            lambda state: self.enbline1(self.checkBox, self.exPrL, self.exPrPct, self.prPct))
        self.checkBox_2.stateChanged.connect(
            lambda state: self.enbline1(self.checkBox_2, self.exWrL, self.exWrPct, self.wrPct))

        self.assPct1_5.clear()
        self.exPrL.clear()
        self.exWrL.clear()
        self.exPrPct.clear()
        self.exWrPct.clear()
        self.prPct.clear()
        self.wrPct.clear()

    def atnfunc(self):
        self.atn1.setEnabled(self.atnChk.isChecked())
        self.atn1Pct.setEnabled(self.atnChk.isChecked())
        self.atnPct.setEnabled(self.atnChk.isChecked())

        self.atn1.clear()
        self.atn1Pct.clear()
        self.atnPct.clear()

    def rctfunc(self):
        self.rct1.setEnabled(self.rctChk.isChecked())
        self.rct1Pct.setEnabled(self.rctChk.isChecked())
        self.rctPct.setEnabled(self.rctChk.isChecked())

        self.rct1.clear()
        self.rct1Pct.clear()
        self.rctPct.clear()

    def atdfunc(self):
        self.atdPct.setEnabled(self.atdChk.isChecked())
        self.atd1.setEnabled(self.atdChk.isChecked())
        self.atd1Pct.setEnabled(self.atdChk.isChecked())

        self.atd1.clear()
        self.atd1Pct.clear()
        self.atdPct.clear()

    def enbline(self, chkBox, line1, line2):
        line1.setEnabled(chkBox.isChecked())
        line2.setEnabled(chkBox.isChecked())
        line1.clear()
        line2.clear()

    def enbline1(self, chkBox, line1, line2, line3):
        line1.setEnabled(chkBox.isChecked())
        line2.setEnabled(chkBox.isChecked())
        line3.setEnabled(chkBox.isChecked())
        line1.clear()
        line2.clear()
        line3.clear()

    def Back(self):
        self.stackedWidget.setCurrentIndex(0)
    def loadfunc(self):
        try:
            scrName = self.screenName.text()
            sub = self.subjC.text()
            term = self.term.text()
            studId = self.studID.text()

            if not studId:
                self.msgBoxWarn("Kindly Provide a Student ID")
                return

            elif studId.isalpha():
                self.msgBoxWarn("Kindly Provide a Student ID in Numeric Format")
                return

            con = sqlite3.connect("hmp.db")
            cur = con.cursor()
            cur.execute(
                f"SELECT * FROM loadData WHERE accountName = ? AND subjectCode = ? AND Term = ? AND studentID = ?",
                (scrName, sub, term, studId))

            result = cur.fetchone()

            if result:
                cur.execute(
                    f"SELECT QuizPct, Quiz1, Quiz11, Quiz2, Quiz22, Quiz3, Quiz33, Quiz4, Quiz44, "
                    f"AssPct, Ass1, Ass11, Ass2, Ass22, Ass3, Ass33, Ass4, Ass44,"
                    f"PracPct, Prac1, Prac11, Prac2, Prac22, Prac3, Prac33, Prac4, Prac44,"
                    f"ExamPct, ePr1, ePr2, eWr1, eWr2,"
                    f"atnpct, atn1, atn11,"
                    f"rctpct, rct1, rct11,"
                    f"atdpct, atd1, atd11, prPct, wrPct "
                    f"FROM loadData WHERE accountName = ? AND subjectCode = ? AND Term = ? AND studentID = ?",
                    (scrName, sub, term, studId))

                result1 = cur.fetchone()

                if result1:

                    if result1[0] is not None and result1[0] != "":
                        self.assPct1_3.setEnabled(True)
                        self.quizChk.setChecked(True)
                        self.assPct1_3.setText(result1[0])

                    if result1[1] is not None and result1[1] != "":
                        self.qL1.setEnabled(True)
                        self.pctQ1.setEnabled(True)
                        self.q1.setChecked(True)
                        self.qL1.setText(result1[1])
                        self.pctQ1.setText(result1[2])

                    if result1[3] is not None and result1[3] != "":
                        self.qL2.setEnabled(True)
                        self.pctQ2.setEnabled(True)
                        self.q2.setChecked(True)
                        self.qL2.setText(result1[3])
                        self.pctQ2.setText(result1[4])

                    if result1[5] is not None and result1[5] != "":
                        self.qL3.setEnabled(True)
                        self.pctQ3.setEnabled(True)
                        self.q3.setChecked(True)
                        self.qL3.setText(result1[5])
                        self.pctQ3.setText(result1[6])

                    if result1[7] is not None and result1[7] != "":
                        self.qL4.setEnabled(True)
                        self.pctQ4.setEnabled(True)
                        self.q4.setChecked(True)
                        self.qL4.setText(result1[7])
                        self.pctQ4.setText(result1[8])

                    if result1[9] is not None and result1[9] != "":
                        self.assPct1_2.setEnabled(True)
                        self.assignCHK.setChecked(True)
                        self.assPct1_2.setText(result1[9])

                    if result1[10] is not None and result1[10] != "":
                        self.assL1.setEnabled(True)
                        self.assPct1.setEnabled(True)
                        self.assign1.setChecked(True)
                        self.assL1.setText(result1[10])
                        self.assPct1.setText(result1[11])

                    if result1[12] is not None and result1[12] != "":
                        self.assL2.setEnabled(True)
                        self.assPct2.setEnabled(True)
                        self.assign2.setChecked(True)
                        self.assL2.setText(result1[12])
                        self.assPct2.setText(result1[13])

                    if result1[14] is not None and result1[14] != "":
                        self.assL3.setEnabled(True)
                        self.assPct3.setEnabled(True)
                        self.assign3.setChecked(True)
                        self.assL3.setText(result1[14])
                        self.assPct3.setText(result1[15])

                    if result1[16] is not None and result1[16] != "":
                        self.assL4.setEnabled(True)
                        self.assPct4.setEnabled(True)
                        self.assign4.setChecked(True)
                        self.assL4.setText(result1[16])
                        self.assPct4.setText(result1[17])

                    if result1[18] is not None and result1[18] != "":
                        self.assPct1_4.setEnabled(True)
                        self.prChk.setChecked(True)
                        self.assPct1_4.setText(result1[18])

                    if result1[19] is not None and result1[19] != "":
                        self.prL1.setEnabled(True)
                        self.prL1pct.setEnabled(True)
                        self.pr1.setChecked(True)
                        self.prL1.setText(result1[19])
                        self.prL1pct.setText(result1[20])

                    if result1[21] is not None and result1[21] != "":
                        self.prL2.setEnabled(True)
                        self.prL2pct.setEnabled(True)
                        self.pr2.setChecked(True)
                        self.prL2.setText(result1[21])
                        self.prL2pct.setText(result1[22])

                    if result1[23] is not None and result1[23] != "":
                        self.prL3.setEnabled(True)
                        self.prL3pct.setEnabled(True)
                        self.pr3.setChecked(True)
                        self.prL3.setText(result1[23])
                        self.prL3pct.setText(result1[24])

                    if result1[25] is not None and result1[25] != "":
                        self.prL4.setEnabled(True)
                        self.prL4pct.setEnabled(True)
                        self.pr4.setChecked(True)
                        self.prL4.setText(result1[25])
                        self.prL4pct.setText(result1[26])

                    if result1[27] is not None and result1[27] != "":
                        self.assPct1_5.setEnabled(True)
                        self.prelim.setChecked(True)
                        self.assPct1_5.setText(result1[27])

                    if result1[28] is not None and result1[28] != "":
                        self.checkBox.setChecked(True)
                        self.exPrL.setEnabled(True)
                        self.exPrPct.setEnabled(True)
                        self.exPrL.setText(result1[28])
                        self.exPrPct.setText(result1[29])
                        self.prPct.setText(result1[41])

                    if result1[30] is not None and result1[30] != "":
                        self.checkBox_2.setChecked(True)
                        self.exWrL.setEnabled(True)
                        self.exWrPct.setEnabled(True)
                        self.exWrL.setText(result1[30])
                        self.exWrPct.setText(result1[31])
                        self.wrPct.setText(result1[42])

                    if result1[32] is not None and result1[32] != "":
                        self.atnChk.setChecked(True)
                        self.atnPct.setText(result1[32])
                        self.atn1.setText(result1[33])
                        self.atn1Pct.setText(result1[34])

                    if result1[35] is not None and result1[35] != "":
                        self.rctChk.setChecked(True)
                        self.rctPct.setText(result1[35])
                        self.rct1.setText(result1[36])
                        self.rct1Pct.setText(result1[37])

                    if result1[38] is not None and result1[38] != "":
                        self.atdChk.setChecked(True)
                        self.atdPct.setText(result1[38])
                        self.atd1.setText(result1[39])
                        self.atd1Pct.setText(result1[40])

                    self.msgBoxInfo("Successfully Loaded")
                    if self.showInfo == QMessageBox.Ok:
                        self.showOverview()

                con.close()

            else:
                self.msgBoxWarn("No Data Found. Provide Raw Score first then Compute and Save it")

                con.close()

        except Exception as e:
            print("error loadfunct: ", str(e))

    def xport2xcel(self):
        try:
            df = pd.DataFrame()
            subjC = self.subjC.text()
            term = self.term.text()

            header = [self.studentTbl.horizontalHeaderItem(col).text() for col in
                      range(self.studentTbl.columnCount())]
            df = pd.DataFrame(columns=header)

            for row in range(self.studentTbl.rowCount()):
                row_data = [self.studentTbl.item(row, col).text() for col in
                            range(self.studentTbl.columnCount())]
                df.loc[len(df)] = row_data

            docsPath = os.path.expanduser("~/Documents")

            file_path, _ = QFileDialog.getSaveFileName(self.centralwidget, "Save File", docsPath,
                                                       "Excel Files (*.xlsx);;All Files (*)")

            if file_path:
                df.to_excel(file_path, index=False)
                print(f"Data exported to {file_path}")
                self.msgBoxInfo(f"The {subjC} - {term} Table has been exported")

        except Exception as e:
            print("Error in exporting: ", str(e))
    def removefunc(self):
        slctItems = self.studentTbl.selectedItems()
        if slctItems:
            slctd_row = slctItems[0].row()
            self.studentTbl.removeRow(slctd_row)
        else:
            self.msgBoxWarn("Please select a Row")

    # ====================================HOMEPAGE FUNCTION=============================================================

    # ====================================POP-UP FORM (SELECTION) FUNCTION=========================================================
    def dialog(self):
        self.Form = QtWidgets.QDialog()
        self.uiForm = Ui_Form()
        self.uiForm.setupUi(self.Form)
        self.Form.setModal(True)
        self.Form.show()

        self.uiForm.formStacked.setCurrentIndex(0)
        self.connectDB1()
        self.connectfunc()
    def connectfunc(self):
        self.uiForm.submitbtn.clicked.connect(self.createSubDB)
        self.uiForm.proceedbtn.clicked.connect(self.selectSubDB)
        # self.uiForm.selectCmb.currentIndexChanged.connect(self.selectTerm)

        self.uiForm.prelimbtn.toggled.connect(lambda: self.selectTerm(self.uiForm.prelimbtn, "PRELIMINARY"))
        self.uiForm.midbtn.toggled.connect(lambda: self.selectTerm(self.uiForm.midbtn, "MIDTERM"))
        self.uiForm.finalbtn.toggled.connect(lambda: self.selectTerm(self.uiForm.finalbtn, "FINAL"))
    def selectTerm(self, radBtn, term):
        if radBtn.isChecked():
            self.Term = term
        else:
            pass
    def createSubDB(self):
        table_name = self.uiForm.subjL.text().strip()
        acntN = self.screenName.text()
        try:
            if table_name:

                conn = sqlite3.connect('hmp.db')
                cursor = conn.cursor()

                cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name=?;", (table_name,))
                existing_table = cursor.fetchone()

                if existing_table:

                    cursor.execute(f"SELECT * FROM {table_name} WHERE Term = ?", (self.Term,))
                    result = cursor.fetchone()

                    if result:

                        self.msgBoxInfo(f"The Subject Code : '{table_name}' - '{self.Term}' is already Exist")

                        if self.showInfo == QMessageBox.Ok or self.showInfo == QMessageBox.Yes:
                            self.uiForm.formStacked.setCurrentIndex(2)
                        else:
                            pass

                    else:

                        cursor.execute(f"INSERT INTO {table_name} (accountName, SubjectCode, Term) VALUES (?,?,?)",
                                       (acntN, table_name, self.Term))

                        conn.commit()

                        self.msgBoxInfo("Saved Successfully")

                        if self.showInfo == QMessageBox.Ok or self.showInfo == QMessageBox.Yes:
                            self.subjC1.setText(table_name)
                            self.subjC.setText(table_name)
                            self.term.setText(self.Term)
                            self.prelim.setText(self.Term)
                            self.Form.close()
                        pass

                else:
                    if not self.uiForm.prelimbtn.isChecked() and not self.uiForm.midbtn.isChecked() and not self.uiForm.finalbtn.isChecked():
                        self.msgBoxWarn("Please select a term (Prelim, Midterm, or Final).")
                    else:

                        cursor.execute(f"CREATE TABLE {table_name} "
                                       f"(accountName TEXT NOT NULL, "
                                       f"SubjectCode TEXT NOT NULL, "
                                       f"Term TEXT NOT NULL);")
                        conn.commit()

                        cursor.execute(f"INSERT INTO {table_name} (accountName, SubjectCode, Term) VALUES (?,?,?)",
                                       (acntN, table_name, self.Term))

                        conn.commit()

                        self.msgBoxInfo("Saved Successfully")
                        if self.showInfo == QMessageBox.Ok or self.showInfo == QMessageBox.Yes:
                            self.subjC1.setText(table_name)
                            self.subjC.setText(table_name)
                            self.prelim.setText(self.Term)
                            self.term.setText(self.Term)
                            self.Form.close()

                self.clearfunc()

                conn.close()


            else:
                self.msgBoxWarn("Fill empty filled")
        except Exception as e:
            print("error in create sub : ", str(e))
            self.msgBoxWarn("Kindly remove non-alphabet(ex.-,(),{}...")
    def connectDB1(self):
        conn = sqlite3.connect("hmp.db")
        if not conn:
            print("Database connection error")
            sys.exit(1)

        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        all_tables = [row[0] for row in cur.fetchall()]

        if "userAccount" in all_tables:
            all_tables.remove("userAccount")
        if "studentInfo" in all_tables:
            all_tables.remove("studentInfo")
        if "loadData" in all_tables:
            all_tables.remove("loadData")
        if "finalLoadData" in all_tables:
            all_tables.remove("finalLoadData")

        for table_name in all_tables:
            self.uiForm.selectCmb.addItem(table_name)

        self.uiForm.selectCmb.currentIndexChanged.connect(self.selectTermDB)
    def selectTermDB(self):
        conn = sqlite3.connect("hmp.db")
        cur = conn.cursor()

        name = self.uiForm.selectCmb.currentText()

        self.uiForm.comboBox.clear()

        query = f"SELECT DISTINCT Term FROM {name};"

        cur.execute(query)
        unique_values = cur.fetchall()

        for value in unique_values:
            self.uiForm.comboBox.addItem(str(value[0]))

        conn.close()
    def selectSubDB(self):
        try:
            subjCode = self.uiForm.selectCmb.currentText()
            term = self.uiForm.comboBox.currentText()
            con = sqlite3.connect("hmp.db")
            cur = con.cursor()
            cur.execute(f"SELECT * FROM {subjCode} WHERE Term = ?", (term,))
            result = cur.fetchone()

            if result:
                self.term1.setText(f"{term} - TERM")
                self.subjC1.setText(subjCode)
                self.subjC.setText(subjCode)
                self.prelim.setText(term)
                self.term.setText(term)
                self.stackedWidget.setCurrentIndex(0)
                self.Form.close()

                self.clearfunc()

            else:
                self.msgBoxWarn(f"There is no existing '{subjCode}' - '{term}', must create first")
                if self.showWarn == QMessageBox.Ok or self.showWarn == QMessageBox.Yes:
                    self.uiForm.formStacked.setCurrentIndex(1)
                else:
                    pass

            con.close()
        except Exception as e:
            self.msgBoxWarn("Error : ", str(e))
    def clearfunc(self):
        self.studID.clear()
        self.lastN.clear()
        self.firstN.clear()
        self.MidN.clear()
        self.quizChk.setChecked(False)
        self.assignCHK.setChecked(False)
        self.prChk.setChecked(False)
        self.atnChk.setChecked(False)
        self.rctChk.setChecked(False)
        self.atdChk.setChecked(False)
        self.prelim.setChecked(False)
    # ====================================POP-UP FORM (OVERVIEW) FUNCTION=========================================================
    def showOverview(self):

        self.over = QtWidgets.QDialog()
        self.uiOver = over_Form()
        self.uiOver.overviewForm(self.over)
        self.over.setModal(True)

        self.studentOver()
        self.computeOverQz()
        self.computeOverAss()
        self.computeOverPrac()
        self.computeOverEx()
        self.computeOverAtn()
        self.computeOveRct()
        self.computeOveAtd()
        self.overall()
        self.uiOver.pushButton.clicked.connect(self.savefunc)
    def studentOver(self):
        try:
            studId = self.studID.text()
            lname = self.lastN.text()
            fname = self.firstN.text()
            mname = self.MidN.text()

            self.uiOver.studTableF.setRowCount(0)

            row_position = self.uiOver.studTableF.rowCount()
            self.uiOver.studTableF.insertRow(row_position)

            self.uiOver.studTableF.setItem(row_position, 0, QTableWidgetItem(studId))
            self.uiOver.studTableF.setItem(row_position, 1, QTableWidgetItem(lname))
            self.uiOver.studTableF.setItem(row_position, 2, QTableWidgetItem(fname))
            self.uiOver.studTableF.setItem(row_position, 3, QTableWidgetItem(mname))
        except Exception as e:
            print("error in student info populate: ", str(e))
    def computeOverQz(self):
        try:
            if self.quizChk.isChecked():
                q1 = self.qL1.text() or '0'
                q2 = self.qL2.text() or '0'
                q3 = self.qL3.text() or '0'
                q4 = self.qL4.text() or '0'

                qT1 = self.pctQ1.text() or '0'
                qT2 = self.pctQ2.text() or '0'
                qT3 = self.pctQ3.text() or '0'
                qT4 = self.pctQ4.text() or '0'

                qPct = self.assPct1_3.text() or '0'

                chckB = self.quizChk.text()

                if (q1 and q2 and q3 and q3 and q4 and qT1 and qT2 and qT3 and qT4 and qPct):
                    numQ1 = float(q1)
                    numQ2 = float(q2)
                    numQ3 = float(q3)
                    numQ4 = float(q4)

                    numQP1 = float(qT1)
                    numQP2 = float(qT2)
                    numQP3 = float(qT3)
                    numQP4 = float(qT4)

                    numQPct = float(qPct)

                    if self.quizChk.isChecked() and numQPct == 0:
                        self.msgBoxWarn(f"Percentage in checked {chckB} zero is not allowed.")
                    elif self.quizChk.isChecked() and numQP1 == 0 and numQP2 == 0 and numQP3 == 0 and numQP4 == 0:
                        self.msgBoxWarn(f"Denominator Zero (ex. 50/0) in {chckB} is not allowed.")
                    elif self.quizChk.isChecked() and not self.studID.text():
                        self.msgBoxWarn("Please provide a Student ID")
                    else:
                        self.over.show()
                        total = numQ1 + numQ2 + numQ3 + numQ4
                        total2 = numQP1 + numQP2 + numQP3 + numQP4
                        total3 = total / total2
                        result = total3 * numQPct

                        self.uiOver.qF1.setText(f"{q1}/{qT1}")
                        self.uiOver.qF2.setText(f"{q2}/{qT2}")
                        self.uiOver.qF3.setText(f"{q3}/{qT3}")
                        self.uiOver.qF4.setText(f"{q4}/{qT4}")
                        self.uiOver.qT.setText(f"{total}/{total2}")
                        self.uiOver.qTE.setText(f"{total3 * 100:.2f}")
                        self.uiOver.qPF.setText(f"{chckB} Percentage = {result:.2f}%/{qPct}%")

                        self.quiz = numQ1 + numQ2 + numQ3 + numQ4
                        self.quiz1 = numQP1 + numQP2 + numQP3 + numQP4


                        self.qzPct = result
                        self.quizEq = total3 * 100
                        self.qzPct1 = numQPct


            else:
                self.qzPct1 = 0.00
                self.qzPct = 0.00
                self.quizEq = 0.00
        except:
            self.msgBoxWarn(f"Please input only a digit in {chckB}")
    def computeOverAss(self):
        try:
            if self.assignCHK.isChecked():
                q1 = self.assL1.text() or '0'
                q2 = self.assL2.text() or '0'
                q3 = self.assL3.text() or '0'
                q4 = self.assL4.text() or '0'

                qT1 = self.assPct1.text() or '0'
                qT2 = self.assPct2.text() or '0'
                qT3 = self.assPct3.text() or '0'
                qT4 = self.assPct4.text() or '0'

                qPct = self.assPct1_2.text() or '0'

                chckB = self.assignCHK.text()

                if (q1 and q2 and q3 and q3 and q4 and qT1 and qT2 and qT3 and qT4 and qPct):
                    numQ1 = float(q1)
                    numQ2 = float(q2)
                    numQ3 = float(q3)
                    numQ4 = float(q4)

                    numQP1 = float(qT1)
                    numQP2 = float(qT2)
                    numQP3 = float(qT3)
                    numQP4 = float(qT4)

                    numQPct = float(qPct)

                    if self.assignCHK.isChecked() and numQPct == 0:
                        self.msgBoxWarn(f"Percentage in checked {chckB} zero is not allowed.")
                    elif self.assignCHK.isChecked() and numQP1 == 0 and numQP2 == 0 and numQP3 == 0 and numQP4 == 0:
                        self.msgBoxWarn(f"Denominator Zero (ex. 50/0) in {chckB} is not allowed.")
                    elif self.assignCHK.isChecked() and not self.studID.text():
                        self.msgBoxWarn("Please provide a Student ID")
                    else:
                        self.over.show()
                        total = numQ1 + numQ2 + numQ3 + numQ4
                        total2 = numQP1 + numQP2 + numQP3 + numQP4
                        total3 = total / total2
                        result = total3 * numQPct

                        self.uiOver.assF1.setText(f"{q1}/{qT1}")
                        self.uiOver.assF2.setText(f"{q2}/{qT2}")
                        self.uiOver.assF3.setText(f"{q3}/{qT3}")
                        self.uiOver.assF4.setText(f"{q4}/{qT4}")
                        self.uiOver.assT.setText(f"{total}/{total2}")
                        self.uiOver.assTE.setText(f"{total3 * 100:.2f}")
                        self.uiOver.assPF.setText(f"{chckB} Percentage = {result:.2f}%/{qPct}%")

                        self.ass = numQ1 + numQ2 + numQ3 + numQ4
                        self.ass1 = numQP1 + numQP2 + numQP3 + numQP4

                        self.assignPct = result
                        self.assEq = total3 * 100
                        self.assignPct1 = numQPct


            else:
                self.assignPct1 = 0.00
                self.assignPct = 0.00
                self.assEq = 0.00
        except:
            self.msgBoxWarn(f"Please input only a digit in {chckB}")
    def computeOverPrac(self):

        try:
            if self.prChk.isChecked():

                q1 = self.prL1.text() or '0'
                q2 = self.prL2.text() or '0'
                q3 = self.prL3.text() or '0'
                q4 = self.prL4.text() or '0'

                qT1 = self.prL1pct.text() or '0'
                qT2 = self.prL2pct.text() or '0'
                qT3 = self.prL3pct.text() or '0'
                qT4 = self.prL4pct.text() or '0'

                qPct = self.assPct1_4.text() or '0'

                chckB = self.prChk.text()

                if (q1 and q2 and q3 and q3 and q4 and qT1 and qT2 and qT3 and qT4 and qPct):
                    numQ1 = float(q1)
                    numQ2 = float(q2)
                    numQ3 = float(q3)
                    numQ4 = float(q4)

                    numQP1 = float(qT1)
                    numQP2 = float(qT2)
                    numQP3 = float(qT3)
                    numQP4 = float(qT4)

                    numQPct = float(qPct)

                    if self.prChk.isChecked() and numQPct == 0:
                        self.msgBoxWarn(f"Percentage in checked {chckB} zero is not allowed.")
                    elif self.prChk.isChecked() and numQP1 == 0 and numQP2 == 0 and numQP3 == 0 and numQP4 == 0:
                        self.msgBoxWarn(f"Denominator Zero (ex. 50/0) in {chckB} is not allowed.")
                    elif self.prChk.isChecked() and not self.studID.text():
                        self.msgBoxWarn("Please provide a Student ID")
                    else:
                        self.over.show()
                        total = numQ1 + numQ2 + numQ3 + numQ4
                        total2 = numQP1 + numQP2 + numQP3 + numQP4
                        total3 = total / total2
                        result = total3 * numQPct

                        self.uiOver.pracF1.setText(f"{q1}/{qT1}")
                        self.uiOver.pracF2.setText(f"{q2}/{qT2}")
                        self.uiOver.pracF3.setText(f"{q3}/{qT3}")
                        self.uiOver.pracF4.setText(f"{q4}/{qT4}")
                        self.uiOver.pracT.setText(f"{total}/{total2}")
                        self.uiOver.pracTE.setText(f"{total3 * 100:.2f}")
                        self.uiOver.pracPF.setText(f"{chckB} Percentage = {result:.2f}%/{qPct}%")

                        self.prac = numQ1 + numQ2 + numQ3 + numQ4
                        self.prac1 = numQP1 + numQP2 + numQP3 + numQP4

                        self.pracPct = result
                        self.pracEq = total3 * 100
                        self.pracPct1 = numQPct


                else:
                    pass
            else:
                self.pracPct1 = 0.00
                self.pracPct = 0.00
                self.pracEq = 0.00
        except:
            self.msgBoxWarn(f"Please input only a digit in {chckB}")
    def computeOverEx(self):
        try:
            if self.prelim.isChecked():
                q1 = self.exPrL.text() or '0'
                q11 = self.exPrPct.text() or '0'
                q111 = self.prPct.text() or '0'

                q2 = self.exWrL.text() or '0'
                q22 = self.exWrPct.text() or '0'
                q222 = self.wrPct.text() or '0'

                qPct = self.assPct1_5.text() or '0'

                pract = self.checkBox.text()
                writt = self.checkBox_2.text()

                chckB = self.prelim.text()

                if (q1 and q11 and q111 and q2 and q22 and q222 and qPct):
                    numQ1 = float(q1)
                    numQ11 = float(q11)
                    numQ111 = float(q111)
                    numQ2 = float(q2)
                    numQ22 = float(q22)
                    numQ222 = float(q222)

                    numQPct = float(qPct)

                    if self.prelim.isChecked() and numQPct == 0:
                        self.msgBoxWarn(f"Percentage Zero in checked {chckB} is not allowed.")
                    elif self.prelim.isChecked() and numQ11 == 0 and numQ22 == 0:
                        self.msgBoxWarn(f"Denominator Zero (ex. 50/0) in {chckB} is not allowed.")
                    elif self.prelim.isChecked() and not self.studID.text():
                        self.msgBoxWarn("Please provide a Student ID")
                    elif self.checkBox.isChecked() and not self.checkBox_2.isChecked() and numQ111 != 100:
                        self.msgBoxWarn(f"{pract} be must equal to 100%")
                    elif self.checkBox_2.isChecked() and not self.checkBox.isChecked() and numQ222 != 100:
                        self.msgBoxWarn(f"{writt} must be equal to 100%")
                    elif self.checkBox_2.isChecked() and self.checkBox.isChecked() and numQ222 + numQ111 != 100:
                        self.msgBoxWarn(f"The sum of {pract} and {writt} must be equal to 100%")

                    elif self.checkBox.isChecked() and self.checkBox_2.isChecked() and numQ222 + numQ111 == 100:
                        prac = numQ1 / numQ11
                        value1 = prac * numQ111

                        writ = numQ2 / numQ22
                        value2 = writ * numQ222

                        pct = value1 + value2

                        value3 = numQPct / 100

                        Tpct = pct * value3

                        num = numQ1 + numQ2
                        denum = numQ11 + numQ22

                        self.uiOver.weF.setText(f"{q1}/{q11}")
                        self.uiOver.peF.setText(f"{q2}/{q22}")
                        self.uiOver.peF_2.setText(f"{num}/{denum}")

                    elif self.checkBox.isChecked() and not self.checkBox_2.isChecked() and numQ111 == 100:
                        prac = numQ1 / numQ11
                        pct = prac * numQ111

                        value3 = numQPct / 100

                        Tpct = pct * value3


                        self.uiOver.peF.setText(f"{q1}/{q11}")
                        self.uiOver.peF_2.setText(f"{numQ1}/{numQ11}")

                    elif not self.checkBox.isChecked() and self.checkBox_2.isChecked() and numQ222 == 100:
                        wri = numQ2 / numQ22
                        pct = wri * numQ222

                        value3 = numQPct / 100

                        Tpct = pct * value3

                        self.uiOver.weF.setText(f"{q2}/{q22}")
                        self.uiOver.peF_2.setText(f"{numQ2}/{numQ22}")


                    self.uiOver.peE.setText(f"{pct:.2f}")
                    self.uiOver.exPF.setText(f"Exam Percentage = {Tpct:.2f}%/{qPct}%")

                    self.exPct = Tpct
                    self.exEq = pct
                    self.exPct1 = numQPct

                    self.over.show()

            else:
                self.exPct1 = 0.00
                self.exPct1 = 0.00
                self.exPct = 0.00
                self.exEq = 0.00
        except Exception as e:
            print("error in exam :", str(e))
    def computeOverAtn(self):
        try:
            if self.atnChk.isChecked():
                q1 = self.atn1.text() or '0'
                q2 = self.atn1Pct.text() or '0'

                q3 = self.atnPct.text() or '0'

                chckB = self.atnChk.text()

                if (q1 and q2 and q3 and q3):
                    numQ1 = float(q1)
                    numQ2 = float(q2)
                    numQ3 = float(q3)

                    if self.atnChk.isChecked() and q3 == 0:
                        self.msgBoxWarn(f"Percentage of {chckB} zero is not allowed.")
                    elif self.atnChk.isChecked() and numQ3 == 0:
                        self.msgBoxWarn(f"Denominator Zero (ex. 50/0) in {chckB} is not allowed.")
                    elif self.atnChk.isChecked() and not self.studID.text():
                        self.msgBoxWarn("Please provide a Student ID")
                    else:
                        self.over.show()
                        total = numQ1 / numQ2
                        result1 = total * numQ3

                        self.uiOver.atnF.setText(f"{q1}/{q2}")
                        self.uiOver.atdE.setText(f"{total * 100:.2f}")
                        self.uiOver.oPF.setText(f"{chckB} Percentage = {result1:.2f}%/{q3}%")

                        self.attendPct = result1
                        self.atnEq = total * 100

                        self.attendPct1 = numQ3


            else:
                self.attendPct1 = 0.00
                self.attendPct = 0.00
                self.atnEq = 0.00
        except:
            self.msgBoxWarn(f"Please input only a digit in {chckB}")
    def computeOveRct(self):
        try:
            if self.rctChk.isChecked():
                q1 = self.rct1.text() or '0'
                q2 = self.rct1Pct.text() or '0'

                q3 = self.rctPct.text() or '0'

                chckB = self.rctChk.text()

                if (q1 and q2 and q3 and q3):
                    numQ1 = float(q1)
                    numQ2 = float(q2)
                    numQ3 = float(q3)

                    if self.rctChk.isChecked() and q3 == 0:
                        self.msgBoxWarn(f"Percentage of {chckB} zero is not allowed.")
                    elif self.rctChk.isChecked() and numQ3 == 0:
                        self.msgBoxWarn(f"Denominator Zero (ex. 50/0) in {chckB} is not allowed.")
                    elif self.rctChk.isChecked() and not self.studID.text():
                        self.msgBoxWarn("Please provide a Student ID")
                    else:
                        self.over.show()
                        total = numQ1 / numQ2
                        result2 = total * numQ3
                        self.uiOver.rctF.setText(f"{q1}/{q2}")
                        self.uiOver.rctE.setText(f"{total * 100:.2f}")
                        self.uiOver.oPF_2.setText(f"{chckB} Percentage = {result2:.2f}%/{q3}%")

                        self.recPct = result2
                        self.recEq = total * 100

                        self.recPct1 = numQ3

            else:
                self.recPct1 = 0.00
                self.recPct = 0.00
                self.recEq = 0.00
        except:
            self.msgBoxWarn(f"Please input only a digit in {chckB}")
    def computeOveAtd(self):
        try:
            if self.atdChk.isChecked():
                q1 = self.atd1.text() or '0'
                q2 = self.atd1Pct.text() or '0'

                q3 = self.atdPct.text() or '0'

                chckB = self.atdChk.text()

                if (q1 and q2 and q3 and q3):
                    numQ1 = float(q1)
                    numQ2 = float(q2)
                    numQ3 = float(q3)

                    if self.atdChk.isChecked() and q3 == 0:
                        self.msgBoxWarn(f"Percentage of {chckB} zero is not allowed.")
                    elif self.atdChk.isChecked() and numQ3 == 0:
                        self.msgBoxWarn(f"Denominator Zero (ex. 50/0) in {chckB} is not allowed.")
                    elif self.atdChk.isChecked() and not self.studID.text():
                        self.msgBoxWarn("Please provide a Student ID")
                    else:
                        self.over.show()
                        total = numQ1 / numQ2
                        result3 = total * numQ3

                        self.uiOver.atdF.setText(f"{q1}/{q2}")
                        self.uiOver.atdE_2.setText(f"{total * 100:.2f}")
                        self.uiOver.oPF_3.setText(f"{chckB} Percentage = {result3:.2f}%/{q3}%")

                        self.att = numQ1
                        self.att1 = numQ2
                        self.attPct1 = numQ3


                        self.attPct = result3
                        self.attEq = total * 100


            else:
                self.attPct1 = 0.00
                self.attPct = 0.00
                self.attEq = 0.00
        except:
            self.msgBoxWarn(f"Please input only a digit in {chckB}")
    def overall(self):
        try:
            q1 = self.qL1.text() or '0'
            q2 = self.qL2.text() or '0'
            q3 = self.qL3.text() or '0'
            q4 = self.qL4.text() or '0'
            qT1 = self.pctQ1.text() or '0'
            qT2 = self.pctQ2.text() or '0'
            qT3 = self.pctQ3.text() or '0'
            qT4 = self.pctQ4.text() or '0'

            as1 = self.assL1.text() or '0'
            as2 = self.assL2.text() or '0'
            as3 = self.assL3.text() or '0'
            as4 = self.assL4.text() or '0'
            asT1 = self.assPct1.text() or '0'
            asT2 = self.assPct2.text() or '0'
            asT3 = self.assPct3.text() or '0'
            asT4 = self.assPct4.text() or '0'

            p1 = self.prL1.text() or '0'
            p2 = self.prL2.text() or '0'
            p3 = self.prL3.text() or '0'
            p4 = self.prL4.text() or '0'
            pT1 = self.prL1pct.text() or '0'
            pT2 = self.prL2pct.text() or '0'
            pT3 = self.prL3pct.text() or '0'
            pT4 = self.prL4pct.text() or '0'

            exP1 = self.exPrL.text() or '0'
            exP2 = self.exPrPct.text() or '0'
            exW1 = self.exWrL.text() or '0'
            exW2 = self.exWrPct.text() or '0'

            atn1 = self.atn1.text() or '0'
            atn2 = self.atn1Pct.text() or '0'
            rct1 = self.rct1.text() or '0'
            rct2 = self.rct1Pct.text() or '0'
            atd1 = self.atd1.text() or '0'
            atd2 = self.atd1Pct.text() or '0'

            p = self.prPct.text() or '0'
            w = self.wrPct.text() or '0'
            pct = self.assPct1_5.text() or '0'

            if (q1 and q2 and q3 and q4 and qT1 and qT2 and qT3 and qT4 and as1 and as2 and as3 and as4 and
                    asT1 and asT2 and asT3 and asT4 and p1 and p2 and p3 and p4 and pT1 and pT2 and pT3 and pT4
                    and exP1 and exP2 and exW1 and exW2 and atn1 and atn2 and rct1 and rct2 and atd1 and atd2 and w
                    and p and pct
            ):

                num1 = float(q1)
                num2 = float(q2)
                num3 = float(q3)
                num4 = float(q4)
                num5 = float(as1)
                num6 = float(as2)
                num7 = float(as3)
                num8 = float(as4)
                num9 = float(p1)
                num10 = float(p2)
                num11 = float(p3)
                num12 = float(p4)
                num13 = float(exP1)
                num14 = float(exW1)
                num15 = float(atn1)
                num16 = float(rct1)
                num17 = float(atd1)

                denum1 = float(qT1)
                denum2 = float(qT2)
                denum3 = float(qT3)
                denum4 = float(qT4)
                denum5 = float(asT1)
                denum6 = float(asT2)
                denum7 = float(asT3)
                denum8 = float(asT4)
                denum9 = float(pT1)
                denum10 = float(pT2)
                denum11 = float(pT3)
                denum12 = float(pT4)
                denum13 = float(exP2)
                denum14 = float(exW2)
                denum15 = float(atn2)
                denum16 = float(rct2)
                denum17 = float(atd2)
                expct = float(pct)
                Pp = float(p)
                Ww = float(w)

                num = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10 + num11 + num12 + num13 + num14 + num15 + num16 + num17
                denum = (denum1 + denum2 + denum3 + denum4 + denum5 + denum6 + denum7 + denum8 + denum9 + denum10 + denum11 + denum12 +
                            denum13 + denum14 + denum15 + denum16 + denum17)

                numR = (num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10 + num11
                        + num12 + num15 + num16 + num17)
                denumR = (denum1 + denum2 + denum3 + denum4 + denum5 + denum6 + denum7 + denum8 + denum9 + denum10 +
                          denum11 + denum12 + denum15 + denum16 + denum17)


                if self.prelim.isChecked() and self.checkBox.isChecked() and self.checkBox_2.isChecked():
                        Ex = expct / 100

                        pr = num13 / denum13
                        wr = num14 / denum14

                        pr1 = pr * Pp
                        wr1 = wr * Ww

                        ex = (pr1 + wr1) * Ex

                        prd = (denum13 / denum13) * Pp
                        wrd = (denum14 / denum14) * Ww

                        exD = (prd + wrd) * Ex

                        over = ((numR + ex) / (denumR + exD)) * 100

                        self.uiOver.overF.setText(f"OVERALL : {num}/{denum}")
                        self.uiOver.gradeFE.setText(f"GWA = {over:.2f}")

                elif self.prelim.isChecked() and self.checkBox.isChecked() and not self.checkBox_2.isChecked() and Pp == 100:

                        Ex = expct / 100

                        pr = num13 / denum13
                        pr1 = pr * Pp

                        exNum = pr1 * Ex

                        exDenum = (denum13 / denum13) * expct

                        over = ((numR + exNum) / (denumR + exDenum)) * 100

                        self.uiOver.overF.setText(f"OVERALL : {num}/{denum}")
                        self.uiOver.gradeFE.setText(f"GWA = {over:.2f}")

                elif self.prelim.isChecked() and not self.checkBox.isChecked() and self.checkBox_2.isChecked() and Ww == 100:
                        Ex = expct / 100

                        wr = num14 / denum14
                        wr1 = wr * Ww

                        exNum = wr1 * Ex

                        exDenom = (denum14 / denum14) * expct


                        over = ((numR + exNum) / (denumR + exDenom)) * 100

                        self.uiOver.overF.setText(f"OVERALL : {num}/{denum}")
                        self.uiOver.gradeFE.setText(f"GWA = {over:.2f}")

                else:
                        over = (numR / denumR) * 100

                        self.uiOver.overF.setText(f"OVERALL : {numR}/{denumR}")
                        self.uiOver.gradeFE.setText(f"GWA = {over:.2f}")


                if 98.0 <= over <= 100.0 or over > 100.0:
                    self.grade_text = "1.00"
                elif 95.0 <= over < 98.0:
                    self.grade_text = "1.25"
                elif 91.0 <= over < 95.0:
                    self.grade_text = "1.75"
                elif 89.0 <= over < 91.0:
                    self.grade_text = "2.00"
                elif 86.0 <= over < 89.0:
                    self.grade_text = "2.25"
                elif 83.0 <= over < 86.0:
                    self.grade_text = "2.50"
                elif 80.0 <= over < 83.0:
                    self.grade_text = "2.75"
                elif 75.0 <= over < 80.0:
                    self.grade_text = "3.00"
                elif 70.0 <= over < 75.0:
                    self.grade_text = "3.25"
                elif over < 70:
                    self.grade_text = "5.00"
                else:
                    self.grade_text = "0.00"

                self.uiOver.uno.setText(self.grade_text)

                self.overEq = over

                allPct = (self.qzPct1 + self.assignPct1 + self.pracPct1 + self.exPct1 +
                          self.attendPct1 + self.recPct1 + self.attPct1)

                self.uiOver.allPct.setText(f"TOTAL PERCENTAGE : {allPct:.2f}%")


            else:
                print("else in overall")
        except:
            pass
    def savefunc(self):
        scrName = self.screenName.text()
        sub = self.subjC.text()
        term = self.term.text()
        studId = self.studID.text()
        lastN = self.lastN.text()
        firstN = self.firstN.text()
        midN = self.MidN.text()

        qPct = self.assPct1_3.text()
        q1 = self.qL1.text()
        q11 = self.pctQ1.text()
        q2 = self.qL2.text()
        q22 = self.pctQ2.text()
        q3 = self.qL3.text()
        q33 = self.pctQ3.text()
        q4 = self.qL4.text()
        q44 = self.pctQ4.text()

        assPct = self.assPct1_2.text()
        as1 = self.assL1.text()
        as11 = self.assPct1.text()
        as2 = self.assL2.text()
        as22 = self.assPct2.text()
        as3 = self.assL3.text()
        as33 = self.assPct3.text()
        as4 = self.assL4.text()
        as44 = self.assPct4.text()

        prPct = self.assPct1_4.text()
        pr1 = self.prL1.text()
        pr11 = self.prL1pct.text()
        pr2 = self.prL2.text()
        pr22 = self.prL2pct.text()
        pr3 = self.prL3.text()
        pr33 = self.prL3pct.text()
        pr4 = self.prL4.text()
        pr44 = self.prL4pct.text()

        exPct = self.assPct1_5.text()
        ex1 = self.exPrL.text()
        ex11 = self.exPrPct.text()
        ex111 = self.prPct.text()
        ex2 = self.exWrL.text()
        ex22 = self.exWrPct.text()
        ex222 = self.wrPct.text()

        atnPct = self.atnPct.text()
        atn1 = self.atn1.text()
        atn11 = self.atn1Pct.text()

        rctPct = self.rctPct.text()
        rct1 = self.rct1.text()
        rct11 = self.rct1Pct.text()

        atdPct = self.atdPct.text()
        atd1 = self.atd1.text()
        atd11 = self.atd1Pct.text()

        try:
            con = sqlite3.connect("hmp.db")
            cur = con.cursor()
            cur.execute(
                f"SELECT * FROM loadData WHERE accountName = ? AND subjectCode = ? AND Term = ? AND studentID = ?",
                (scrName, sub, term, studId))
            result = cur.fetchone()

            if result:
                updtquery = (
                    "UPDATE loadData SET "
                    "QuizPct = ?, quiz1 = ?, quiz11 = ?, "
                    "quiz2 = ?, quiz22 = ?, quiz3 = ?, quiz33 = ?, quiz4 = ?, quiz44 = ?, "
                    "PracPct = ?, Prac1 = ?, Prac11 = ?, Prac2 = ?, Prac22 = ?, Prac3 = ?, "
                    "Prac33 = ?, Prac4 = ?, Prac44 = ?, "
                    "AssPct = ?, Ass1 = ?, Ass11 = ?, Ass2 = ?, Ass22 = ?, "
                    "Ass3 = ?, Ass33 = ?, Ass4 = ?, Ass44 = ?, "
                    "ExamPct = ?, ePr1 = ?, ePr2 = ?, eWr1 = ?, eWr2 = ?, "
                    "atnpct = ?, atn1 = ?, atn11 = ?, "
                    "rctpct = ?, rct1 = ?, rct11 = ?, "
                    "atdpct = ?, atd1 = ?, atd11 = ?, prPct = ?, wrPct = ? "
                    "WHERE accountName = ? AND subjectCode = ? AND Term = ? AND studentID = ?"
                )

                updtvals = (
                    qPct, q1, q11, q2, q22, q3, q33, q4, q44,
                    prPct, pr1, pr11, pr2, pr22, pr3, pr33, pr4, pr44,
                    assPct, as1, as11, as2, as22, as3, as33, as4, as44,
                    exPct, ex1, ex11, ex2, ex22,
                    atnPct, atn1, atn11,
                    rctPct, rct1, rct11,
                    atdPct, atd1, atd11, ex111, ex222,
                    scrName, sub, term, studId
                )

                cur.execute(updtquery, updtvals)
                con.commit()
                self.msgBoxInfo(f"{sub} - {term}, Student ID - {studId} Modified Successfully")
                con.close()

            else:
                if not studId or not lastN or not firstN or not midN:
                    self.msgBoxWarn("Please fill out all fields.")
                else:

                    cur.execute("SELECT studentID FROM studentInfo WHERE studentID = ?", (studId,))
                    result1 = cur.fetchone()

                    if result1:

                        insrtquery = (
                            "INSERT INTO loadData "
                            "(QuizPct, quiz1, quiz11, "
                            "quiz2, quiz22, quiz3, quiz33, quiz4, quiz44, "
                            "PracPct, Prac1, Prac11, Prac2, Prac22, Prac3, "
                            "Prac33, Prac4, Prac44, "
                            "AssPct, Ass1, Ass11, Ass2, Ass22, "
                            "Ass3, Ass33, Ass4, Ass44, "
                            "ExamPct, ePr1, ePr2, eWr1, eWr2, "
                            "atnpct, atn1, atn11, "
                            "rctpct, rct1, rct11, "
                            "atdpct, atd1, atd11, prPct, wrPct, "
                            "accountName, subjectCode, Term, studentID) "
                            "VALUES "
                            "(?, ?, ?, ?, ?, ?, ?, ?, ?, "
                            "?, ?, ?, ?, ?, ?, ?, ?, ?, ?, "
                            "?, ?, ?, ?, ?, ?, ?, ?, ?, ?, "
                            "?, ?, ?, ?, ?, ?, ?, ?, ?, ?, "
                            "?, ?, ?, ?, ?, ?, ?, ?)"
                        )

                        insrtvals = (
                            qPct, q1, q11, q2, q22, q3, q33, q4, q44,
                            prPct, pr1, pr11, pr2, pr22, pr3, pr33, pr4, pr44,
                            assPct, as1, as11, as2, as22, as3, as33, as4, as44,
                            exPct, ex1, ex11, ex2, ex22,
                            atnPct, atn1, atn11,
                            rctPct, rct1, rct11,
                            atdPct, atd1, atd11, ex111, ex222,
                            scrName, sub, term, studId
                        )

                        cur.execute(insrtquery, insrtvals)

                        con.commit()

                        self.msgBoxInfo("Successfully Saved")

                    else:
                        cur.execute("INSERT INTO studentInfo (studentID, LastName, FirstName, MiddleName) VALUES (?, ?, ?, ?)",
                            (studId, lastN, firstN, midN))

                        con.commit()

                        insrtquery = (
                            "INSERT INTO loadData "
                            "(QuizPct, quiz1, quiz11, "
                            "quiz2, quiz22, quiz3, quiz33, quiz4, quiz44, "
                            "PracPct, Prac1, Prac11, Prac2, Prac22, Prac3, "
                            "Prac33, Prac4, Prac44, "
                            "AssPct, Ass1, Ass11, Ass2, Ass22, "
                            "Ass3, Ass33, Ass4, Ass44, "
                            "ExamPct, ePr1, ePr2, eWr1, eWr2, "
                            "atnpct, atn1, atn11, "
                            "rctpct, rct1, rct11, "
                            "atdpct, atd1, atd11, prPct, wrPct, "
                            "accountName, subjectCode, Term, studentID) "
                            "VALUES "
                            "(?, ?, ?, ?, ?, ?, ?, ?, ?, "
                            "?, ?, ?, ?, ?, ?, ?, ?, ?, ?, "
                            "?, ?, ?, ?, ?, ?, ?, ?, ?, ?, "
                            "?, ?, ?, ?, ?, ?, ?, ?, ?, ?, "
                            "?, ?, ?, ?, ?, ?, ?, ?)"
                        )

                        insrtvals = (
                            qPct, q1, q11, q2, q22, q3, q33, q4, q44,
                            prPct, pr1, pr11, pr2, pr22, pr3, pr33, pr4, pr44,
                            assPct, as1, as11, as2, as22, as3, as33, as4, as44,
                            exPct, ex1, ex11, ex2, ex22,
                            atnPct, atn1, atn11,
                            rctPct, rct1, rct11,
                            atdPct, atd1, atd11, ex111, ex222,
                            scrName, sub, term, studId
                        )

                        cur.execute(insrtquery, insrtvals)

                        con.commit()

                        self.msgBoxInfo(f"Student ID: {studId} - {lastN}, {firstN} {midN} is Successfully Registered & his/her data were Saved")

            con.close()

        except Exception as e:
            print("error in savefunc: ", str(e))

    # ====================================POP-UP FORM FUNCTION=========================================================
    def msgBoxInfo(self, msg):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("AcadExcel")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(msg)
        self.showInfo = msgBox.exec()

    def msgBoxWarn(self, msg1):
        msgBox1 = QMessageBox()
        msgBox1.setWindowTitle("AcadExcel")
        msgBox1.setIcon(QMessageBox.Warning)
        msgBox1.setText(msg1)
        self.showWarn = msgBox1.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())