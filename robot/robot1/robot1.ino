#include <AFMotor.h>
 
AF_DCMotor motor4(4);
AF_DCMotor motor2(2);
AF_DCMotor motor3(3);
AF_DCMotor motor1(1);

unsigned long distance; 

int TRIG = A1;
int ECHO = A0;

bool autopilot_on;
 
void setup() {
  Serial.begin(9600);           // set up Serial library at 9600 bps
  Serial.println("Motor test!");
  
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
}
 
void loop() {
  if (autopilot_on) {
    distance = getDistance();
    if (distance < 15) {
      turn_right(200);
    } else {
      forward(200);
    }
    delay(200);
    stop();
  }
}

void turn_left(uint8_t speed) {   // turn left

  motor4.run(FORWARD);
  motor2.run(FORWARD); 
  motor3.run(BACKWARD);
  motor1.run(BACKWARD);
  motor4.setSpeed(speed);
  motor2.setSpeed(speed);
  motor3.setSpeed(speed);
  motor1.setSpeed(speed);
}

void turn_right(uint8_t speed) {
  motor4.run(BACKWARD);
  motor2.run(BACKWARD);
  motor3.run(FORWARD);
  motor1.run(FORWARD);
  motor4.setSpeed(speed);
  motor2.setSpeed(speed);
  motor3.setSpeed(speed);
  motor1.setSpeed(speed);
}

  
  void forward(uint8_t speed) {  

  motor4.run(FORWARD);
  motor2.run(FORWARD); 
  motor3.run(FORWARD);
  motor1.run(FORWARD);
  motor4.setSpeed(speed);
  motor2.setSpeed(speed);
  motor3.setSpeed(speed);
  motor1.setSpeed(speed);
}
 
   void backward(uint8_t speed) {  

  motor4.run(BACKWARD);
  motor2.run(BACKWARD); 
  motor3.run(BACKWARD);
  motor1.run(BACKWARD);
  motor4.setSpeed(speed);
  motor2.setSpeed(speed);
  motor3.setSpeed(speed);
  motor1.setSpeed(speed);
}
  

void stop() {
  motor4.run(RELEASE);
  motor2.run(RELEASE);
  motor3.run(RELEASE);
  motor1.run(RELEASE);
}
  

void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    if (inChar == 'F') {
      forward(200);
    }else if (inChar == 'B') {
      backward(200);
    }else if (inChar == 'R') {
      turn_right(200);
    } else if (inChar == 'L') {
      turn_left(200);
    } else if (inChar == 'S') {
      stop();
    } else if (inChar == 'X') {
      autopilot_on = true;
    } else if (inChar == 'x') {
      autopilot_on = false;
    };
  };
}

unsigned long getDistance() {
  unsigned long duration;
  unsigned long distance; 
  digitalWrite(TRIG, HIGH);
  delay(10);
  digitalWrite(TRIG, LOW);
  duration = pulseIn(ECHO, HIGH);
  distance = duration / 58;
  return distance; 
}

