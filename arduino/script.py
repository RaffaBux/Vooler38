import serial

try:
    arduino = serial.Serial("/dev/ttyACM0",timeout=1)
except:
    print("Errore")

dati=str(arduino.readline())

### aggiornamento database
### invio dati al master