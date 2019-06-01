from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ServerGUI(QtWidgets.QMainWindow):

    scrolling_signal = QtCore.pyqtSignal([list]) ### debug

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
        ### I've cut some things
        # self.gridLayout_2.addWidget(self.label19, 20, 0, 1, 1)
        # listaLabel.append(self.label19)
        self.scrollArea.setWidget(self.scrollContent)
        self.verticalLayout.addWidget(self.scrollArea)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        Server.setCentralWidget(self.centralwidget)
        self.retranslateUi(Server)
        QtCore.QMetaObject.connectSlotsByName(Server)
        self.scrolling_signal.connect(self.aggScroll) ### debug

        be=Thread(target=self.backend, args=[lambda: threadMainPace, listaLabel], daemon=True) ###debug
        be.start()

    def retranslateUi(self, Server):
        _translate = QtCore.QCoreApplication.translate
        Server.setWindowTitle(_translate("Server", "Server"))
        self.statoServerLabel.setText(_translate("Server", "Stato server:"))
        self.statoLabel.setText(_translate("Server", "***"))
        self.imgLabel.setText(_translate("Server", "<html><head/><body><p><img src=\"gray.png\"/></p></body></html>"))

    def backend(self, exit, listaLabel):
        from threading import Thread
        import socket
        import mysql.connector as mys
        global ind
        ind=1
        global listaDati
        listaDati=[]
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("127.0.0.1", 8282)) #indirizzo macchina
        s.listen(10)
        while exit():
            try:
                connClient, ipClient = s.accept()
                cred=connClient.recv(1024).decode() #0 username, 1 password, 2 codIstruzione, 3&&+ info aggiuntive
                cod=cred.split(",")
                arrDati=cod
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

                elif(int(cod[2]==9)): ### debug purposes
                    print(cod)
                    print("This is just a test for Raffa")
                """ DEBUG """
                # aggLabel=Thread(target=self.aggScroll, args=[listaDati, listaLabel, arrDati])
                # aggLabel.start()
                #self.aggScroll(listaDati, listaLabel, arrDati)
                self.scrolling_signal.emit([listaLabel, cod]) ### debug
            except KeyboardInterrupt:
                s.close()
                print("server chiuso")
                break
            except Exception as e:
                print(e) ### debug
                pass
    @QtCore.pyqtSlot(list)
    def aggScroll(self, arguments):
        listaLabel, cod = arguments
        print(cod)
        try:
            global ind
            import datetime
            ora=datetime.datetime.now()
            if ind==3:
                listaDati.pop(0)
                ind-=1
            istr=ora.strftime("%d-%m-%y")+" "+ora.strftime("%H-%M-%S")+" > "    #costruisco la stringa da appendere
            for el in cod:
                istr += " | "+str(el)
            """ DEBUG purpuses"""
            # listaDati.append(istr)                                                #appendo la stringa
            # QtWidgets.QLabel(self.scrollContent)
            # for c in range(len(listaDati)):                                     #setto testo nelle label
            #     listaLabel[c].setText(listaDati[c])
            # ind+=1
            # listaLabel.append(QtWidgets.QLabel(self.scrollContent)) ### debug
            # listaLabel[len(listaLabel)-1].setText(istr) ### debug
            label = QtWidgets.QLabel(istr)
            #self.scrollContent.layout().insertWidget(self.scrollContent.layout().count(), label)
            self.scrollContent.layout().addWidget(label)
        except Exception as e:
            print(e)   ### debug
            pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_ServerGUI()
    sys.exit(app.exec_())
