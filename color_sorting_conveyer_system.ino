#include <Servo.h>

Servo redServo, greenServo, blueServo, yellowServo;

void setup() {
  Serial.begin(9600);
  // redServo.attach(13);     // Connect red servo to pin 5
  // greenServo.attach(6);   // Green to pin 6
  // blueServo.attach(9);    // Blue to pin 9
  // yellowServo.attach(10); // Yellow to pin 10
  pinMode(13,OUTPUT);
}

void loop() {
  if (Serial.available()) {
    char color = Serial.read();

    if (color == 'R') {
      digitalWrite(13,HIGH);
      delay(1000);
      digitalWrite(13,LOW);
      // redServo.write(90);
      // delay(500);
      // redServo.write(0);
     } 
    // else if (color == 'G') {
    //   greenServo.write(90);
    //   delay(500);
    //   greenServo.write(0);
    // } 
    // else if (color == 'B') {
    //   blueServo.write(90);
    //   delay(500);
    //   blueServo.write(0);
    // } 
    // else if (color == 'Y') {
    //   yellowServo.write(90);
    //   delay(500);
    //   yellowServo.write(0);
    // }
  }
}
