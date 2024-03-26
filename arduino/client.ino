#include <SoftwareSerial.h>
using namespace std;

char nomeslv = '2';                 // nome dello slave
SoftwareSerial Scheda3(0, 1);       // RX,TX
int alimentazione3 = 3;             // alimentazione 485
String valore;                      // valore di return dalla funzione getValue
int slavecercato;                   // indice 0 del messaggio
int valvolacercata;                 // indice 1 del messaggio
int temperatura;                    // variabile temperatura sonda
int pinaperto1 = 22;                // pin micro valvola1 aperta
int pinchiuso1 = 23;                // pin micro valvola1 chiusa
int statoSONDA1;                    // bit sonda inserita o disinserita
int pinstatoSONDA1 = 24;            // pin controllo presenza sonda
int pinletturaSONDA1 = A0;          // pin lettura temperatura sonda
int soglia1 = 25;                   // valore setup (soglia) temperatura sonda1
int valvola1 = 9;                   // relè valvola1
int statoVALVOLA1;                  // bit valvola inserita o disinserita
int pinstatoVALVOLA1 = 25;          // pin controllo presenza valvola
int pinanomalia = 13;               // led anomalia
int statoVALVOLAAP;                 // stato valvola aperta
int statoVALVOLACH;                 // stato valvola chiusa
boolean txrx = true;                // txrx = true -> rx
String dati;                        // stringa composta dai dati di una singola sonda/valvola

void setup() {
  Serial.begin(9600);                 // debug
  Scheda3.begin(9600);                // inizializza comunicazione con 485
  pinMode(valvola1, OUTPUT);          // dichiarazione relè 
  pinMode(pinaperto1, INPUT);
  pinMode(pinchiuso1, INPUT);
  pinMode(pinstatoSONDA1, INPUT);
  pinMode(pinanomalia,OUTPUT);

  digitalWrite(alimentazione3, LOW);  // inizializza ricezione dal 485
  Serial.println("1");
  while(true){
    char c = Scheda3.read();
    if (c == "!"){
      break;  
    }  
  }
  Serial.println("2");
}

String getValue(String dati, char separatore, int indice){              /// trova i valori alla posizione 'indice'
  int found = 0;
  int strindice[] = { 0, -1 };
  int maxindice = dati.length() - 1;
  for (int i = 0; i <= maxindice && found <= indice; i++) {
      if (dati.charAt(i) == separatore || i == maxindice) {
          found++;
          strindice[0] = strindice[1] + 1;
          strindice[1] = (i == maxindice) ? i+1 : i;
      }
  }
  return found > indice ? dati.substring(strindice[0], strindice[1]) : "";  /// restituisce il valore alla posizione richiesta
}

void loop(){
  if(txrx == true){
    Serial.println("3");
    digitalWrite(alimentazione3, LOW);                                  /// abilita ascolto al 485
    int i = 0;
    String mex = "";                                                    // dati in entrata (master to slave) -> nomeslave[0],nomevalvola[1],sogliatemperatura[2]
    boolean giusto = false;
    if(Scheda3.available() > 0){                                        /// se il master sta parlando allora lo ascolto
      while(Scheda3.available()){                                       /// riceve un carattere alla volta
        char c = (char)Scheda3.read();
        if (i = 0 && c != nomeslv){
          break;  
        }
        if (c != '/'){
          mex = mex + c;
        }
        else{
          giusto = true;
          break;
        }
        i++;
      }
      if (giusto == true){                                              /// se il primo carattere è il nome della slave allora va avanti sennò lascia perdere                                          
        valore = getValue(mex, ';', 1);                                 /// (stringa, separatore, indice del dato cercato)
        valvolacercata = valore.toInt();
        if (valvolacercata==1){
          valore = getValue(mex, ';', 2);
          soglia1 = valore.toInt();
        }
        // AGGIUNGERE EVENTUALI ALTRE VALVOLE
      }
    }
    txrx = false;
  }
  else{
    Serial.println("4");
    //--------------****DA COPIARE PER OGNI SONDA CON CORRISPONDENTE VALVOLA (CAMBIARE NUMERO)****--------------
    /// SLAVE 2 - VALVOLA E SONDA 1
  
    String finale = "";                               // stringa finale con tutti i dati di valvole e sonde
    String nomeslvS = String(nomeslv);
    dati = "m;"+nomeslvS;                             // master[0], nomeslave[1]
    statoVALVOLAAP = digitalRead(pinaperto1);         // controlla se la valvola è aperta
    statoVALVOLACH = digitalRead(pinchiuso1);         // controlla se la valvola è chiusa
    statoSONDA1 = digitalRead(pinstatoSONDA1);        // lettura stato sonda (1 collegata, 0 scollegata)
    statoVALVOLA1 = digitalRead(pinstatoVALVOLA1);    // lettura stato valvola (1 attaccata alla corrente, 0 staccata dalal corrente)
    if (statoVALVOLAAP != statoVALVOLACH && statoVALVOLA1 == 1){
      digitalWrite(pinanomalia,LOW);
      dati=dati+";1;"+statoSONDA1+";1;"+statoVALVOLA1+";"+statoVALVOLAAP;             // preparazione stringa di dati: nomesonda[2];statosonda[3];nomevalvola[4];statovalvola[5];statovalvolaaperta[6]
    }
    else{
      if (statoVALVOLAAP == statoVALVOLACH && statoVALVOLA1 == 1){
        digitalWrite(pinanomalia,HIGH);
        dati=dati+";1;"+statoSONDA1+";1;"+statoVALVOLA1+";a";                         // a[6] = avaria
      }
      else{
        dati=dati+";1;"+statoSONDA1+";1;"+statoVALVOLA1+";d";                         // d[6] = spina staccata
      }
    }
    if (statoSONDA1 == 1){
      temperatura = analogRead(pinletturaSONDA1);
      temperatura = temperatura/3.3;                                                  // taratura sonda temperatura
      dati = dati + ";" + temperatura;                                                // temperatura[7] in gradi centigradi
      if (temperatura<2 || temperatura>=40){                                          // controllo anomalia
        digitalWrite(pinanomalia,HIGH);
        dati = dati + ";" + "a";                                                      // a[8] = anomalia
      }
      else{
        dati = dati + ";" + "n";                                                      // n[8] = normale
        if (temperatura >= soglia1) {                                                 // controllo con soglia
          digitalWrite(valvola1,LOW);
        } 
        else {
          if (temperatura <= soglia1-1){                                              // ritardo sulla temperatura 
            digitalWrite(valvola1,HIGH);
          }
        } 
      }
    }
    Serial.println(dati);                                                             /// debug
    finale = finale + dati;
        
    //--------------------------------------------------------------------------------------
    /// INCOLLARE QUI SOTTO EVENTUALI ALTRE SONDE E VALVOLE, CAMBIANO IL LORO NOME CON NUMERI CRESCENTI
    /// per ogni nuova sonda e valvola aggiungere finale = finale + "_";
  
    digitalWrite(alimentazione3, HIGH);                                               // abilita trasmissione s2m
    finale = finale + "/";
    Serial.println(finale);
    for (int i = 0; i < finale.length(); i++){
      char c = finale.charAt(i);
      Scheda3.write(c);
      Scheda3.flush();
    }
    txrx = true;
  }

  digitalWrite(alimentazione3, LOW);                                                  // inizializza ricezione dal 485
  while(true){                                                                        // sincronizzazione
    char c = Scheda3.read();
    if (c == "!"){
      break;  
    }  
  }
}