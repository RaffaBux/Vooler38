#print ("({})<====3")
import socket
import mysql.connector as mys
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 8080)) #indirizzo macchina
s.listen(10)
while True:
    try:
        connClient, ipClient = s.accept()
        cred=connClient.recv(1024).decode() #0 username, 1 password, 2 codIstruzione, 3&&+ info aggiuntive
        cod=cred.split(",")
        if int(cod[2])==0:
            print(cod)
            try:
                mydb0=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Login")  #credenziali mysql
                myc0=mydb0.cursor()
                myc0.execute("select * from Utenze where user='"+str(cod[0])+"' and passwd='"+str(cod[1])+"'")
                myc0.fetchall()
                nrows=myc0.rowcount
                if nrows==1:
                    connClient.send("accesso_corretto".encode())
                else:
                    connClient.send("credenziali_errate".encode())
                mydb0.close()
            except:
                connClient.send("errore_connessione".encode())
                mydb0.close()
        elif int(cod[2])==1:
            print(cod)
            try:
                mydb1=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Esterno")   #dopo da sostituire con le credenziali
                myc1=mydb1.cursor()
                myc1.execute("select tempEsterno from Esterno where idEsterno=1")
                record=myc1.fetchone()
                connClient.send(str(record[0]).encode())
            except BrokenPipeError:
                mydb1.close()
            except:
                connClient.send("---".encode())
                mydb1.close()
        elif int(cod[2])==2:
            print(cod)
            cod=str(cod[3]).split(" ")
            try:
                mydb2=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Cantina")
                myc2=mydb2.cursor()
                if cod[0]=="Vaso":
                    myc2.execute("select tempBotte from Botte where idBotte="+str(cod[3]))
                    record=myc2.fetchone()
                    connClient.send(str(record[0]).encode())
                else:
                    myc2.execute("select tempLocale from Locale where idEsterno="+str(cod[2]))
                    record=myc2.fetchone()
                    connClient.send(str(record[0]).encode())
            except BrokenPipeError:
                mydb2.close()
            except:
                connClient.send("*****".encode())
                mydb2.close() 
    except KeyboardInterrupt:
        s.close()
        print("server chiuso")
        break
    except:
        pass