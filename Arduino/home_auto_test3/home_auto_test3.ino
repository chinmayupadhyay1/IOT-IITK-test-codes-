#include<ESP8266WiFi.h>
#include <WiFiUdp.h> 
WiFiUDP Udp;
 
const char* ssid="SmartCity";
const char* password="69366938";
//int led=13;
int button = 12;
//int ledState =LOW;
int buttonCurrent;
int buttonPrevious = LOW; 
int port = 8080;

void setup() {
  pinMode(button, INPUT);
//pinMode(led,OUTPUT);
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
  Udp.beginPacket("192.168.1.49",port); 
  }
void loop()
  {
  buttonCurrent = digitalRead(button);
  if (buttonCurrent == HIGH && buttonPrevious == LOW)
  {
  //if (ledState == HIGH)
  //{
  //ledState = LOW;
    Udp.write("HIGH");
    Udp.endPacket(); 
  }
  else
  {
 //ledState = HIGH;
   Udp.write("LOW");
   Udp.endPacket(); 
  }
 }
// digitalWrite(led, ledState);
// buttonPrevious = buttonCurrent;
// }
    
