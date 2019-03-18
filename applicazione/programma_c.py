from PyQt5 import QtCore, QtGui, QtWidgets
#Bussolotto Raffaele, 25/02/2019, v_1.0
class Ui_finestra(object):
    def setupUi(self, finestra):
        finestra.setObjectName("finestra")
        finestra.resize(392, 300)
        self.formLayoutWidget = QtWidgets.QWidget(finestra)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 371, 281))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.form = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.form.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.form.setContentsMargins(0, 0, 0, 0)
        self.form.setObjectName("form")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.form.setItem(1, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        self.usernameL = QtWidgets.QLabel(self.formLayoutWidget)
        self.usernameL.setObjectName("usernameL")
        self.form.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.usernameL)
        self.username = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.username.setObjectName("username")
        self.form.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.username)
        userText=self.username.text()
        self.passwordL = QtWidgets.QLabel(self.formLayoutWidget)
        self.passwordL.setObjectName("passwordL")
        self.form.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.passwordL)
        self.passwd = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.passwd.setObjectName("passwd")
        self.form.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.passwd)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.form.setItem(5, QtWidgets.QFormLayout.SpanningRole, spacerItem1)
        self.invia = QtWidgets.QPushButton(self.formLayoutWidget)
        self.invia.setObjectName("invia")
        self.form.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.invia)
        self.fallimento = QtWidgets.QLabel(self.formLayoutWidget)
        self.fallimento.setText("")
        self.fallimento.setObjectName("fallimento")
        self.form.setWidget(4, QtWidgets.QFormLayout.FieldRole,self.fallimento)
        self.invia.clicked.connect(lambda: self.invia_click(self.fallimento))
        self.retranslateUi(finestra)
        QtCore.QMetaObject.connectSlotsByName(finestra)

    def retranslateUi(self, finestra):
        _translate = QtCore.QCoreApplication.translate
        finestra.setWindowTitle(_translate("finestra", "LOG-IN"))
        self.usernameL.setText(_translate("finestra", "username:"))
        self.passwordL.setText(_translate("finestra", "password:"))
        self.invia.setText(_translate("finestra", "ACCEDI"))

    def invia_click(self,fallimento):
        import socket
        client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("localhost",8080))
        userText=self.username.text()
        passwdText=self.passwd.text()
        cred=userText+","+passwdText
        client.send(cred.encode())
        risp=client.recv(1024).decode()
        if risp=="credenziali_errate" or risp=="errore_login":
            self.fallimento.setText("credenziali errate")
        elif risp=="errore_connessione":
            self.fallimento.setText("errore_connessione")
        elif risp=="accesso_corretto":
            self.fallimento.setText("accesso corretto")
        client.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    finestra = QtWidgets.QDialog()
    ui = Ui_finestra()
    ui.setupUi(finestra)
    finestra.show()
    sys.exit(app.exec_())