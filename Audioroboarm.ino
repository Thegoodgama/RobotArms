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
  sx.write(px);
  sy.write(py);

}

void loop() {
 if(Serial.available() >=3){
    int data[3];

    for (int i = 0; i < 3; i++){
      data[i] = Serial.read();
    }

    sx.write(data[0]);
    sy.write(data[1]);
    if(data[2] == 1){
      sb.write(180);
    }
    else if (data[2]== 0 ){
      sb.write(90);
    }
  }
}

  