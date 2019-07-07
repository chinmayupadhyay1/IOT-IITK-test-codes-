int val=0;
void setup() {
  Serial.begin(9600);
  // put your setup code here, to run once:

}

void loop() {
  val = analogRead(A0);
  Serial.println(val);
  delay(500);// put your main code here, to run repeatedly:

}
