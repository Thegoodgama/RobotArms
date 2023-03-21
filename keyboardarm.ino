#include <Servo.h>


Servo sx;
Servo sy;
Servo sb;
int px = 90;
int py = 90;

void setup() {
  Serial.begin(9600);
  sx.attach(10);
  sy.attach(9);
  sb.attach(11);


}

void loop() {
  if(px > 180) px = 180;
  else if(px < 0) px = 0;
  if(py > 180) py = 180;
  else if(py < 0) py = 0;
  
  sx.write(px);
  sy.write(py);
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    if (command == "up") {
      py -=10;
      
    } 
    else if (command == "down") {
      py +=10;
      
    } 
    else if (command == "left") {
      px -=10;
      
    } 
    else if (command == "right") {
      px+=10;
   
    }
    else if(command == "open"){
      sb.write(90);
    }
    else if (command == "close"){
      sb.write(180);
    }
  }
}