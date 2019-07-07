int led = 13;
int button = 12;
int ledState =LOW;
int buttonCurrent;
int buttonPrevious = LOW; 

void setup() {
 pinMode(button, INPUT); // put your setup code here, to run once:
 pinMode(led, OUTPUT);
}

void loop() { 
  buttonCurrent = digitalRead(button);// put your main code here, to run repeatedly:
 if (buttonCurrent == HIGH && buttonPrevious == LOW )
 {
  if (ledState == HIGH)
  {
    ledState = LOW;
  }
  else
  {
    ledState = HIGH;
  }
 }
 digitalWrite(led, ledState);
 buttonPrevious = buttonCurrent;
}
