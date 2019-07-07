#include<ESP8266WiFi.h>
#include <WiFiUdp.h>

WiFiUDP Udp;

const char* ssid="SmartCity";
const char* password="69366938";
int remort_port = 5002;
int local_port = 5003;

char packetBuffer[UDP_TX_PACKET_MAX_SIZE + 1];
char  ReplyBuffer[] = "acknowledged\r\n";     

void setup() 
{
Serial.begin(115200);  
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
 
//Udp.beginPacket("192.168.1.41",remort_port);

Udp.begin(local_port);
}

void loop() 
{
  int packetSize = Udp.parsePacket();
  if (packetSize) 
  {
//    Serial.printf("Received packet of size %d from %s:%d\n    (to %s:%d, free heap = %d B)\n",
//                  packetSize,
//                  Udp.remoteIP().toString().c_str(), Udp.remotePort(),
//                  Udp.destinationIP().toString().c_str(), Udp.localPort(),
//                  ESP.getFreeHeap());

    int n = Udp.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE);
    packetBuffer[n] = 0;
    Serial.println("Contents:");
    Serial.println(packetBuffer);
    Udp.endPacket();

  }
}