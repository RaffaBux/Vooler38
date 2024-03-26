from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ServerGUI(QtWidgets.QMainWindow):

    scrolling_signal = QtCore.pyqtSignal([list])

    def __init__(self):
        super(Ui_ServerGUI, self).__init__()
        self.setupUi(self)
        self.showMaximized()

    def closeEvent(self, event):
        try:
            threadMainPace=False
            app.closeAllWindows()
        except:
            pass

    def setupUi(self, Server):
        from threading import Thread
        threadMainPace=True
        listaLabel=[]
        Server.setObjectName("Server")
        Server.resize(564, 265)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("2_icon38Server.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Server.setWindowIcon(icon)
        Server.setStyleSheet("background-color: rgb(217, 240, 255);")
        self.centralwidget = QtWidgets.QWidget(Server)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.statoServerLabel = QtWidgets.QLabel(self.centralwidget)
        self.statoServerLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.statoServerLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statoServerLabel.setObjectName("statoServerLabel")
        self.horizontalLayout.addWidget(self.statoServerLabel)
        self.statoLabel = QtWidgets.QLabel(self.centralwidget)
        self.statoLabel.setObjectName("statoLabel")
        self.horizontalLayout.addWidget(self.statoLabel)
        self.imgLabel = QtWidgets.QLabel(self.centralwidget)
        self.imgLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.imgLabel.setObjectName("imgLabel")
        self.horizontalLayout.addWidget(self.imgLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollContent = QtWidgets.QWidget()
        self.scrollContent.setGeometry(QtCore.QRect(0, 0, 529, 472))
        self.scrollContent.setObjectName("scrollContent")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollContent)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea.setWidget(self.scrollContent)
        self.verticalLayout.addWidget(self.scrollArea)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        Server.setCentralWidget(self.centralwidget)
        self.retranslateUi(Server)
        QtCore.QMetaObject.connectSlotsByName(Server)
        self.scrolling_signal.connect(self.aggScroll)
        be=Thread(target=self.backend, args=[lambda: threadMainPace, listaLabel], daemon=True)
        be.start()

    def retranslateUi(self, Server):
        _translate = QtCore.QCoreApplication.translate
        Server.setWindowTitle(_translate("Server", "Server"))
        self.statoServerLabel.setText(_translate("Server", "Stato server:"))
        self.statoLabel.setText(_translate("Server", "***"))
        self.imgLabel.setText(_translate("Server", "<html><head/><body><p><img src=\"gray.png\"/></p></body></html>"))

    def imgServer(self, imgLabel, stato, exit):
        while exit():
            try:
                if stato==0:
                    self.imgLabel.setText("<html><head/><body><p><img src=\"gray.png\"/></p></body></html>")
                    self.statoLabel.setText("Inattivo")
                elif stato==1:
                    self.imgLabel.setText("<html><head/><body><p><img src=\"green.png\"/></p></body></html>")
                    self.statoLabel.setText("Attivo")
                else:
                    self.imgLabel.setText("<html><head/><body><p><img src=\"red.png\"/></p></body></html>")
                    self.statoLabel.setText("Avaria")
            except Exception as e:
                print(e)    ###debug

    def acqFunct(self, exit):
        import mysql.connector as mys
        import serial
        import time
        arduino = serial.Serial('COM18', 115200, timeout=0)
        while exit():
            dati=arduino.readline()
            if dati:
                try:
                    datiDec = dati.decode('utf-8')
                    print(datiDec) #debug
                    valore=datiDec.split(";")          #1[0] = master, nomeslave[1],nomesonda[2];statosonda[3];nomevalvola[4];statovalvola[5];statovalvolaaperta[6] (3[6] = avaria/2[6] = spina staccata); temperatura[7]; 1[8] = anomalia/0[8] = normale;
                    mydb9=mys.connect(host="localhost", user="vignaiolo", passwd="vigna38", database="Cantina")
                    myc9=mydb9.cursor()
                    myc9.execute("select idSondaV,statoS,statoV,funzV from Sonda where idBotte=14")  #esempio esame
                    record=myc9.fetchone()
                    if str(record[1])!=str(valore[3]):
                        flagStatoS = 1
                    else:
                        flagStatoS = 0
                    if str(record[2])!=str(valore[5]):
                        flagStatoV = 1
                    else:
                        flagStatoV = 0
                    if str(record[3])!=str(valore[6]):
                        flagFunzionamentoV = 1
                    else:
                        flagFunzionamentoV = 0
                    myc9.execute("insert into StoricoSonda(dataAggS,statoAggS,flagStatoS,statoAggV,flagStatoV,funzAggV,flagFunzionamentoV,idSondaV)values(now(),"+str(record[1])+","+str(flagStatoS)+","+str(record[2])+","+str(flagStatoV)+","+str(record[3])+","+str(flagFunzionamentoV)+","+str(record[0])+")")
                    myc9.execute("update Sonda set statoS="+str(valore[3])+", statoV="+str(valore[5])+", funzV="+str(valore[6])+" where idSondaV="+str(valore[2]))
                    myc9.execute("select idBotte,contenuto,tempBotte,tempsetBotte,volume from Botte where idBotte=14")  #esempio esame
                    record=myc9.fetchone()
                    myc9.execute("insert into StoricoBotte(dataAggB,contenutoAggB,tempAggB,tempsetAggB,volumeAggB,idBotte,flagContenuto,flagTemperatura,flagTemperaturaSet,flagVolume)values(now(),'"+str(record[1])+"',"+str(record[2])+","+str(record[3])+","+str(record[4])+","+str(record[0])+",0,1,0,0)")
                    myc9.execute("update Botte set tempbotte="+str(valore[7])+" where idBotte="+str(valore[2]))
                    mydb9.commit()
                except Exception as e:
                    print(e)
                
    def confFunc(self, valore):
        import serial
        import time
        try:
            val = valore.split(".")
            arduino = serial.Serial('COM18', 115200, timeout=0)
            arduino.write(val[0].encode())
            dati=arduino.readline()
            print(dati.decode('utf-8'))
            arduino.close()
        except Exception as e:
            arduino.close()

    def backend(self, exit, listaLabel):
        from threading import Thread
        import socket
        import mysql.connector as mys
        import serial
        stato=0
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("192.168.0.3", 8282)) #indirizzo macchina
        s.listen(10)
        acquisizione = Thread(target=self.acqFunct, args = [exit], daemon = True)
        acquisizione.start()
        while exit():
            try:                 
                statoServer=Thread(target=self.imgServer, args=[self.imgLabel, stato, exit], daemon=True)
                statoServer.start()
                connClient, ipClient = s.accept()
                cred=connClient.recv(1024).decode() #0 username, 1 password, 2 codIstruzione, 3&&+ info aggiuntive
                cod=cred.split(",")
                arrDati=cod
                if int(cod[2])==0:      #login
                    try:
                        mydb0=mys.connect(host="localhost", user="vignaiolo", passwd="vigna38", database="Login")  #credenziali mysql
                        myc0=mydb0.cursor()
                        myc0.execute("select username,password from Utente where username='"+str(cod[0])+"' and password='"+str(cod[1])+"'")
                        record=myc0.fetchone()
                        if record[0]==str(cod[0]) and record[1]==str(cod[1]):
                            connClient.send("accesso_corretto".encode())
                        else:
                            connClient.send("credenziali_errate".encode())
                        mydb0.close()
                    except:
                        connClient.send("credenziali_errate".encode())
                        mydb0.close()
                elif int(cod[2])==1:    #temperatura esterna
                    try:
                        mydb1=mys.connect(host="localhost", user="vignaiolo", passwd="vigna38", database="Esterno")   #credenziali mysql
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
                    cod=str(cod[3]).split(" ")
                    try:
                        mydb2=mys.connect(host="localhost", user="vignaiolo", passwd="vigna38", database="Cantina") #credenziali mysql
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
                    cod=str(cod[3]).split(" ")
                    try:
                        mydb3=mys.connect(host="localhost", user="vignaiolo", passwd="vigna38", database="Cantina") #credenziali mysql
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
                    cod=str(cod[3]).split(" ")
                    try:
                        if cod[0]=="Vaso":
                            mydb4=mys.connect(host="localhost", user="vignaiolo", passwd="vigna38", database="Cantina") #credenziali mysql
                            myc4=mydb4.cursor()
                            myc4.execute("select tempsetBotte from Botte where idBotte="+str(cod[2]))
                            record=myc4.fetchone()
                            connClient.send(str(record[0]).encode())
                        else:
                            mydb4=mys.connect(host="localhost", user="vignaiolo", passwd="vigna38", database="Cantina") #credenziali mysql
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
                    try:
                        valore=cod[4]
                        cod=str(cod[3]).split(" ")
                        if cod[0]=="Vaso":
                            mydb5=mys.connect(host="localhost", user="vignaiolo", passwd="vigna38", database="Cantina") #credenziali mysql
                            myc5=mydb5.cursor()
                            myc5.execute("select idBotte,contenuto,tempBotte,tempsetBotte,volume from Botte where idBotte="+str(cod[2]))
                            record=myc5.fetchone()
                            myc5.execute("insert into StoricoBotte(dataAggB,contenutoAggB,tempAggB,tempsetAggB,volumeAggB,idBotte,flagContenuto,flagTemperatura,flagTemperaturaSet,flagVolume)values(now(),'"+str(record[1])+"',"+str(record[2])+","+str(record[3])+","+str(record[4])+","+str(record[0])+",0,0,1,0)")
                            myc5.execute("update Botte set tempsetBotte="+str(valore)+" where idBotte="+str(cod[2]))
                            mydb5.commit()
                        else:
                            mydb5=mys.connect(host="localhost", user="vignaiolo", passwd="vigna38", database="Cantina") #credenziali mysql
                            myc5=mydb5.cursor()
                            myc5.execute("select idLocale,tempLocale,tempsetLocale from Locale where idLocale="+str(cod[1]))
                            record=myc5.fetchone()
                            myc5.execute("insert into StoricoLocale(dataAggL,tempAggL,tempsetAggL,idLocale,flagTemperatura,flagTemperaturaSet)values(now(),"+str(record[1])+","+str(record[2])+","+str(record[0])+",0,1)")
                            myc5.execute("update Locale set tempsetLocale="+str(valore)+" where idLocale="+str(cod[1]))
                            mydb5.commit()
                        #conferma=Thread(target=self.confFunc, args=[valore], daemon=True)
                        #conferma.start()
                        connClient.send("temperatura aggiornata".encode())
                    except BrokenPipeError:
                        mydb5.close()
                    except Exception as e:
                        print(e)
                        mydb5.rollback()
                        connClient.send("errore aggiornamento".encode())
                        mydb5.close()
                elif int(cod[2])==6:    #grafico monitoraggio temperature
                    misure=""
                    quando=""
                    dati=""
                    cod=str(cod[3]).split(" ")
                    try:
                        if cod[0]=="Vaso":
                            mydb6=mys.connect(host="localhost", user="vignaiolo", passwd="vigna38", database="Cantina") #credenziali mysql
                            myc6=mydb6.cursor()
                            myc6.execute("select tempAggB from StoricoBotte where idBotte="+str(cod[2])+" order by dataAggB desc limit 10")
                            recordTemp=myc6.fetchall()
                            myc6.execute("select dataAggB from StoricoBotte where idBotte="+str(cod[2])+" order by dataAggB desc limit 10")
                            recordDate=myc6.fetchall()
                        else:
                            mydb6=mys.connect(host="localhost", user="vignaiolo", passwd="vigna38", database="Cantina") #credenziali mysql
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
                    misure=""
                    quando=""
                    dati=""
                    c=0
                    cod=str(cod[3]).split(" ")
                    try:
                        mydb7=mys.connect(host="localhost", user="vignaiolo", passwd="vigna38", database="Cantina") #credenziali mysql
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
                    cod=str(cod[3]).split(" ")
                    try:
                        mydb8=mys.connect(host="localhost", user="vignaiolo", passwd="vigna38", database="Cantina") #credenziali mysql
                        myc8=mydb8.cursor()
                        if cod[0]=="Vaso":
                            myc8.execute("select statoV, funzV from Sonda,Botte where Sonda.idSondaV=Botte.idSondaV and Sonda.idBotte="+str(cod[2]))
                        else:
                            myc8.execute("select statoV, funzV from Sonda,Locale where Sonda.idSondaV=Locale.idSondaV and Sonda.idLocale="+str(cod[1]))
                        record=myc8.fetchone()
                        if record[0]==0 and record[1]==0 or record[1]==2:
                            connClient.send("disinserita".encode())
                        elif record[0]==0 and record[1]==1 or record[1]==3:
                            connClient.send("avaria".encode())
                        elif record[0]==1 and record[1]==0 or record[1]==0:
                            connClient.send("off".encode())
                        elif record[0]==1 and record[1]==1 or record[1]==1:
                            connClient.send("on".encode())
                    except BrokenPipeError:
                        mydb8.close()
                    except Exception as e:
                        print(e)
                        connClient.send("*****".encode())
                        mydb8.close()
                labelAgg=Thread(target=self.scrolling_signal.emit, args=[arrDati], daemon=True)
                labelAgg.start()
                stato=1
            except:
                stato=2
                pass
    
    @QtCore.pyqtSlot(list)
    def aggScroll(self, cod):
        #print(cod) #debug
        try:
            import datetime
            ora=datetime.datetime.now()
            istr=ora.strftime("%d/%m/%y")+" "+ora.strftime("%H:%M:%S")+" > "    #costruisco la stringa da appendere
            for el in cod:
                istr += " | "+str(el)
            label = QtWidgets.QLabel(istr)
            self.scrollContent.layout().addWidget(label)
        except Exception as e:
            print(e)
            pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_ServerGUI()
    sys.exit(app.exec_())
