#include<ESP8266WiFi.h>
#include <WiFiUdp.h> 
WiFiUDP Udp;
 
const char* ssid="SmartCity";
const char* password="69366938";
int port = 8080;
int button = 12;
char packetBuffer[UDP_TX_PACKET_MAX_SIZE]
void setup() 
{
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
  int packetSize = Udp.parsePacket();
  if(packetSize)  
 {
  Serial.print("Received packet of size ");
  Udp.read(packetBuffer,UDP_TX_PACKET_MAX_SIZE);
  Serial.println("Contents:");
  Serial.println(packetBuffer);
  if (packetBuffer == "HIGH")
  {
    digitalWrite(LED,HIGH);
  }
  else if (packebuffer == "LOW")
  {
    digitalWrite(LED,LOW);
  }
  }
}
