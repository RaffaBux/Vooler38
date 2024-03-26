#include <SoftwareSerial.h>
using namespace std;

char nomeslv = 'm';                           // nome dello slave

SoftwareSerial Scheda1(0, 1);                 // RX,TX
int alimentazione2 = 3;                       // alimentazione 485
int pinanomalia = 13;                         // led anomalia
boolean txrx = true;                          // true = rx ; false = tx
String mex = "";
String dati = "";
String finale;                                // stringa finale con tutti i dati di valvole e sonde

void setup() {
  Serial.begin(9600);                         // initialize serial communication at 9600 bits per second
  Scheda1.begin(9600);                        // inizializza comunicazione con 485

  delay(5000);
  digitalWrite(alimentazione2, HIGH);         // inizializza trasmissione
  Scheda1.write("!");
  Scheda1.flush();
}

void loop(){
  if (txrx == false){
    digitalWrite(alimentazione2, LOW);
    String mex = "";
    if (Serial.available()){                          // se arriva messaggio da seriale lo prende
      while(Serial.available()){
        char c = (char)Serial.read();
        if (c != '/'){
           mex = mex + c;
         }
         else{
           break;
         }
      }
    }
    if(Scheda1.available() > 0){              /// se arriva messaggio da slave allora lo prende
      String dati = "";
      while(Scheda1.available()){             /// riceve un carattere alla volta
        char c = (char)Scheda1.read();
        if (c != '/'){
          dati = dati + c;
        }
        else{
          break;
        }
      }
    }
    txrx = true;
  }
  else{
    digitalWrite(alimentazione2, HIGH);
    for (int i = 0; i < dati.length(); i++){
      char c = dati.charAt(i);
      Serial.write(c);
      Serial.flush();
    }
    for (int i = 0; i < mex.length(); i++){   /// m2s
      char c = mex.charAt(i);
      Scheda1.write(c);
      Scheda1.flush();
    }
    txrx = false;
  }

  delay(5000);                                //sincronizzazione
  digitalWrite(alimentazione2, HIGH);         // inizializza trasmissione
  Scheda1.write("!");
  Scheda1.flush();
}