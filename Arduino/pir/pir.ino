int pirsensor = 2;
int LED = 13;
int sensorValue = 0;
int pirstate = LOW;
void setup() {
  // put your setup code here, to run once:
  pinMode(pirsensor, INPUT);
  pinMode(LED, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int Value = digitalRead(pirsensor);
  if (sensorValue == HIGH) {
    digitalWrite(LED, HIGH);
  }else{
    digitalWrite(LED, LOW);
  }
}
