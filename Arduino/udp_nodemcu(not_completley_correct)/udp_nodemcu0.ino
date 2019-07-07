#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <WiFiServer.h>

const char* ssid     = "<SmartCity>";     
const char* password = "<69366938>";    
const char* host = "103.246.106.208";  
const int   port =8080 ;           

unsigned long previousMillis = millis(); 
String data ="1234";
 WiFiClient client;
 WiFiServer server(2222);
void setup() {
  Serial.begin(9600);
  Serial.print("Connecting to ");
  Serial.println(ssid);
  
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
 
  Serial.println("");
  Serial.println("WiFi connected");  
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  client.connect(host, port);
  client.println("Hello");
}
 
void loop() {
     while(client.available()){
      char line = client.read();
      Serial.print(line);
    }
}
