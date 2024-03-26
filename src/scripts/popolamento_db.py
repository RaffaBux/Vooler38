import mysql.connector as mys
from random import randint
'''c=0
mydb7=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Cantina")
myc7=mydb7.cursor()
while c<1500:
    try:
        x=randint(4,33)
        myc7.execute("select idBotte, contenuto, tempBotte, tempsetBotte, volume from Botte where idBotte="+str(x))
        record=myc7.fetchone()
        myc7.execute("insert into StoricoBotte(idBotte,dataAggB,contenutoAggB,tempAggB,tempsetAggB,volumeAggB,flagVolume,flagContenuto,flagTemperatura)values("+str(record[0])+",now(),'"+str(record[1])+"',"+str(record[2])+","+str(record[3])+","+str(record[4])+",0,0,1)")
        temp=randint(0,100)
        myc7.execute("update Botte set tempBotte="+str(temp)+" where idBotte="+str(x))
        mydb7.commit()
        print(c)
        c+=1
    except Exception as b:
        print(b)
    except Exception as e:
        mydb7.rollback()
        print(e)
mydb7.close()
print("concluso")'''

c=4
mydb7=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Cantina")
myc7=mydb7.cursor()
while c<34:
    try:
        xa=randint(0,1)
        xb=randint(0,1)
        xc=randint(0,1)
        myc7.execute("insert into Sonda(idSondaV,statoS,statoV,funzV,idBotte)values("+str(c)+","+str(xa)+","+str(xb)+","+str(xc)+","+str(c)+")")
        mydb7.commit()
        print(c)
        c+=1
    except Exception as b:
        print(b)
    except Exception as e:
        mydb7.rollback()
        print(e)
mydb7.close()
print("concluso")