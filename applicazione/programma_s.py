import socket
import mysql.connector as mys
#Bussolotto Raffaele, 25/02/2019, v_1.0
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)                                         #server applicazione 
s.bind(("localhost", 8080))
s.listen(5)
while True:
    try:
        conn_c, indrz = s.accept()
        cred=conn_c.recv(1024).decode()                                                             #lista con [0] username 
        log=cred.split(",")
        print(log)
        try:                                                                                        #e [1] password
            mydb=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Login")
            myc=mydb.cursor()                                                                                  #login
            myc.execute("select * from Utenze where user='"+str(log[0])+"' and passwd='"+str(log[1])+"'")
            myc.fetchall()
            number=myc.rowcount
            if number==1:
                string="accesso_corretto"
                conn_c.send(string.encode())
                mydb.close()
            else:
                conn_c.send("credenziali_errate".encode())
                mydb.close()
        except:
            conn_c.send("errore_connessione".encode())
            mydb.close()
    except KeyboardInterrupt:
        s.close()
        print("server chiuso")
        break