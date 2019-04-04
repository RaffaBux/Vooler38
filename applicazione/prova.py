# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'temperature.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_temperature(object):
    def setupUi(self, temperature):
        temperature.setObjectName("temperature")
        temperature.resize(464, 387)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("2_icon38.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        temperature.setWindowIcon(icon)
        self.grigliatemp = QtWidgets.QWidget(temperature)
        self.grigliatemp.setObjectName("grigliatemp")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.grigliatemp)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tempLabel = QtWidgets.QLabel(self.grigliatemp)
        self.tempLabel.setObjectName("tempLabel")
        self.gridLayout_2.addWidget(self.tempLabel, 1, 0, 1, 1)
        self.monitoraggioButton = QtWidgets.QPushButton(self.grigliatemp)
        self.monitoraggioButton.setObjectName("monitoraggioButton")
        self.gridLayout_2.addWidget(self.monitoraggioButton, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 5, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 4, 0, 1, 1)
        self.statoLabel = QtWidgets.QLabel(self.grigliatemp)
        self.statoLabel.setObjectName("statoLabel")
        self.gridLayout_2.addWidget(self.statoLabel, 5, 2, 1, 1)
        self.tempmodificabileLabel = QtWidgets.QLabel(self.grigliatemp)
        self.tempmodificabileLabel.setObjectName("tempmodificabileLabel")
        self.gridLayout_2.addWidget(self.tempmodificabileLabel, 2, 0, 1, 1)
        self.temperaturaAtt = QtWidgets.QLabel(self.grigliatemp)
        self.temperaturaAtt.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.temperaturaAtt.setObjectName("temperaturaAtt")
        self.gridLayout_2.addWidget(self.temperaturaAtt, 1, 1, 1, 1)
        self.celsiusLabel1 = QtWidgets.QLabel(self.grigliatemp)
        self.celsiusLabel1.setObjectName("celsiusLabel1")
        self.gridLayout_2.addWidget(self.celsiusLabel1, 1, 2, 1, 1)
        self.celsiusLabel2 = QtWidgets.QLabel(self.grigliatemp)
        self.celsiusLabel2.setObjectName("celsiusLabel2")
        self.gridLayout_2.addWidget(self.celsiusLabel2, 2, 2, 1, 1)
        self.confermaButton = QtWidgets.QPushButton(self.grigliatemp)
        self.confermaButton.setObjectName("confermaButton")
        self.gridLayout_2.addWidget(self.confermaButton, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
        self.spintemp = QtWidgets.QDoubleSpinBox(self.grigliatemp)
        self.spintemp.setWrapping(False)
        self.spintemp.setFrame(True)
        self.spintemp.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spintemp.setReadOnly(False)
        self.spintemp.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spintemp.setAccelerated(False)
        self.spintemp.setKeyboardTracking(True)
        self.spintemp.setPrefix("")
        self.spintemp.setDecimals(1)
        self.spintemp.setMinimum(5.0)
        self.spintemp.setMaximum(25.0)
        self.spintemp.setSingleStep(0.1)
        self.spintemp.setProperty("value", 16.0)
        self.spintemp.setObjectName("spintemp")
        self.gridLayout_2.addWidget(self.spintemp, 2, 1, 1, 1)
        temperature.setCentralWidget(self.grigliatemp)

        self.retranslateUi(temperature)
        QtCore.QMetaObject.connectSlotsByName(temperature)

    def retranslateUi(self, temperature):
        _translate = QtCore.QCoreApplication.translate
        temperature.setWindowTitle(_translate("temperature", "******"))
        self.tempLabel.setText(_translate("temperature", "Temperatura ******:"))
        self.monitoraggioButton.setText(_translate("temperature", "Monitoraggio"))
        self.statoLabel.setText(_translate("temperature", "<html><head/><body><p><img src=\"gray.png\"/></p></body></html>"))
        self.tempmodificabileLabel.setText(_translate("temperature", "Temperatura modificabile: "))
        self.temperaturaAtt.setText(_translate("temperature", "---"))
        self.celsiusLabel1.setText(_translate("temperature", "°C"))
        self.celsiusLabel2.setText(_translate("temperature", "°C"))
        self.confermaButton.setText(_translate("temperature", "Conferma"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    temperature = QtWidgets.QMainWindow()
    ui = Ui_temperature()
    ui.setupUi(temperature)
    temperature.show()
    sys.exit(app.exec_())