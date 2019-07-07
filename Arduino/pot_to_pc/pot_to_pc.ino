void setup() {
  Serial.begin(9600);

}

void loop() 
{
  int val = analogRead(A0);
  val = map(val, 0, 1023, 0, 100);
  //Serial.write(val);
  Serial.println(val);
  delay(500);
}
