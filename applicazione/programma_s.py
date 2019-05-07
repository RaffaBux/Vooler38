#print ("({})<====3")
import socket
import mysql.connector as mys
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 9090)) #indirizzo macchina
s.listen(10)
while True:
    try:
        connClient, ipClient = s.accept()
        cred=connClient.recv(1024).decode() #0 username, 1 password, 2 codIstruzione, 3&&+ info aggiuntive
        cod=cred.split(",")
        if int(cod[2])==0:  #login
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
                connClient.send("errore_connessione".encode())
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
        elif int(cod[2])==2:    #temperature botti e locali
            print(cod)
            cod=str(cod[3]).split(" ")
            try:
                mydb2=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Cantina") #credenziali mysql
                myc2=mydb2.cursor()
                if cod[0]=="Vaso":
                    myc2.execute("select tempBotte from Botte where idBotte="+str(cod[2]))
                    record=myc2.fetchone()
                    connClient.send(str(record[0]).encode())
                else:
                    myc2.execute("select tempLocale from Locale where idLocale="+str(cod[1]))
                    record=myc2.fetchone()
                    connClient.send(str(record[0]).encode())
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
                    myc5.execute("select idBotte,contenuto,tempBotte,tempsetBotte from Botte where idBotte="+str(cod[2]))
                    record=myc5.fetchone()
                    myc5.execute("insert into StoricoBotte(dataAggB,contenutoAggB,tempAggB,tempsetAggB,idBotte)values(now(),'"+str(record[1])+"',"+str(record[2])+","+str(record[3])+","+str(record[0])+")")
                    myc5.execute("update Botte set tempsetBotte="+str(valore)+" where idBotte="+str(cod[2]))
                    mydb5.commit()
                else:
                    mydb5=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Cantina") #credenziali mysql
                    myc5=mydb5.cursor()
                    myc5.execute("select idLocale,tempLocale,tempsetLocale from Locale where idLocale="+str(cod[1]))
                    record=myc5.fetchone()
                    myc5.execute("insert into StoricoLocale(dataAggL,tempAggL,tempsetAggL,idLocale)values(now(),"+str(record[1])+","+str(record[2])+","+str(record[0])+")")
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
    except KeyboardInterrupt:
        s.close()
        print("server chiuso")
        break
    except:
        pass