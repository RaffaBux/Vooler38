from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ServerGUI(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui_ServerGUI, self).__init__
        self.setupUi(self)
        self.showMaximized

    def setupUi(self, Server):
        listaLabel=[]
        Server.setObjectName("Server")
        Server.resize(564, 354)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("2_icon38Server.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Server.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Server)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.StatoServerLabel = QtWidgets.QLabel(self.centralwidget)
        self.StatoServerLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.StatoServerLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.StatoServerLabel.setObjectName("StatoServerLabel")
        self.horizontalLayout.addWidget(self.StatoServerLabel)
        self.StatoLabel = QtWidgets.QLabel(self.centralwidget)
        self.StatoLabel.setObjectName("StatoLabel")
        self.horizontalLayout.addWidget(self.StatoLabel)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollContent = QtWidgets.QWidget()
        self.scrollContent.setGeometry(QtCore.QRect(0, 0, 542, 300))
        self.scrollContent.setObjectName("scrollContent")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollContent)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.AggLabel = QtWidgets.QLabel(self.scrollContent)
        self.AggLabel.setObjectName("AggLabel")
        self.gridLayout_2.addWidget(self.AggLabel, 0, 0, 1, 1)
        listaLabel.append(self.AggLabel)
        self.scrollArea.setWidget(self.scrollContent)
        self.verticalLayout.addWidget(self.scrollArea)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        Server.setCentralWidget(self.centralwidget)
        self.retranslateUi(Server)
        QtCore.QMetaObject.connectSlotsByName(Server)
        self.backend(listaLabel)

    def retranslateUi(self, Server):
        _translate = QtCore.QCoreApplication.translate
        Server.setWindowTitle(_translate("Server", "MainWindow"))
        self.StatoServerLabel.setText(_translate("Server", "Stato server:"))
        self.StatoLabel.setText(_translate("Server", "***"))
        self.label.setText(_translate("Server", "<html><head/><body><p><img src=\"gray.png\"/></p></body></html>"))
        self.AggLabel.setText(_translate("Server", "DATA > CODICE"))

    def backend(self, lista):
        from threading import Thread
        import socket
        import mysql.connector as mys
        global ind
        ind=1
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("localhost", 8282)) #indirizzo macchina
        s.listen(10)
        while True:
            try:
                connClient, ipClient = s.accept()
                cred=connClient.recv(1024).decode() #0 username, 1 password, 2 codIstruzione, 3&&+ info aggiuntive
                cod=cred.split(",")
                if int(cod[2])==0:      #login
                    print(cod)
                    try:
                        mydb0=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Login")  #credenziali mysql
                        myc0=mydb0.cursor()
                        myc0.execute("select username,password from Utente where username='"+str(cod[0])+"' and password='"+str(cod[1])+"'")
                        record=myc0.fetchone()
                        if record[0]==str(cod[0]) and record[1]==str(cod[1]):
                            connClient.send("accesso_corretto".encode())
                        else:
                            connClient.send("credenziali_errate".encode())
                        mydb0.close()
                    except Exception as e:
                        print(e)
                        connClient.send("credenziali_errate".encode())
                        mydb0.close()
                elif int(cod[2])==1:    #temperatura esterna
                    print(cod)
                    try:
                        mydb1=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Esterno")   #credenziali mysql
                        myc1=mydb1.cursor()
                        myc1.execute("select tempEsterno from Esterno where idEsterno=1")
                        record=myc1.fetchone()
                        connClient.send(str(record[0]).encode())
                    except BrokenPipeError:
                        mydb1.close()
                    except:
                        connClient.send("*****".encode())
                        mydb1.close()
                elif int(cod[2])==2:    #temperature botti e locali e controllo sonda
                    print(cod)
                    cod=str(cod[3]).split(" ")
                    try:
                        mydb2=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Cantina") #credenziali mysql
                        myc2=mydb2.cursor()
                        if cod[0]=="Vaso":
                            myc2.execute("select statoS from Sonda where idBotte="+str(cod[2]))
                            attivo=myc2.fetchone()
                        else:
                            myc2.execute("select statoS from Sonda where idLocale="+str(cod[1]))
                            attivo=myc2.fetchone()
                        if attivo[0]==1:
                            if cod[0]=="Vaso":
                                myc2.execute("select tempBotte from Botte where idBotte="+str(cod[2]))
                                record=myc2.fetchone()
                                connClient.send(str(record[0]).encode())
                            else:
                                myc2.execute("select tempLocale from Locale where idLocale="+str(cod[1]))
                                record=myc2.fetchone()
                                connClient.send(str(record[0]).encode())
                        else:
                            connClient.send("**sonda disinserita**".encode())
                    except BrokenPipeError:
                        mydb2.close()
                    except Exception as e:
                        print(e)
                        connClient.send("*****".encode())
                        mydb2.close()
                elif int(cod[2])==3:    #contenuto
                    print(cod)
                    cod=str(cod[3]).split(" ")
                    try:
                        mydb3=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Cantina") #credenziali mysql
                        myc3=mydb3.cursor()
                        myc3.execute("select contenuto from Botte where idBotte="+str(cod[2]))
                        record=myc3.fetchone()
                        connClient.send(str(record[0]).encode())
                    except BrokenPipeError:
                        mydb3.close()
                    except Exception as e:
                        print(e)
                        connClient.send("*****".encode())
                        mydb3.close()
                elif int(cod[2])==4:    #reset spin
                    print(cod)
                    cod=str(cod[3]).split(" ")
                    try:
                        if cod[0]=="Vaso":
                            mydb4=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Cantina") #credenziali mysql
                            myc4=mydb4.cursor()
                            myc4.execute("select tempsetBotte from Botte where idBotte="+str(cod[2]))
                            record=myc4.fetchone()
                            connClient.send(str(record[0]).encode())
                        else:
                            mydb4=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Cantina") #credenziali mysql
                            myc4=mydb4.cursor()
                            myc4.execute("select tempsetLocale from Locale where idLocale="+str(cod[1]))
                            record=myc4.fetchone()
                            connClient.send(str(record[0]).encode())
                    except BrokenPipeError:
                        mydb4.close()
                    except Exception as e:
                        print(e)
                        connClient.send("16.0".encode())
                        mydb4.close()
                elif int(cod[2])==5:    #conferma spin
                    print(cod)
                    valore=cod[4]
                    cod=str(cod[3]).split(" ")
                    try:
                        if cod[0]=="Vaso":
                            mydb5=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Cantina") #credenziali mysql
                            myc5=mydb5.cursor()
                            myc5.execute("select idBotte,contenuto,tempBotte,tempsetBotte,volume from Botte where idBotte="+str(cod[2]))
                            record=myc5.fetchone()
                            myc5.execute("insert into StoricoBotte(dataAggB,contenutoAggB,tempAggB,tempsetAggB,volumeAggB,idBotte,flagContenuto,flagTemperatura,flagTemperaturaSet,flagVolume)values(now(),'"+str(record[1])+"',"+str(record[2])+","+str(record[3])+","+str(record[4])+","+str(record[0])+",0,0,1,0)")
                            myc5.execute("update Botte set tempsetBotte="+str(valore)+" where idBotte="+str(cod[2]))
                            mydb5.commit()
                        else:
                            mydb5=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Cantina") #credenziali mysql
                            myc5=mydb5.cursor()
                            myc5.execute("select idLocale,tempLocale,tempsetLocale from Locale where idLocale="+str(cod[1]))
                            record=myc5.fetchone()
                            myc5.execute("insert into StoricoLocale(dataAggL,tempAggL,tempsetAggL,idLocale,flagTemperatura,flagTemperaturaSet)values(now(),"+str(record[1])+","+str(record[2])+","+str(record[0])+",0,1)")
                            myc5.execute("update Locale set tempsetLocale="+str(valore)+" where idLocale="+str(cod[1]))
                            mydb5.commit()
                        connClient.send("temperatura aggiornata".encode())
                    except BrokenPipeError:
                        mydb5.close()
                    except Exception as e:
                        print(e)
                        mydb5.rollback()
                        connClient.send("errore aggiornamento".encode())
                        mydb5.close()
                elif int(cod[2])==6:    #grafico monitoraggio temperature
                    print(cod)
                    misure=""
                    quando=""
                    dati=""
                    cod=str(cod[3]).split(" ")
                    try:
                        if cod[0]=="Vaso":
                            mydb6=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Cantina") #credenziali mysql
                            myc6=mydb6.cursor()
                            myc6.execute("select tempAggB from StoricoBotte where idBotte="+str(cod[2])+" order by dataAggB desc limit 10")
                            recordTemp=myc6.fetchall()
                            myc6.execute("select dataAggB from StoricoBotte where idBotte="+str(cod[2])+" order by dataAggB desc limit 10")
                            recordDate=myc6.fetchall()
                        else:
                            mydb6=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Cantina") #credenziali mysql
                            myc6=mydb6.cursor()
                            myc6.execute("select tempAggL from StoricoLocale where idLocale="+str(cod[1])+" order by dataAggL desc limit 10")
                            recordTemp=myc6.fetchall()
                            myc6.execute("select dataAggL from StoricoLocale where idLocale="+str(cod[1])+" order by dataAggL desc limit 10")
                            recordDate=myc6.fetchall()
                        c=0
                        for i in recordTemp:
                            try:
                                misure=misure+str(i[0])
                                c+=1
                                if c<len(recordTemp):
                                    misure=misure+","
                            except:
                                c+=1
                                pass
                        c=0
                        for i in recordDate:
                            try:
                                quando=quando+str(i[0])
                                c+=1
                                if c<len(recordDate):
                                    quando=quando+","
                            except:
                                c+=1
                                pass
                        dati=misure+";"+quando
                        connClient.send(dati.encode())
                    except BrokenPipeError:
                        mydb6.close()
                    except Exception as e:
                        print(e)
                        connClient.send("errore invio dati".encode())
                        mydb6.close()
                elif int(cod[2])==7:    #grafico monitoraggio quantità
                    print(cod)
                    misure=""
                    quando=""
                    dati=""
                    c=0
                    cod=str(cod[3]).split(" ")
                    try:
                        mydb7=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Cantina") #credenziali mysql
                        myc7=mydb7.cursor()
                        myc7.execute("select volumeAggB from StoricoBotte where idBotte="+str(cod[2])+" and flagVolume=1 order by dataAggB desc limit 10")
                        recordQuant=myc7.fetchall()
                        myc7.execute("select dataAggB from StoricoBotte where idBotte="+str(cod[2])+" and flagVolume=1 order by dataAggB desc limit 10")
                        recordDate=myc7.fetchall()
                        for i in recordQuant:
                            try:
                                misure=misure+str(i[0])
                                c+=1
                                if c<len(recordQuant):
                                    misure=misure+","
                            except:
                                c+=1
                                pass
                        c=0
                        for i in recordDate:
                            try:
                                quando=quando+str(i[0])
                                c+=1
                                if c<len(recordDate):
                                    quando=quando+","
                            except:
                                c+=1
                                pass
                        dati=misure+";"+quando
                        connClient.send(dati.encode())
                    except BrokenPipeError:
                        mydb7.close()
                    except Exception as e:
                        print(e)
                        connClient.send("errore invio dati".encode())
                        mydb7.close()
                elif int(cod[2])==8:    #controllo avarie valvole
                    print(cod)
                    cod=str(cod[3]).split(" ")
                    try:
                        mydb8=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Cantina") #credenziali mysql
                        myc8=mydb8.cursor()
                        if cod[0]=="Vaso":
                            myc8.execute("select statoV, funzV from Sonda,Botte where Sonda.idSondaV=Botte.idSondaV and Sonda.idBotte="+str(cod[2]))
                        else:
                            myc8.execute("select statoV, funzV from Sonda,Locale where Sonda.idSondaV=Locale.idSondaV and Sonda.idLocale="+str(cod[1]))
                        record=myc8.fetchone()
                        if record[0]==0 and record[1]==0:
                            connClient.send("disinserita".encode())
                        elif record[0]==0 and record[1]==1:
                            connClient.send("avaria".encode())
                        elif record[0]==1 and record[1]==0:
                            connClient.send("off".encode())
                        elif record[0]==1 and record[1]==1:
                            connClient.send("on".encode())
                    except BrokenPipeError:
                        mydb8.close()
                    except Exception as e:
                        print(e)
                        connClient.send("*****".encode())
                        mydb8.close()
            except KeyboardInterrupt:
                s.close()
                print("server chiuso")
                break
            except:
                pass
            aggLabel=Thread(target=self.aggScroll, args=[self.lista, ind, cod])
            aggLabel.start()

    def aggScroll(self, lista, ind, cod):
        from datetime import time, date
        if ind>=20:
            self.gridLayout_2.removeWidget(lista[1])
            ind-=1
        oggi=date.today()
        ora=time.now()
        self.AggLabel = QtWidgets.QLabel(self.scrollContent)
        self.AggLabel.setObjectName("AggLabel")
        self.gridLayout_2.addWidget(self.AggLabel, 0, ind, 1, 1)
        self.AggLabel.setText(str(oggi)+" "+str(ora)+" > ")
        lista.append(self.AggLabel)
        ind+=1

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_ServerGUI()
    sys.exit(app.exec_())