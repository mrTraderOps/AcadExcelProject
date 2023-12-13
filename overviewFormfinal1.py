from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class over_Form(object):
    def overviewForm(self, Form):
        Form.setObjectName("Form")
        Form.resize(856, 668)
        Form.setMaximumSize(856,668)
        Form.setMinimumSize(856,668)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 821, 641))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(320, 30, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.studTableF = QtWidgets.QTableWidget(self.widget)
        self.studTableF.setGeometry(QtCore.QRect(200, 70, 421, 71))
        self.studTableF.setStyleSheet("font: 25 9pt \"Bahnschrift Light\";")
        self.studTableF.setObjectName("studTableF")
        self.studTableF.setColumnCount(5)
        self.studTableF.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.studTableF.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.studTableF.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.studTableF.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.studTableF.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.studTableF.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.studTableF.setHorizontalHeaderItem(4, item)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(280, 170, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(630, 590, 111, 28))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"background-color:rgb(76, 111, 191);\n"
"border-radius: 10%;\n"
"border: None;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(255, 255, 255);\n"
"color: rgb(76, 111, 191);\n"
"border-radius: 10%;\n"
"border: None;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(50, 200, 221, 171))
        self.widget_2.setStyleSheet("font: 25 9pt \"Bahnschrift Light\";")
        self.widget_2.setObjectName("widget_2")
        self.layoutWidget = QtWidgets.QWidget(self.widget_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 197, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.qF1 = QtWidgets.QLabel(self.layoutWidget)
        self.qF1.setObjectName("qF1")
        self.verticalLayout_3.addWidget(self.qF1)
        self.qF2 = QtWidgets.QLabel(self.layoutWidget)
        self.qF2.setObjectName("qF2")
        self.verticalLayout_3.addWidget(self.qF2)
        self.qF3 = QtWidgets.QLabel(self.layoutWidget)
        self.qF3.setObjectName("qF3")
        self.verticalLayout_3.addWidget(self.qF3)
        self.qF4 = QtWidgets.QLabel(self.layoutWidget)
        self.qF4.setObjectName("qF4")
        self.verticalLayout_3.addWidget(self.qF4)
        self.qT = QtWidgets.QLabel(self.layoutWidget)
        self.qT.setObjectName("qT")
        self.verticalLayout_3.addWidget(self.qT)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_27 = QtWidgets.QLabel(self.layoutWidget)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_5.addWidget(self.label_27)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.qTE = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.qTE.setFont(font)
        self.qTE.setObjectName("qTE")
        self.verticalLayout_4.addWidget(self.qTE)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(290, 210, 251, 161))
        self.widget_3.setStyleSheet("font: 25 9pt \"Bahnschrift Light\";")
        self.widget_3.setObjectName("widget_3")
        self.layoutWidget_3 = QtWidgets.QWidget(self.widget_3)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 10, 240, 141))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_28 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_6.addWidget(self.label_28)
        self.label_29 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_6.addWidget(self.label_29)
        self.label_30 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_6.addWidget(self.label_30)
        self.label_31 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_6.addWidget(self.label_31)
        self.label_32 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_6.addWidget(self.label_32)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_33 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_33.setObjectName("label_33")
        self.verticalLayout_7.addWidget(self.label_33)
        self.label_34 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_34.setObjectName("label_34")
        self.verticalLayout_7.addWidget(self.label_34)
        self.label_35 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_7.addWidget(self.label_35)
        self.label_36 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_36.setObjectName("label_36")
        self.verticalLayout_7.addWidget(self.label_36)
        self.label_37 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_37.setObjectName("label_37")
        self.verticalLayout_7.addWidget(self.label_37)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.assF1 = QtWidgets.QLabel(self.layoutWidget_3)
        self.assF1.setObjectName("assF1")
        self.verticalLayout_8.addWidget(self.assF1)
        self.assF2 = QtWidgets.QLabel(self.layoutWidget_3)
        self.assF2.setObjectName("assF2")
        self.verticalLayout_8.addWidget(self.assF2)
        self.assF3 = QtWidgets.QLabel(self.layoutWidget_3)
        self.assF3.setObjectName("assF3")
        self.verticalLayout_8.addWidget(self.assF3)
        self.assF4 = QtWidgets.QLabel(self.layoutWidget_3)
        self.assF4.setObjectName("assF4")
        self.verticalLayout_8.addWidget(self.assF4)
        self.assT = QtWidgets.QLabel(self.layoutWidget_3)
        self.assT.setObjectName("assT")
        self.verticalLayout_8.addWidget(self.assT)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_47 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_47.setObjectName("label_47")
        self.verticalLayout_9.addWidget(self.label_47)
        self.horizontalLayout_2.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.assTE = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.assTE.setFont(font)
        self.assTE.setObjectName("assTE")
        self.verticalLayout_10.addWidget(self.assTE)
        self.horizontalLayout_2.addLayout(self.verticalLayout_10)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setGeometry(QtCore.QRect(550, 210, 251, 161))
        self.widget_4.setStyleSheet("font: 25 9pt \"Bahnschrift Light\";")
        self.widget_4.setObjectName("widget_4")
        self.layoutWidget_6 = QtWidgets.QWidget(self.widget_4)
        self.layoutWidget_6.setGeometry(QtCore.QRect(10, 10, 226, 141))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_56 = QtWidgets.QLabel(self.layoutWidget_6)
        self.label_56.setObjectName("label_56")
        self.verticalLayout_21.addWidget(self.label_56)
        self.label_83 = QtWidgets.QLabel(self.layoutWidget_6)
        self.label_83.setObjectName("label_83")
        self.verticalLayout_21.addWidget(self.label_83)
        self.label_84 = QtWidgets.QLabel(self.layoutWidget_6)
        self.label_84.setObjectName("label_84")
        self.verticalLayout_21.addWidget(self.label_84)
        self.label_85 = QtWidgets.QLabel(self.layoutWidget_6)
        self.label_85.setObjectName("label_85")
        self.verticalLayout_21.addWidget(self.label_85)
        self.label_86 = QtWidgets.QLabel(self.layoutWidget_6)
        self.label_86.setObjectName("label_86")
        self.verticalLayout_21.addWidget(self.label_86)
        self.horizontalLayout_5.addLayout(self.verticalLayout_21)
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_87 = QtWidgets.QLabel(self.layoutWidget_6)
        self.label_87.setObjectName("label_87")
        self.verticalLayout_22.addWidget(self.label_87)
        self.label_88 = QtWidgets.QLabel(self.layoutWidget_6)
        self.label_88.setObjectName("label_88")
        self.verticalLayout_22.addWidget(self.label_88)
        self.label_89 = QtWidgets.QLabel(self.layoutWidget_6)
        self.label_89.setObjectName("label_89")
        self.verticalLayout_22.addWidget(self.label_89)
        self.label_90 = QtWidgets.QLabel(self.layoutWidget_6)
        self.label_90.setObjectName("label_90")
        self.verticalLayout_22.addWidget(self.label_90)
        self.label_91 = QtWidgets.QLabel(self.layoutWidget_6)
        self.label_91.setObjectName("label_91")
        self.verticalLayout_22.addWidget(self.label_91)
        self.horizontalLayout_5.addLayout(self.verticalLayout_22)
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.pracF1 = QtWidgets.QLabel(self.layoutWidget_6)
        self.pracF1.setObjectName("pracF1")
        self.verticalLayout_23.addWidget(self.pracF1)
        self.pracF2 = QtWidgets.QLabel(self.layoutWidget_6)
        self.pracF2.setObjectName("pracF2")
        self.verticalLayout_23.addWidget(self.pracF2)
        self.pracF3 = QtWidgets.QLabel(self.layoutWidget_6)
        self.pracF3.setObjectName("pracF3")
        self.verticalLayout_23.addWidget(self.pracF3)
        self.pracF4 = QtWidgets.QLabel(self.layoutWidget_6)
        self.pracF4.setObjectName("pracF4")
        self.verticalLayout_23.addWidget(self.pracF4)
        self.pracT = QtWidgets.QLabel(self.layoutWidget_6)
        self.pracT.setObjectName("pracT")
        self.verticalLayout_23.addWidget(self.pracT)
        self.horizontalLayout_5.addLayout(self.verticalLayout_23)
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.label_101 = QtWidgets.QLabel(self.layoutWidget_6)
        self.label_101.setObjectName("label_101")
        self.verticalLayout_24.addWidget(self.label_101)
        self.horizontalLayout_5.addLayout(self.verticalLayout_24)
        self.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.pracTE = QtWidgets.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.pracTE.setFont(font)
        self.pracTE.setObjectName("pracTE")
        self.verticalLayout_25.addWidget(self.pracTE)
        self.horizontalLayout_5.addLayout(self.verticalLayout_25)
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setGeometry(QtCore.QRect(50, 390, 251, 91))
        self.widget_5.setStyleSheet("font: 25 9pt \"Bahnschrift Light\";")
        self.widget_5.setObjectName("widget_5")
        self.layoutWidget_5 = QtWidgets.QWidget(self.widget_5)
        self.layoutWidget_5.setGeometry(QtCore.QRect(10, 10, 233, 70))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_67 = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_67.setObjectName("label_67")
        self.verticalLayout_16.addWidget(self.label_67)
        self.label_66 = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_66.setObjectName("label_66")
        self.verticalLayout_16.addWidget(self.label_66)
        self.label_70 = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_70.setObjectName("label_70")
        self.verticalLayout_16.addWidget(self.label_70)
        self.horizontalLayout_4.addLayout(self.verticalLayout_16)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_71 = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_71.setObjectName("label_71")
        self.verticalLayout_17.addWidget(self.label_71)
        self.label_76 = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_76.setObjectName("label_76")
        self.verticalLayout_17.addWidget(self.label_76)
        self.label_75 = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_75.setObjectName("label_75")
        self.verticalLayout_17.addWidget(self.label_75)
        self.horizontalLayout_4.addLayout(self.verticalLayout_17)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.peF = QtWidgets.QLabel(self.layoutWidget_5)
        self.peF.setObjectName("peF")
        self.verticalLayout_18.addWidget(self.peF)
        self.weF = QtWidgets.QLabel(self.layoutWidget_5)
        self.weF.setObjectName("weF")
        self.verticalLayout_18.addWidget(self.weF)
        self.peF_2 = QtWidgets.QLabel(self.layoutWidget_5)
        self.peF_2.setObjectName("peF_2")
        self.verticalLayout_18.addWidget(self.peF_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_18)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_82 = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_82.setObjectName("label_82")
        self.verticalLayout_19.addWidget(self.label_82)
        self.horizontalLayout_4.addLayout(self.verticalLayout_19)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.peE = QtWidgets.QLabel(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.peE.setFont(font)
        self.peE.setObjectName("peE")
        self.verticalLayout_20.addWidget(self.peE)
        self.horizontalLayout_4.addLayout(self.verticalLayout_20)
        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.setGeometry(QtCore.QRect(50, 500, 221, 111))
        self.widget_6.setStyleSheet("font: 25 9pt \"Bahnschrift Light\";")
        self.widget_6.setObjectName("widget_6")
        self.layoutWidget_4 = QtWidgets.QWidget(self.widget_6)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 10, 208, 91))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_53 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_53.setObjectName("label_53")
        self.verticalLayout_11.addWidget(self.label_53)
        self.label_54 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_54.setObjectName("label_54")
        self.verticalLayout_11.addWidget(self.label_54)
        self.label_55 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_55.setObjectName("label_55")
        self.verticalLayout_11.addWidget(self.label_55)
        self.horizontalLayout_3.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_58 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_58.setObjectName("label_58")
        self.verticalLayout_12.addWidget(self.label_58)
        self.label_59 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_59.setObjectName("label_59")
        self.verticalLayout_12.addWidget(self.label_59)
        self.label_60 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_60.setObjectName("label_60")
        self.verticalLayout_12.addWidget(self.label_60)
        self.horizontalLayout_3.addLayout(self.verticalLayout_12)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.atnF = QtWidgets.QLabel(self.layoutWidget_4)
        self.atnF.setObjectName("atnF")
        self.verticalLayout_13.addWidget(self.atnF)
        self.rctF = QtWidgets.QLabel(self.layoutWidget_4)
        self.rctF.setObjectName("rctF")
        self.verticalLayout_13.addWidget(self.rctF)
        self.atdF = QtWidgets.QLabel(self.layoutWidget_4)
        self.atdF.setObjectName("atdF")
        self.verticalLayout_13.addWidget(self.atdF)
        self.horizontalLayout_3.addLayout(self.verticalLayout_13)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_68 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_68.setObjectName("label_68")
        self.verticalLayout_14.addWidget(self.label_68)
        self.label_69 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_69.setObjectName("label_69")
        self.verticalLayout_14.addWidget(self.label_69)
        self.label_72 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_72.setObjectName("label_72")
        self.verticalLayout_14.addWidget(self.label_72)
        self.horizontalLayout_3.addLayout(self.verticalLayout_14)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.atdE = QtWidgets.QLabel(self.layoutWidget_4)
        self.atdE.setObjectName("atdE")
        self.verticalLayout_15.addWidget(self.atdE)
        self.rctE = QtWidgets.QLabel(self.layoutWidget_4)
        self.rctE.setObjectName("rctE")
        self.verticalLayout_15.addWidget(self.rctE)
        self.atdE_2 = QtWidgets.QLabel(self.layoutWidget_4)
        self.atdE_2.setObjectName("atdE_2")
        self.verticalLayout_15.addWidget(self.atdE_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_15)
        self.widget_8 = QtWidgets.QWidget(self.widget)
        self.widget_8.setGeometry(QtCore.QRect(580, 390, 231, 121))
        self.widget_8.setStyleSheet("font: 63 12pt \"Bahnschrift SemiBold\";")
        self.widget_8.setObjectName("widget_8")
        self.overF = QtWidgets.QLabel(self.widget_8)
        self.overF.setGeometry(QtCore.QRect(30, 60, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.overF.setFont(font)
        self.overF.setObjectName("overF")
        self.gradeFE = QtWidgets.QLabel(self.widget_8)
        self.gradeFE.setGeometry(QtCore.QRect(60, 90, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.gradeFE.setFont(font)
        self.gradeFE.setObjectName("gradeFE")
        self.allPct = QtWidgets.QLabel(self.widget_8)
        self.allPct.setGeometry(QtCore.QRect(10, 30, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.allPct.setFont(font)
        self.allPct.setObjectName("allPct")
        self.uno = QtWidgets.QLabel(self.widget)
        self.uno.setGeometry(QtCore.QRect(670, 510, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.uno.setFont(font)
        self.uno.setStyleSheet("font: 63 14pt \"Bahnschrift SemiBold\";")
        self.uno.setObjectName("uno")
        self.uno_2 = QtWidgets.QLabel(self.widget)
        self.uno_2.setGeometry(QtCore.QRect(650, 540, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.uno_2.setFont(font)
        self.uno_2.setStyleSheet("font: 63 14pt \"Bahnschrift SemiBold\";")
        self.uno_2.setObjectName("uno_2")
        self.widget_9 = QtWidgets.QWidget(self.widget)
        self.widget_9.setGeometry(QtCore.QRect(320, 390, 241, 231))
        self.widget_9.setObjectName("widget_9")
        self.exPF = QtWidgets.QLabel(self.widget_9)
        self.exPF.setGeometry(QtCore.QRect(10, 100, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.exPF.setFont(font)
        self.exPF.setStyleSheet("font: 63 10pt \"Bahnschrift SemiBold\";")
        self.exPF.setObjectName("exPF")
        self.pracPF = QtWidgets.QLabel(self.widget_9)
        self.pracPF.setGeometry(QtCore.QRect(10, 70, 211, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pracPF.setFont(font)
        self.pracPF.setStyleSheet("font: 63 10pt \"Bahnschrift SemiBold\";")
        self.pracPF.setObjectName("pracPF")
        self.qPF = QtWidgets.QLabel(self.widget_9)
        self.qPF.setGeometry(QtCore.QRect(10, 10, 211, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.qPF.setFont(font)
        self.qPF.setObjectName("qPF")
        self.assPF = QtWidgets.QLabel(self.widget_9)
        self.assPF.setGeometry(QtCore.QRect(13, 40, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.assPF.setFont(font)
        self.assPF.setStyleSheet("font: 63 10pt \"Bahnschrift SemiBold\";")
        self.assPF.setObjectName("assPF")
        self.widget_7 = QtWidgets.QWidget(self.widget_9)
        self.widget_7.setGeometry(QtCore.QRect(3, 130, 241, 91))
        self.widget_7.setStyleSheet("font: 63 10pt \"Bahnschrift SemiBold\";")
        self.widget_7.setObjectName("widget_7")
        self.oPF_3 = QtWidgets.QLabel(self.widget_7)
        self.oPF_3.setGeometry(QtCore.QRect(10, 60, 231, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.oPF_3.setFont(font)
        self.oPF_3.setObjectName("oPF_3")
        self.oPF_2 = QtWidgets.QLabel(self.widget_7)
        self.oPF_2.setGeometry(QtCore.QRect(10, 30, 231, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.oPF_2.setFont(font)
        self.oPF_2.setObjectName("oPF_2")
        self.oPF = QtWidgets.QLabel(self.widget_7)
        self.oPF.setGeometry(QtCore.QRect(10, 0, 231, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.oPF.setFont(font)
        self.oPF.setObjectName("oPF")
        self.widget_8.raise_()
        self.widget_6.raise_()
        self.widget_5.raise_()
        self.widget_4.raise_()
        self.widget_2.raise_()
        self.label.raise_()
        self.studTableF.raise_()
        self.label_7.raise_()
        self.pushButton.raise_()
        self.widget_3.raise_()
        self.uno.raise_()
        self.uno_2.raise_()
        self.widget_9.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Student Information"))
        item = self.studTableF.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.studTableF.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Student ID"))
        item = self.studTableF.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Last Name"))
        item = self.studTableF.horizontalHeaderItem(2)
        item.setText(_translate("Form", "First Name"))
        item = self.studTableF.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Middle Name"))
        self.label_7.setText(_translate("Form", "Grade Overview & Computation"))
        self.pushButton.setText(_translate("Form", "Save"))
        self.label_2.setText(_translate("Form", "Quiz 1"))
        self.label_3.setText(_translate("Form", "Quiz 2"))
        self.label_4.setText(_translate("Form", "Quiz 3"))
        self.label_5.setText(_translate("Form", "Quiz 4"))
        self.label_6.setText(_translate("Form", "Quiz Total"))
        self.label_8.setText(_translate("Form", "="))
        self.label_9.setText(_translate("Form", "="))
        self.label_10.setText(_translate("Form", "="))
        self.label_11.setText(_translate("Form", "="))
        self.label_12.setText(_translate("Form", "="))
        self.qF1.setText(_translate("Form", "0/0"))
        self.qF2.setText(_translate("Form", "0/0"))
        self.qF3.setText(_translate("Form", "0/0"))
        self.qF4.setText(_translate("Form", "0/0"))
        self.qT.setText(_translate("Form", "0/0"))
        self.label_27.setText(_translate("Form", "Eq."))
        self.qTE.setText(_translate("Form", "0"))
        self.label_28.setText(_translate("Form", "Assigment 1"))
        self.label_29.setText(_translate("Form", "Assigment 2"))
        self.label_30.setText(_translate("Form", "Assigment 3"))
        self.label_31.setText(_translate("Form", "Assigment 4"))
        self.label_32.setText(_translate("Form", "Assigment Total"))
        self.label_33.setText(_translate("Form", "="))
        self.label_34.setText(_translate("Form", "="))
        self.label_35.setText(_translate("Form", "="))
        self.label_36.setText(_translate("Form", "="))
        self.label_37.setText(_translate("Form", "="))
        self.assF1.setText(_translate("Form", "0/0"))
        self.assF2.setText(_translate("Form", "0/0"))
        self.assF3.setText(_translate("Form", "0/0"))
        self.assF4.setText(_translate("Form", "0/0"))
        self.assT.setText(_translate("Form", "0/0"))
        self.label_47.setText(_translate("Form", "Eq."))
        self.assTE.setText(_translate("Form", "0"))
        self.label_56.setText(_translate("Form", "Practical 1"))
        self.label_83.setText(_translate("Form", "Practical 2"))
        self.label_84.setText(_translate("Form", "Practical 3"))
        self.label_85.setText(_translate("Form", "Practical 4"))
        self.label_86.setText(_translate("Form", "Practical Total"))
        self.label_87.setText(_translate("Form", "="))
        self.label_88.setText(_translate("Form", "="))
        self.label_89.setText(_translate("Form", "="))
        self.label_90.setText(_translate("Form", "="))
        self.label_91.setText(_translate("Form", "="))
        self.pracF1.setText(_translate("Form", "0/0"))
        self.pracF2.setText(_translate("Form", "0/0"))
        self.pracF3.setText(_translate("Form", "0/0"))
        self.pracF4.setText(_translate("Form", "0/0"))
        self.pracT.setText(_translate("Form", "0/0"))
        self.label_101.setText(_translate("Form", "Eq."))
        self.pracTE.setText(_translate("Form", "0"))
        self.label_67.setText(_translate("Form", "Practical Exam"))
        self.label_66.setText(_translate("Form", "Written Exam"))
        self.label_70.setText(_translate("Form", "Total Exam"))
        self.label_71.setText(_translate("Form", "="))
        self.label_76.setText(_translate("Form", "="))
        self.label_75.setText(_translate("Form", "="))
        self.peF.setText(_translate("Form", "0/0"))
        self.weF.setText(_translate("Form", "0/0"))
        self.peF_2.setText(_translate("Form", "0/0"))
        self.label_82.setText(_translate("Form", "Eq."))
        self.peE.setText(_translate("Form", "0"))
        self.label_53.setText(_translate("Form", "Attendance"))
        self.label_54.setText(_translate("Form", "Recitation"))
        self.label_55.setText(_translate("Form", "Attitude"))
        self.label_58.setText(_translate("Form", "="))
        self.label_59.setText(_translate("Form", "="))
        self.label_60.setText(_translate("Form", "="))
        self.atnF.setText(_translate("Form", "0/0"))
        self.rctF.setText(_translate("Form", "0/0"))
        self.atdF.setText(_translate("Form", "0/0"))
        self.label_68.setText(_translate("Form", "Eq."))
        self.label_69.setText(_translate("Form", "Eq."))
        self.label_72.setText(_translate("Form", "Eq."))
        self.atdE.setText(_translate("Form", "0"))
        self.rctE.setText(_translate("Form", "0"))
        self.atdE_2.setText(_translate("Form", "0"))
        self.overF.setText(_translate("Form", "OVERALL : 0/0"))
        self.gradeFE.setText(_translate("Form", "GWA = 0.00"))
        self.allPct.setText(_translate("Form", "TOTAL PERCENTAGE : 0%"))
        self.uno.setText(_translate("Form", "0.00"))
        self.uno_2.setText(_translate("Form", "GRADE"))
        self.exPF.setText(_translate("Form", " Exam Percentage = 0%/0%"))
        self.pracPF.setText(_translate("Form", " Practical Percentage = 0%/0%"))
        self.qPF.setText(_translate("Form", " Quiz Percentage = 0%/0%"))
        self.assPF.setText(_translate("Form", "Assignment Percentage = 0%/0%"))
        self.oPF_3.setText(_translate("Form", "Attitude Percentage = 0%"))
        self.oPF_2.setText(_translate("Form", "Recitation Percentage = 0%"))
        self.oPF.setText(_translate("Form", "Attendance Percentage = 0%"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = over_Form()
    ui.overviewForm(Form)
    Form.show()
    sys.exit(app.exec_())
