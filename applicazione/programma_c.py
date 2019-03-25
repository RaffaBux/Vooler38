from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setObjectName("passwordLabel")
        self.gridLayout.addWidget(self.passwordLabel, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.passwordLine = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLine.setObjectName("passwordLine")
        self.gridLayout.addWidget(self.passwordLine, 3, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 3, 1, 1)
        self.usernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.usernameLabel.setObjectName("usernameLabel")
        self.gridLayout.addWidget(self.usernameLabel, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 5, 1, 1, 1)
        self.fallimentoLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.fallimentoLabel.setFont(font)
        self.fallimentoLabel.setText("")
        self.fallimentoLabel.setObjectName("fallimentoLabel")
        self.gridLayout.addWidget(self.fallimentoLabel, 4, 1, 1, 2)
        self.inviaButton = QtWidgets.QPushButton(self.centralwidget)
        self.inviaButton.setObjectName("inviaButton")
        self.inviaButton.clicked.connect(lambda: self.invia_click(self.fallimentoLabel))
        self.gridLayout.addWidget(self.inviaButton, 6, 1, 1, 2)
        self.usernameLine = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameLine.setObjectName("usernameLine")
        self.gridLayout.addWidget(self.usernameLine, 1, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 3, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 3, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 7, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LOGIN"))
        self.passwordLabel.setText(_translate("MainWindow", "password:"))
        self.usernameLabel.setText(_translate("MainWindow", "username:"))
        self.inviaButton.setText(_translate("MainWindow", "INVIA"))

    def invia_click(self,fallimento):
        import socket
        client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("localhost",8080))
        userText=self.usernameLine.text()
        passwdText=self.passwordLine.text()
        cred=userText+","+passwdText
        client.send(cred.encode())
        risp=client.recv(1024).decode()
        if risp=="credenziali_errate":
            self.fallimentoLabel.setText("credenziali errate")
            client.close()
        elif risp=="errore_connessione":
            self.fallimentoLabel.setText("errore_connessione")
            client.close()
        elif risp=="accesso_corretto":
            self.fallimentoLabel.setText("accesso corretto")
            client.close()
            '''self.refresh()

#prototipo refresh inizio

    def refresh(self):
        ui=clCantina()
        ui.functCantina(main)
        app.repaint()

class clCantina(object):
    def functCantina(self, finestraC):
        finestraC.setObjectName("CANTINA")
        self.lineEdit = QtWidgets.QLineEdit(finestraC)
        self.lineEdit.setGeometry(QtCore.QRect(130, 130, 113, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.retranslateUi(finestraC)
        QtCore.QMetaObject.connectSlotsByName(finestraC)

    def retranslateUi(self, finestraC):
        _translate = QtCore.QCoreApplication.translate
        finestraC.setWindowTitle(_translate("CANTINA", "CANTINA"))
        self.lineEdit.setText(_translate("CANTINA", "funziona"))

#fine prototipo refresh'''

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())