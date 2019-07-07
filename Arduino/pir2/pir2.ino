int pirSensor = 8;
int LED = 7;

void setup() {
  pinMode (pirSensor, INPUT);
  pinMode (LED, OUTPUT);// put your setup code here, to run once:

}

void loop() {
  int sensorValue = digitalRead(pirSensor);
  if (sensorValue == 1) {
    digitalWrite(LED , HIGH);
  }
  else 
    digitalWrite(LED , LOW); 
  // put your main code here, to run repeatedly:

}
