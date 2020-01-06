#include <Servo.h> 
#include "HX711.h"

#define calibration_factor -2700.0 // load cell, kalibroidaan erikseen
HX711 scale;
#define DOUT  13
#define CLK  12

int servoPin = 2;
int valve_pin = 3;
int eTape = 0 ;

char python = 'n' ; // n = älä keitä, y = keitä
int kupit = 6 ;
int vaihe = 1 ; // prosessin senhetkinen vaihe [1,n]


Servo Servo1;


void setup() {
  // put your setup code here, to run once:
   Serial.begin(9600) ;
   Servo1.attach(servoPin);
   Servo1.write(40) ;

   scale.begin(DOUT, CLK);
   scale.set_scale(calibration_factor);
}

void loop() {
  // put your main code here, to run repeatedly:
    if(python == 'n'){
    if(Serial.available() > 0) {
    char data = Serial.read();
      python = data;

      kupit = (int) python ;

      
    }
  }
  if(python != 'n'){
  pinMode(valve_pin, OUTPUT);
   
  // vaihe 1: veden mittaus
  while(vaihe == 1){

    int korkeus = 1000 ; // alustus
    int tavoite_vesi = 925- 1.5*kupit ; // 

    // 0 = 925
    // 6 = 917
    // 9 = 904

    digitalWrite(valve_pin,HIGH); // venttiili auki

    //Serial.println("venttiili auki"); // testi

    while(korkeus > tavoite_vesi){
       eTape = analogRead(A0);

       //Serial.println(eTape) ; //testi
       
       korkeus = eTape ; // kalibroi ja muokkaa!!
       
       delay(300) ; 
    }
  

    digitalWrite(valve_pin,LOW) ; //venttiili kiinni

    //Serial.println("venttiili kiinni") ; // testi

    vaihe = 2 ; // ulos loopista ja seuraavaan vaiheeseen
    

    
  }
 // vaihe 2: purujen mittaus
 
 while(vaihe == 2){

   scale.tare(); // nollaus

   //Servo1.attach(servoPin);

   Servo1.write(100) ; // luukku auki, kalibroitava

   float tavoite_purut = kupit * 7.0; //

   float massa = scale.get_units() ;

   while(massa < tavoite_purut){
   massa = scale.get_units();
   delay(50) ;

   //Serial.println(massa) ; // testi
    //int kesto = 500*kupit ;//häpeallinen ratkaisu
   // delay(kesto) ;
  }
   Servo1.write(40) ;
   delay(300); // odotetaan servoa
   vaihe = 3;
   //Servo1.detach();
 }
 // vaihe 3: keitin päälle, kehityksessä
 while(vaihe == 3){

   if(Serial.available() > 0) {
      char data = Serial.read();
    if(data == 'n'){
    python = data;
    vaihe = 1;
    }
   }

    
  
 }

  
  } 
}
