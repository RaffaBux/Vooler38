import mysql.connector as mys
from random import randint
c=0
mydb7=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Cantina")
myc7=mydb7.cursor()
while c<1000:
    try:
        x=randint(4,33)
        myc7.execute("select idBotte, contenuto, tempBotte, tempsetBotte, volume from Botte where idBotte="+str(x))
        record=myc7.fetchone()
        myc7.execute("insert into StoricoBotte(idBotte,dataAggB,contenutoAggB,tempAggB,tempsetAggB,volumeAggB,flagVolume)values("+str(record[0])+",now(),"+str(record[1])+","+str(record[2])+","+str(record[3])+","+str(record[4])+",1)")
        mydb7.commit()
        litri=randint(0,1000)
        myc7.execute("update Botte set volume="+str(litri)+" where idBotte="+str(x))
        mydb7.commit()
        print(c)
        c+=1
    except Exception as e:
        mydb7.rollback()
        print(e)
mydb7.close()
print("concluso")