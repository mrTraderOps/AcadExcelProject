
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(401, 283)
        self.formStacked = QtWidgets.QStackedWidget(Form)
        self.formStacked.setGeometry(QtCore.QRect(20, 10, 371, 261))
        self.formStacked.setStyleSheet("font: 25 9pt \"Bahnschrift Light\";")
        self.formStacked.setObjectName("formStacked")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(60, 70, 261, 51))
        self.label.setObjectName("label")
        self.createSubj = QtWidgets.QPushButton(self.page)
        self.createSubj.setGeometry(QtCore.QRect(50, 130, 121, 41))
        self.createSubj.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.createSubj.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"background-color:rgb(76, 111, 191);\n"
"border-radius: 20%;\n"
"border: None;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(255, 255, 255);\n"
"color: rgb(76, 111, 191);\n"
"border-radius: 20%;\n"
"border: None;\n"
"}")
        self.createSubj.setObjectName("createSubj")
        self.selectBtn = QtWidgets.QPushButton(self.page)
        self.selectBtn.setGeometry(QtCore.QRect(190, 130, 121, 41))
        self.selectBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.selectBtn.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"background-color:rgb(76, 111, 191);\n"
"border-radius: 20%;\n"
"border: None;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(255, 255, 255);\n"
"color: rgb(76, 111, 191);\n"
"border-radius: 20%;\n"
"border: None;\n"
"}")
        self.selectBtn.setObjectName("selectBtn")
        self.formStacked.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(120, 50, 151, 41))
        self.label_2.setObjectName("label_2")
        self.subjL = QtWidgets.QLineEdit(self.page_2)
        self.subjL.setGeometry(QtCore.QRect(120, 90, 113, 20))
        self.subjL.setObjectName("subjL")
        self.prelimbtn = QtWidgets.QRadioButton(self.page_2)
        self.prelimbtn.setGeometry(QtCore.QRect(130, 120, 101, 21))
        self.prelimbtn.setObjectName("prelimbtn")
        self.midbtn = QtWidgets.QRadioButton(self.page_2)
        self.midbtn.setGeometry(QtCore.QRect(130, 150, 82, 21))
        self.midbtn.setObjectName("midbtn")
        self.finalbtn = QtWidgets.QRadioButton(self.page_2)
        self.finalbtn.setGeometry(QtCore.QRect(130, 180, 82, 21))
        self.finalbtn.setObjectName("finalbtn")
        self.submitbtn = QtWidgets.QPushButton(self.page_2)
        self.submitbtn.setGeometry(QtCore.QRect(270, 212, 75, 31))
        self.submitbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submitbtn.setStyleSheet("QPushButton {\n"
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
        self.submitbtn.setObjectName("submitbtn")
        self.backBtn = QtWidgets.QPushButton(self.page_2)
        self.backBtn.setGeometry(QtCore.QRect(10, 20, 81, 31))
        self.backBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backBtn.setStyleSheet("QPushButton {\n"
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
        self.backBtn.setObjectName("backBtn")
        self.formStacked.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setGeometry(QtCore.QRect(130, 60, 131, 16))
        self.label_3.setObjectName("label_3")
        self.selectCmb = QtWidgets.QComboBox(self.page_3)
        self.selectCmb.setGeometry(QtCore.QRect(120, 100, 121, 21))
        self.selectCmb.setObjectName("selectCmb")
        self.proceedbtn = QtWidgets.QPushButton(self.page_3)
        self.proceedbtn.setGeometry(QtCore.QRect(260, 212, 75, 31))
        self.proceedbtn.setStyleSheet("QPushButton {\n"
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
        self.proceedbtn.setObjectName("proceedbtn")
        self.backBtn1 = QtWidgets.QPushButton(self.page_3)
        self.backBtn1.setGeometry(QtCore.QRect(20, 20, 75, 31))
        self.backBtn1.setStyleSheet("QPushButton {\n"
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
        self.backBtn1.setObjectName("backBtn1")
        self.comboBox = QtWidgets.QComboBox(self.page_3)
        self.comboBox.setGeometry(QtCore.QRect(120, 170, 121, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setGeometry(QtCore.QRect(140, 140, 71, 16))
        self.label_4.setObjectName("label_4")
        self.formStacked.addWidget(self.page_3)

        self.retranslateUi(Form)
        self.formStacked.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.function()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "AcadExcel"))
        self.label.setText(_translate("Form", "Creating New Subject Code? or Select Subject?"))
        self.createSubj.setText(_translate("Form", "Create New"))
        self.selectBtn.setText(_translate("Form", "Select"))
        self.label_2.setText(_translate("Form", "Provide a Subject Code"))
        self.prelimbtn.setText(_translate("Form", "PRELIMINARY"))
        self.midbtn.setText(_translate("Form", "MIDTERM"))
        self.finalbtn.setText(_translate("Form", "FINAL"))
        self.submitbtn.setText(_translate("Form", "Submit"))
        self.backBtn.setText(_translate("Form", "Back"))
        self.label_3.setText(_translate("Form", "Select Subject Code"))
        self.proceedbtn.setText(_translate("Form", "Proceed"))
        self.backBtn1.setText(_translate("Form", "Back"))
        self.label_4.setText(_translate("Form", "Select a Term"))

    def function(self):
        self.createSubj.clicked.connect(self.createSub)
        self.selectBtn.clicked.connect(self.selectSub)
        self.backBtn.clicked.connect(self.backfunc)
        self.backBtn1.clicked.connect(self.backfunc)
    def backfunc(self):
        self.formStacked.setCurrentIndex(0)
    def createSub(self):
        self.formStacked.setCurrentIndex(1)
    def selectSub(self):
        self.formStacked.setCurrentIndex(2)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QDialog()
    ui = Ui_Form()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())


