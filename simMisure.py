#!/usr/bin/python
# coding=utf-8
 
# Needed modules will be imported
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import mysql.connector as mys
from random import randint
 
# The break of 2 seconds will be configured here
sleeptime = 1
 
# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
DHTSensor = Adafruit_DHT.DHT11
 
# The pin which is connected with the sensor will be declared here
GPIO_Pin = 23
 
print('KY-015 sensortest - temperature and humidity')
 
try:
    while(1):
        # Measurement will be started and the result will be written into the variables
        humid, temper = Adafruit_DHT.read_retry(DHTSensor, GPIO_Pin)
 
        print("-----------------------------------------------------------------")
        if humid is not None and temper is not None:
 
            # The result will be shown at the console
            x=randint(1,33)
            if x>3:
                print('VV'+str(x)+': temperature = {0:0.1f}°C  | rel. humidity = {1:0.1f}%'.format(temper, humid))
                mydb5=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Cantina") #credenziali mysql
                myc5=mydb5.cursor()
                myc5.execute("select idBotte,contenuto,tempBotte,tempsetBotte from Botte where idBotte="+str(x))
                record=myc5.fetchone()
                myc5.execute("insert into StoricoBotte(dataAggB,contenutoAggB,tempAggB,tempsetAggB,idBotte)values(now(),'"+str(record[1])+"',"+str(record[2])+","+str(record[3])+","+str(record[0])+")")
                myc5.execute("update Botte set tempBotte="+str(temper)+" where idBotte="+str(x))
                mydb5.commit()
            else:
                print('L'+str(x)+': temperature = {0:0.1f}°C  | rel. humidity = {1:0.1f}%'.format(temper, humid))
                mydb5=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Cantina") #credenziali mysql
                myc5=mydb5.cursor()
                myc5.execute("select idLocale,tempLocale,tempsetLocale from Locale where idLocale="+str(x))
                record=myc5.fetchone()
                myc5.execute("insert into StoricoLocale(dataAggL,tempAggL,tempsetAggL,idLocale)values(now(),"+str(record[1])+","+str(record[2])+","+str(record[0])+")")
                myc5.execute("update Locale set tempLocale="+str(temper)+" where idLocale="+str(x))
                mydb5.commit()
            mydb5.close()
         
        # Because of the linux OS, the Raspberry Pi has problems with realtime measurements.
        # It is possible that, because of timing problems, the communication fails.
        # In that case, an error message will be displayed - the result should be shown at the next try.
        else:
            print('Error while reading - please wait for the next try!')
        print("-----------------------------------------------------------------")
        print("")
        time.sleep(sleeptime)
 
# Scavenging work after the end of the program
except KeyboardInterrupt:
    GPIO.cleanup()