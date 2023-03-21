#include <Servo.h>

Servo s1;
Servo s2;
Servo s3;

int x = A0;
int y = A1;
int b = 8;

void setup() {
  Serial.begin(9600);
  pinMode(x, INPUT);
  pinMode(y,INPUT);
  pinMode(b,INPUT);
  digitalWrite(b,HIGH);
  s1.attach(10);
  s2.attach(9);
  s3.attach(11);
}

void loop() {
  int xVal = analogRead(x);
  int yVal = analogRead(y);
  int bVal = digitalRead(b);
  Serial.println(bVal);

  int sX = map(xVal, 0, 1023, 0, 180);
  int sY = map(yVal, 0, 1023, 0, 180);
 

  s1.write(sX);
  s2.write(sY);
  if(bVal == 0){
    s3.write(180);
  }
  else s3.write(90);


  delay(10);
}