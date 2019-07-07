#include<ESP8266WiFi.h>
#include <WiFiUdp.h>

WiFiUDP Udp;

const char* ssid="SmartCity";
const char* password="69366938";

int port = 8080;

void setup() 
{
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
}

void loop() 
{
  Udp.beginPacket("192.168.1.41",port);
  Udp.write("hello");
  Udp.endPacket();   
  delay(2000);
}
