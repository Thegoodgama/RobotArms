#include <Servo.h>
Servo sx;
Servo sy;
Servo sz;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  sx.attach(10); 
  sy.attach(9);
  sz.attach(11);

}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() >=3){
    int data[3];

    for (int i = 0; i < 3; i++){
      data[i] = Serial.read();
    }

    sx.write(data[0]);
    sy.write(data[1]);
    if(data[2] == 1){
      sz.write(90);
    }
    else if (data[2]==0){
      sz.write(180);
    }
  }

}
