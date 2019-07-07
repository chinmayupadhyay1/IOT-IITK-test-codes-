 void setup()
 {
 pinMode(10,OUTPUT);
 digitalWrite(10,LOW);
 Serial.begin(9600);

}

void loop() 
{
//  Serial.print(" HELLO \r\n");
//  delay(1000);  
  if (Serial.available()>0)
    {
    if (Serial.read() == 97)
    {
     digitalWrite(10,HIGH);
    }
    else
    {
     digitalWrite(10,LOW);
    }
  }
}
