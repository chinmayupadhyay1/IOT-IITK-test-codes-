#include<ESP8266WiFi.h>
const char* ssid="SmartCity";
const char* password="69366938";
int led=13;

void setup() {
  pinMode(led,OUTPUT);
  digitalWrite(led,LOW);
  Serial.begin(9600);
  Serial.println();
  Serial.print("connecting to");
  Serial.println(ssid);

  WiFi.begin(ssid,password);
  Serial.print("connecting");

  while(WiFi.status()!= WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }

  Serial.println("WiFi connected");
  Serial.print("NodeMCU IP Address");
  Serial.println(WiFi.localIP());  
   
  digitalWrite(led,HIGH);
  Serial.println();

  }
void loop() {
 
  }
    
