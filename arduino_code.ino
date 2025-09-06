#include <Wire.h>

const int pressurePin = A0; 
const int motionPin = 2;

void setup() {
  Serial.begin(9600);
  pinMode(motionPin, INPUT);
}

void loop() {
  int pressureVal = analogRead(pressurePin);
  int motionVal = digitalRead(motionPin);

  Serial.print("Pressure:");
  Serial.print(pressureVal);
  Serial.print(", Motion:");
  Serial.println(motionVal);

  delay(500);
}
