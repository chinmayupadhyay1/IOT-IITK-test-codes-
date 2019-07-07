#include<ESP8266WiFi.h>
#include<PubSubClient.h>
const char* ssid="SmartCity";
const char* password="69366938";
const char* mqttServer="192,168.1.41";
const int mqttPort= 8080;
const char* mqttUser="";
const char* mqttPassword="";

WiFiClient espClient;
PubSubClient client(espclient);

void setup() {
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

 client.setServer(mqttServer, mqttPort);
}

void loop() {
  // put your main code here, to run repeatedly:

}
