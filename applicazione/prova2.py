from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainGUI(object):
    def setupUi(self, MainGUI):
        MainGUI.setObjectName("MainGUI")
        MainGUI.resize(600, 540)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("2_icon38.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainGUI.setWindowIcon(icon)
        MainGUI.setStyleSheet("background-color: rgb(217, 240, 255);")
        self.main_grid = QtWidgets.QWidget(MainGUI)
        self.main_grid.setObjectName("main_grid")
        self.gridLayout = QtWidgets.QGridLayout(self.main_grid)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.passwordLabel = QtWidgets.QLabel(self.main_grid)
        self.passwordLabel.setObjectName("passwordLabel")
        self.gridLayout.addWidget(self.passwordLabel, 3, 1, 1, 1)
        self.passwordLine = QtWidgets.QLineEdit(self.main_grid)
        self.passwordLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLine.setObjectName("passwordLine")
        self.gridLayout.addWidget(self.passwordLine, 3, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 3, 1, 1)
        self.usernameLabel = QtWidgets.QLabel(self.main_grid)
        self.usernameLabel.setObjectName("usernameLabel")
        self.gridLayout.addWidget(self.usernameLabel, 1, 1, 1, 1)
        self.fallimentoLabel = QtWidgets.QLabel(self.main_grid)
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.fallimentoLabel.setFont(font)
        self.fallimentoLabel.setText("")
        self.fallimentoLabel.setObjectName("fallimentoLabel")
        self.gridLayout.addWidget(self.fallimentoLabel, 4, 1, 1, 2)
        self.inviaButton = QtWidgets.QPushButton(self.main_grid)
        font = QtGui.QFont()
        font.setKerning(False)
        self.inviaButton.setFont(font)
        self.inviaButton.setObjectName("inviaButton")
        self.inviaButton.clicked.connect(lambda: self.invia_click(self.fallimentoLabel))
        self.gridLayout.addWidget(self.inviaButton, 6, 1, 1, 2)
        self.usernameLine = QtWidgets.QLineEdit(self.main_grid)
        self.usernameLine.setObjectName("usernameLine")
        self.gridLayout.addWidget(self.usernameLine, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 3, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 0, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 7, 1, 1, 1)
        MainGUI.setCentralWidget(self.main_grid)
        self.retranslateUi(MainGUI)
        QtCore.QMetaObject.connectSlotsByName(MainGUI)

    def retranslateUi(self, MainGUI):
        _translate = QtCore.QCoreApplication.translate
        MainGUI.setWindowTitle(_translate("MainGUI", "LOGIN"))
        self.passwordLabel.setText(_translate("MainGUI", "password:"))
        self.usernameLabel.setText(_translate("MainGUI", "username:"))
        self.inviaButton.setText(_translate("MainGUI", "INVIA"))

    def invia_click(self,fallimento):
        import socket
        client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("localhost",8080))                                      #credenziali mutevoli
        userText=self.usernameLine.text()
        passwdText=self.passwordLine.text()
        cred=userText+","+passwdText
        client.send(cred.encode())
        risp=client.recv(1024).decode()
        if risp=="credenziali_errate":
            self.fallimentoLabel.setText("credenziali errate")
            client.close()
        elif risp=="errore_connessione" or risp=="":
            self.fallimentoLabel.setText("errore_connessione")
            client.close()
        elif risp=="accesso_corretto":
            self.fallimentoLabel.setText("accesso corretto")
            client.close()
            ui=Ui_CantinaGUI()
            ui.setupUi(MainGUI)

class Ui_CantinaGUI(object):
    def setupUi(self, CantinaGUI):
        name=[]
        CantinaGUI.setObjectName("CantinaGUI")
        CantinaGUI.setWindowModality(QtCore.Qt.WindowModal)
        CantinaGUI.setEnabled(True)
        '''CantinaGUI.resize(637, 769)
        CantinaGUI.setMinimumSize(QtCore.QSize(637, 769))'''
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        CantinaGUI.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("2_grappoloicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CantinaGUI.setWindowIcon(icon)
        CantinaGUI.setAutoFillBackground(True)
        CantinaGUI.setStyleSheet("")
        CantinaGUI.setAnimated(True)
        CantinaGUI.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(CantinaGUI)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.mappacantLabel = QtWidgets.QLabel(self.centralwidget)
        self.mappacantLabel.setObjectName("mappacantLabel")
        self.gridLayout_2.addWidget(self.mappacantLabel, 1, 0, 1, 1)
        self.list_scrollarea = QtWidgets.QScrollArea(self.centralwidget)
        self.list_scrollarea.setStyleSheet("background-color: rgb(233, 236, 255);")
        self.list_scrollarea.setWidgetResizable(True)
        self.list_scrollarea.setObjectName("list_scrollarea")
        self.list_grid = QtWidgets.QWidget()
        self.list_grid.setGeometry(QtCore.QRect(0, 0, 102, 1101))
        self.list_grid.setObjectName("list_grid")
        self.gridLayout = QtWidgets.QGridLayout(self.list_grid)
        self.gridLayout.setObjectName("gridLayout")
        self.vv16 = QtWidgets.QPushButton(self.list_grid)
        self.vv16.setObjectName("vv16")
        self.gridLayout.addWidget(self.vv16, 3, 0, 1, 1)
        self.locale2 = QtWidgets.QPushButton(self.list_grid)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.locale2.setFont(font)
        self.locale2.setStyleSheet("background-color: rgb(221, 237, 255);")
        self.locale2.setObjectName("locale2")
        name.append(self.locale2.objectName())
        self.locale2.clicked.connect(lambda: self.functemp(name[0]))
        self.gridLayout.addWidget(self.locale2, 9, 0, 1, 1)
        self.vv14 = QtWidgets.QPushButton(self.list_grid)
        self.vv14.setObjectName("vv14")
        name.append(self.vv14.objectName())
        self.vv14.clicked.connect(lambda: self.functemp(name[1]))
        self.gridLayout.addWidget(self.vv14, 1, 0, 1, 1)
        self.vv22 = QtWidgets.QPushButton(self.list_grid)
        self.vv22.setObjectName("vv22")
        name.append(self.vv22.objectName())
        self.vv22.clicked.connect(lambda: self.functemp(name[2]))
        self.gridLayout.addWidget(self.vv22, 21, 0, 1, 1)
        self.vv33 = QtWidgets.QPushButton(self.list_grid)
        self.vv33.setObjectName("vv33")
        name.append(self.vv33.objectName())
        self.vv33.clicked.connect(lambda: self.functemp(name[3]))
        self.gridLayout.addWidget(self.vv33, 32, 0, 1, 1)
        self.vv7 = QtWidgets.QPushButton(self.list_grid)
        self.vv7.setObjectName("vv7")
        name.append(self.vv7.objectName())
        self.vv7.clicked.connect(lambda: self.functemp(name[4]))
        self.gridLayout.addWidget(self.vv7, 13, 0, 1, 1)
        self.vv32 = QtWidgets.QPushButton(self.list_grid)
        self.vv32.setObjectName("vv32")
        name.append(self.vv14.objectName())
        self.vv14.clicked.connect(lambda: self.functemp(name[0]))
        self.gridLayout.addWidget(self.vv32, 31, 0, 1, 1)
        self.vv19 = QtWidgets.QPushButton(self.list_grid)
        self.vv19.setObjectName("vv19")
        name.append(self.vv14.objectName())
        self.vv14.clicked.connect(lambda: self.functemp(name[0]))
        self.gridLayout.addWidget(self.vv19, 6, 0, 1, 1)
        self.vv15 = QtWidgets.QPushButton(self.list_grid)
        self.vv15.setObjectName("vv15")
        name.append(self.vv14.objectName())
        self.vv14.clicked.connect(lambda: self.functemp(name[0]))
        self.gridLayout.addWidget(self.vv15, 2, 0, 1, 1)
        self.vv27 = QtWidgets.QPushButton(self.list_grid)
        self.vv27.setObjectName("vv27")
        name.append(self.vv14.objectName())
        self.vv14.clicked.connect(lambda: self.functemp(name[0]))
        self.gridLayout.addWidget(self.vv27, 26, 0, 1, 1)
        self.vv25 = QtWidgets.QPushButton(self.list_grid)
        self.vv25.setObjectName("vv25")
        name.append(self.vv14.objectName())
        self.vv14.clicked.connect(lambda: self.functemp(name[0]))
        self.gridLayout.addWidget(self.vv25, 24, 0, 1, 1)
        self.vv23 = QtWidgets.QPushButton(self.list_grid)
        self.vv23.setObjectName("vv23")
        name.append(self.vv14.objectName())
        self.vv14.clicked.connect(lambda: self.functemp(name[0]))
        self.gridLayout.addWidget(self.vv23, 22, 0, 1, 1)
        self.vv8 = QtWidgets.QPushButton(self.list_grid)
        self.vv8.setObjectName("vv8")
        name.append(self.vv14.objectName())
        self.vv14.clicked.connect(lambda: self.functemp(name[0]))
        self.gridLayout.addWidget(self.vv8, 14, 0, 1, 1)
        self.vv29 = QtWidgets.QPushButton(self.list_grid)
        self.vv29.setObjectName("vv29")
        name.append(self.vv14.objectName())
        self.vv14.clicked.connect(lambda: self.functemp(name[0]))
        self.gridLayout.addWidget(self.vv29, 28, 0, 1, 1)
        self.vv30 = QtWidgets.QPushButton(self.list_grid)
        self.vv30.setObjectName("vv30")
        name.append(self.vv14.objectName())
        self.vv14.clicked.connect(lambda: self.functemp(name[0]))
        self.gridLayout.addWidget(self.vv30, 29, 0, 1, 1)
        self.vv17 = QtWidgets.QPushButton(self.list_grid)
        self.vv17.setObjectName("vv17")
        name.append(self.vv14.objectName())
        self.vv14.clicked.connect(lambda: self.functemp(name[0]))
        self.gridLayout.addWidget(self.vv17, 4, 0, 1, 1)
        self.locale3 = QtWidgets.QPushButton(self.list_grid)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.locale3.setFont(font)
        self.locale3.setStyleSheet("background-color: rgb(221, 237, 255);")
        self.locale3.setObjectName("locale3")
        name.append(self.vv14.objectName())
        self.vv14.clicked.connect(lambda: self.functemp(name[0]))
        self.gridLayout.addWidget(self.locale3, 20, 0, 1, 1)
        self.vv28 = QtWidgets.QPushButton(self.list_grid)
        self.vv28.setObjectName("vv28")
        name.append(self.vv14.objectName())
        self.vv14.clicked.connect(lambda: self.functemp(name[0]))
        self.gridLayout.addWidget(self.vv28, 27, 0, 1, 1)
        self.vv24 = QtWidgets.QPushButton(self.list_grid)
        self.vv24.setObjectName("vv24")
        name.append(self.vv14.objectName())
        self.vv14.clicked.connect(lambda: self.functemp(name[0]))
        self.gridLayout.addWidget(self.vv24, 23, 0, 1, 1)
        self.vv20 = QtWidgets.QPushButton(self.list_grid)
        self.vv20.setObjectName("vv20")
        name.append(self.vv14.objectName())
        self.vv14.clicked.connect(lambda: self.functemp(name[0]))
        self.gridLayout.addWidget(self.vv20, 7, 0, 1, 1)
        self.vv18 = QtWidgets.QPushButton(self.list_grid)
        self.vv18.setObjectName("vv18")
        name.append(self.vv14.objectName())
        self.vv14.clicked.connect(lambda: self.functemp(name[0]))
        self.gridLayout.addWidget(self.vv18, 5, 0, 1, 1)
        self.vv21 = QtWidgets.QPushButton(self.list_grid)
        self.vv21.setObjectName("vv21")
        name.append(self.vv14.objectName())
        self.vv14.clicked.connect(lambda: self.functemp(name[0]))
        self.gridLayout.addWidget(self.vv21, 8, 0, 1, 1)
        self.vv10 = QtWidgets.QPushButton(self.list_grid)
        self.vv10.setObjectName("vv10")
        name.append(self.vv14.objectName())
        self.vv14.clicked.connect(lambda: self.functemp(name[0]))
        self.gridLayout.addWidget(self.vv10, 16, 0, 1, 1)
        self.vv31 = QtWidgets.QPushButton(self.list_grid)
        self.vv31.setObjectName("vv31")
        name.append(self.vv14.objectName())
        self.vv14.clicked.connect(lambda: self.functemp(name[0]))
        self.gridLayout.addWidget(self.vv31, 30, 0, 1, 1)
        self.vv26 = QtWidgets.QPushButton(self.list_grid)
        self.vv26.setObjectName("vv26")
        name.append(self.vv14.objectName())
        self.vv14.clicked.connect(lambda: self.functemp(name[0]))
        self.gridLayout.addWidget(self.vv26, 25, 0, 1, 1)
        self.vv11 = QtWidgets.QPushButton(self.list_grid)
        self.vv11.setObjectName("vv11")
        name.append(self.vv14.objectName())
        self.vv14.clicked.connect(lambda: self.functemp(name[0]))
        self.gridLayout.addWidget(self.vv11, 17, 0, 1, 1)
        self.vv12 = QtWidgets.QPushButton(self.list_grid)
        self.vv12.setObjectName("vv12")
        name.append(self.vv14.objectName())
        self.vv14.clicked.connect(lambda: self.functemp(name[0]))
        self.gridLayout.addWidget(self.vv12, 18, 0, 1, 1)
        self.vv13 = QtWidgets.QPushButton(self.list_grid)
        self.vv13.setObjectName("vv13")
        name.append(self.vv14.objectName())
        self.vv14.clicked.connect(lambda: self.functemp(name[0]))
        self.gridLayout.addWidget(self.vv13, 19, 0, 1, 1)
        self.vv6 = QtWidgets.QPushButton(self.list_grid)
        self.vv6.setObjectName("vv6")
        name.append(self.vv14.objectName())
        self.vv14.clicked.connect(lambda: self.functemp(name[0]))
        self.gridLayout.addWidget(self.vv6, 12, 0, 1, 1)
        self.vv4 = QtWidgets.QPushButton(self.list_grid)
        self.vv4.setObjectName("vv4")
        name.append(self.vv14.objectName())
        self.vv14.clicked.connect(lambda: self.functemp(name[0]))
        self.gridLayout.addWidget(self.vv4, 10, 0, 1, 1)
        self.vv5 = QtWidgets.QPushButton(self.list_grid)
        self.vv5.setObjectName("vv5")
        name.append(self.vv14.objectName())
        self.vv14.clicked.connect(lambda: self.functemp(name[0]))
        self.gridLayout.addWidget(self.vv5, 11, 0, 1, 1)
        self.locale1 = QtWidgets.QPushButton(self.list_grid)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.locale1.setFont(font)
        self.locale1.setStyleSheet("background-color: rgb(221, 237, 255);")
        self.locale1.setObjectName("locale1")
        name.append(self.vv14.objectName())
        self.vv14.clicked.connect(lambda: self.functemp(name[0]))
        self.gridLayout.addWidget(self.locale1, 0, 0, 1, 1)
        self.vv9 = QtWidgets.QPushButton(self.list_grid)
        self.vv9.setObjectName("vv9")
        name.append(self.vv14.objectName())
        self.vv14.clicked.connect(lambda: self.functemp(name[0]))
        self.gridLayout.addWidget(self.vv9, 15, 0, 1, 1)
        self.list_scrollarea.setWidget(self.list_grid)
        self.gridLayout_2.addWidget(self.list_scrollarea, 0, 1, 2, 1)
        self.top_grid = QtWidgets.QGridLayout()
        self.top_grid.setObjectName("top_grid")
        self.dataoraTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dataoraTimeEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dataoraTimeEdit.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.dataoraTimeEdit.setFrame(False)
        self.dataoraTimeEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dataoraTimeEdit.setReadOnly(True)
        self.dataoraTimeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dataoraTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 4, 5), QtCore.QTime(10, 0, 0)))
        self.dataoraTimeEdit.setDate(QtCore.QDate(2019, 4, 5))
        self.dataoraTimeEdit.setTime(QtCore.QTime(10, 0, 0))
        self.dataoraTimeEdit.setMaximumDate(QtCore.QDate(7999, 12, 31))
        self.dataoraTimeEdit.setObjectName("dataoraTimeEdit")
        self.top_grid.addWidget(self.dataoraTimeEdit, 0, 1, 1, 1)
        self.tempestLabel = QtWidgets.QLabel(self.centralwidget)
        self.tempestLabel.setObjectName("tempestLabel")
        self.top_grid.addWidget(self.tempestLabel, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.top_grid, 0, 0, 1, 1)
        CantinaGUI.setCentralWidget(self.centralwidget)
        self.retranslateUi(CantinaGUI)
        QtCore.QMetaObject.connectSlotsByName(CantinaGUI)

    def retranslateUi(self, CantinaGUI):
        _translate = QtCore.QCoreApplication.translate
        CantinaGUI.setWindowTitle(_translate("CantinaGUI", "MAPPA VASI VINARI"))
        self.mappacantLabel.setText(_translate("CantinaGUI", "<html><head/><body><p><img src=\"3_Planimetria_Botti.png\"/></p></body></html>"))
        self.vv16.setText(_translate("CantinaGUI", "v.v. 16"))
        self.locale2.setText(_translate("CantinaGUI", "LOCALE 2"))
        self.vv14.setText(_translate("CantinaGUI", "v.v. 14"))
        self.vv22.setText(_translate("CantinaGUI", "v.v. 22"))
        self.vv33.setText(_translate("CantinaGUI", "v.v. 33"))
        self.vv7.setText(_translate("CantinaGUI", "v.v. 7"))
        self.vv32.setText(_translate("CantinaGUI", "v.v. 32"))
        self.vv19.setText(_translate("CantinaGUI", "v.v. 19"))
        self.vv15.setText(_translate("CantinaGUI", "v.v. 15"))
        self.vv27.setText(_translate("CantinaGUI", "v.v. 27"))
        self.vv25.setText(_translate("CantinaGUI", "v.v. 25"))
        self.vv23.setText(_translate("CantinaGUI", "v.v. 23"))
        self.vv8.setText(_translate("CantinaGUI", "v.v. 8"))
        self.vv29.setText(_translate("CantinaGUI", "v.v. 29"))
        self.vv30.setText(_translate("CantinaGUI", "v.v. 30"))
        self.vv17.setText(_translate("CantinaGUI", "v.v. 17"))
        self.locale3.setText(_translate("CantinaGUI", "LOCALE 3"))
        self.vv28.setText(_translate("CantinaGUI", "v.v. 28"))
        self.vv24.setText(_translate("CantinaGUI", "v.v. 24"))
        self.vv20.setText(_translate("CantinaGUI", "v.v. 20"))
        self.vv18.setText(_translate("CantinaGUI", "v.v. 18"))
        self.vv21.setText(_translate("CantinaGUI", "v.v. 21"))
        self.vv10.setText(_translate("CantinaGUI", "v.v. 10"))
        self.vv31.setText(_translate("CantinaGUI", "v.v. 31"))
        self.vv26.setText(_translate("CantinaGUI", "v.v. 26"))
        self.vv11.setText(_translate("CantinaGUI", "v.v. 11"))
        self.vv12.setText(_translate("CantinaGUI", "v.v. 12"))
        self.vv13.setText(_translate("CantinaGUI", "v.v. 13"))
        self.vv6.setText(_translate("CantinaGUI", "v.v. 6"))
        self.vv4.setText(_translate("CantinaGUI", "v.v. 4"))
        self.vv5.setText(_translate("CantinaGUI", "v.v. 5"))
        self.locale1.setText(_translate("CantinaGUI", "LOCALE 1"))
        self.vv9.setText(_translate("CantinaGUI", "v.v. 9"))
        self.tempestLabel.setText(_translate("CantinaGUI", "Temperatura esterna: *****°C"))

    def functemp(self, name):
        command = name + ""
        eval(command)
        print(sb)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainGUI = QtWidgets.QMainWindow()
    ui = Ui_MainGUI()
    ui.setupUi(MainGUI)
    MainGUI.showMaximized()
    sys.exit(app.exec_())

