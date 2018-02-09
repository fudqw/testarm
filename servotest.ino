/*************************************************** 
  This is an example for our Adafruit 16-channel PWM & Servo driver
  Servo test - this will drive 16 servos, one after the other

  Pick one up today in the adafruit shop!
  ------> http://www.adafruit.com/products/815

  These displays use I2C to communicate, 2 pins are required to  
  interface. For Arduino UNOs, thats SCL -> Analog 5, SDA -> Analog 4

  Adafruit invests time and resources providing this open source code, 
  please support Adafruit and open-source hardware by purchasing 
  products from Adafruit!

  Written by Limor Fried/Ladyada for Adafruit Industries.  
  BSD license, all text above must be included in any redistribution
 ****************************************************/

#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

// called this way, it uses the default address 0x40
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();
// you can also call it with a different address you want
//Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x41);

// Depending on your servo make, the pulse width min and max may vary, you 
// want these to be as small/large as possible without hitting the hard stop
// for max range. You'll have to tweak them as necessary to match the servos you
// have!
#define SERVOMIN  130 // this is the 'minimum' pulse length count (out of 4096)
#define SERVOMAX  650 // this is the 'maximum' pulse length count (out of 4096)

// our servo # counter
uint8_t servonum = 0;
 int ca=300;
 int j1=450;
 int j2=310;
 int j3=450;
 int j4=450;
 int j5=600;
 int j6=370;
 int j7=470;
 int j1t=j1;
 int j2t=j2;
 int j3t=j3;
 int j4t=j4;
 int j5t=j5;
 int j6t=j6;
 int j7t=j7;
  int j14=610;
   int j15=480;
   int sp=1;
 String jnum;
String readString;
void setup() {
  Serial.begin(9600);
  Serial.println("16 channel Servo test!");

  pwm.begin();
  
  pwm.setPWMFreq(60);  // Analog servos run at ~60 Hz updates

  yield();
}

// you can use this function if you'd like to set the pulse length in seconds
// e.g. setServoPulse(0, 0.001) is a ~1 millisecond pulse width. its not precise!
void setServoPulse(uint8_t n, double pulse) {
  double pulselength;
  
  pulselength = 1000000;   // 1,000,000 us per second
  pulselength /= 60;   // 60 Hz
  Serial.print(pulselength); Serial.println(" us per period"); 
  pulselength /= 4096;  // 12 bits of resolution
  Serial.print(pulselength); Serial.println(" us per bit"); 
  pulse *= 1000;
  pulse /= pulselength;
  Serial.println(pulse);
  pwm.setPWM(n, 0, pulse);
}

void loop() {
  // Drive each servo one at a time


  
  while (Serial.available()) {
    delay(3);  //delay to allow buffer to fill
    if (Serial.available() >0) {
      char c = Serial.read();  //gets one byte from serial buffer
      readString += c; //makes the string readString
    }
  }

  if (readString.length() >0) {
      Serial.print("pulse"); //see what was received
      //Serial.println(readString); 

      jnum=readString.substring(0,3);
      if (jnum=="j01")
      {
        j1t = readString.substring(3,6).toInt();
        Serial.println("j1");
        Serial.println(j1); 
       }
      else if (jnum=="j02")
      {
        j2t = readString.substring(3,6).toInt();
         Serial.println("j2");
        Serial.println(j2);
      }
      else if (jnum=="j03")
      {
        j3t = readString.substring(3,6).toInt();
        Serial.println(j3);
      }
      else if (jnum=="j04")
      {
        j4t = readString.substring(3,6).toInt();
        Serial.println(j4);
      }
      else if (jnum=="j05")
      {
        j5t = readString.substring(3,6).toInt();
        Serial.println(j5);
      }
      else if (jnum=="j06")
      {
        j6t  = readString.substring(3,6).toInt();
        Serial.println(j6);
      }
      else if (jnum=="j07")
      {
        j7t  = readString.substring(3,6).toInt();
        Serial.println(j7);
      }
      else if (jnum=="j14")
      {
        j14 = readString.substring(3,6).toInt();
        Serial.println(j14);
      }
      else if (jnum=="j15")
      {
        j15  = readString.substring(3,6).toInt();
        Serial.println(j15);
      }
      else if (jnum=="spd")
      {
        sp  = readString.substring(3,6).toInt();
        Serial.println(sp);
      }
      else{}
      delay(1);
                
       
    readString="";
  }

  if (j1<j1t)
                {j1=j1+sp;}
                else if (j1>j1t)
                {j1=j1-sp;}
                
                if (j2<j2t)
                {j2=j2+sp;}
                else if (j2>j2t)
                {j2=j2-sp;}
                
                if (j3<j3t)
                {j3=j3+sp;}
                else if (j3>j3t)
                {j3=j3-sp;}
                
                if (j4<j4t)
                {j4=j4+sp;}
                else if (j4>j4t)
                {j4=j4-sp;}
                
                if (j5<j5t)
                {j5=j5+sp;}
                else if (j5>j5t)
                {j5=j5-sp;}
                
                if (j6<j6t)
                {j6=j6+sp;}
                else if (j6>j6t)
                {j6=j6-sp;}
                
                if (j7<j7t)
                {j7=j7+sp;}
                else if (j7>j7t)
                {j7=j7-sp;}
                
                 
                  pwm.setPWM(0, 0, j1);
                  pwm.setPWM(1, 0, j2);
                  pwm.setPWM(2, 0, j3);
                  pwm.setPWM(3, 0, j4);
                  pwm.setPWM(4, 0, j5);
                  pwm.setPWM(5, 0, j6);
                  pwm.setPWM(6, 0, j7);
                  pwm.setPWM(14, 0, j14);
                  pwm.setPWM(15, 0, j15);
                delay(1);
              
                servonum ++;
                if (servonum > 0) servonum = 0;
  
  /*else
  {
    Serial.print("servo");
     Serial.println(servonum);
                for (uint16_t pulselen = SERVOMIN; pulselen < SERVOMAX; pulselen++) {
                  pwm.setPWM(servonum, 0, ca);
                }
              
                delay(30);
                for (uint16_t pulselen = SERVOMAX; pulselen > SERVOMIN; pulselen--) {
                  pwm.setPWM(servonum, 0, ca);
                }
              
                delay(30);
              
                servonum ++;
                if (servonum > 6) servonum = 0;
    }
*/

  

 
}
