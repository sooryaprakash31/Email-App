# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/credentials.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 350)
        self.emailText = QtWidgets.QTextEdit(Form)
        self.emailText.setGeometry(QtCore.QRect(200, 70, 341, 41))
        self.emailText.setObjectName("emailText")
        self.password = QtWidgets.QLabel(Form)
        self.password.setGeometry(QtCore.QRect(40, 140, 101, 23))
        self.password.setObjectName("password")
        self.passText = QtWidgets.QTextEdit(Form)
        self.passText.setGeometry(QtCore.QRect(200, 140, 341, 41))
        self.passText.setObjectName("passText")
        self.emailAddress = QtWidgets.QLabel(Form)
        self.emailAddress.setGeometry(QtCore.QRect(40, 70, 131, 23))
        self.emailAddress.setObjectName("emailAddress")
        self.sendMails = QtWidgets.QPushButton(Form)
        self.sendMails.setGeometry(QtCore.QRect(400, 220, 141, 51))
        self.sendMails.setObjectName("sendMails")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.password.setText(_translate("Form", "Password"))
        self.emailAddress.setText(_translate("Form", "Email address"))
        self.sendMails.setText(_translate("Form", "Send Mails"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
