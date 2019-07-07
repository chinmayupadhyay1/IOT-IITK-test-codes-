 void setup() {
 pinMode(13,OUTPUT);
 digitalWrite(13,LOW);
 Serial.begin(9600);// put your setup code here, to run once:

}

void loop() 
{
  if (Serial.available()>0)
  { 
    //Serial.println(Serial.read());
    if (Serial.read() == 97)
    {
      Serial.print("yes");
     digitalWrite(13,HIGH);
    }
    else
    {
     digitalWrite(13,LOW);
    }
  }
 }
