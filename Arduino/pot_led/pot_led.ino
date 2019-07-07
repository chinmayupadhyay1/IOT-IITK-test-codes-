int led = 11;
int pot = 0;
void setup() {
  pinMode(led, OUTPUT); // put your setup code here, to run once:

}

void loop() {
  int val = analogRead(pot);
  val = map(val, 1, 1024, 1, 255);
  analogWrite(led, val);
  
  // put your main code here, to run repeatedly:

}
