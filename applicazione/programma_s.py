#print ("({})<====3")
import socket
import mysql.connector as mys
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)                                         #server applicazione 
s.bind(("localhost", 8080))
s.listen(5)
while True:
    try:
        conn_c, indrz = s.accept()
        cred=conn_c.recv(1024).decode()                                                             #lista con [0] username 
        log=cred.split(",")
        print(log)
        if int(log[2])==0:
            try:                                                                                        #e [1] password
                mydb0=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Login")   #dopo da sostituire con le credenziali
                myc0=mydb0.cursor()                                                                                  #login
                myc0.execute("select * from Utenze where user='"+str(log[0])+"' and passwd='"+str(log[1])+"'")
                myc0.fetchall()
                number=myc0.rowcount
                if number==1:
                    string="accesso_corretto"
                    conn_c.send(string.encode())
                    mydb0.close()
                else:
                    conn_c.send("credenziali_errate".encode())
                    mydb0.close()
            except:
                conn_c.send("errore_connessione".encode())
                mydb0.close()
        elif int(log[2])==1:
            import time
            while True:
                try:
                    mydb1=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Esterno")   #dopo da sostituire con le credenziali
                    myc1=mydb1.cursor()
                    while True:
                        myc1.execute("select tempEsterno from Esterno where idEsterno=1")
                        record=myc1.fetchone()
                        conn_c.send(str(record[0]).encode())
                        time.sleep(35)
                except BrokenPipeError:
                    mydb1.close()
                    break
                except:
                    conn_c.send("*****".encode())
        elif int(log[2])==2:
            import time
            determ=str(log[3])
            determ=determ.split(" ")
            while True:
                try:
                    mydb2=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Cantina")   #dopo da sostituire con le credenziali
                    myc2=mydb2.cursor()
                    while True:
                        if determ[0]=="'Vaso":
                            "".join(list(determ[2]).remove('\''))
                            myc2.execute("select tempBotte from Botte where idBotte="+determ)
                            record=myc2.fetchone()
                            conn_c.send(str(record[0]).encode())
                        else:
                            "".join(list(determ[1]).remove('\''))
                            myc2.execute("select tempLocale from Locale where idEsterno="+determ)
                            record=myc2.fetchone()
                            conn_c.send(str(record[0]).encode())
                        time.sleep(35)
                except BrokenPipeError:
                    mydb2.close()
                    break
                except:
                    conn_c.send("*****".encode())
    
    except KeyboardInterrupt:
        s.close()
        print("server chiuso")
        break