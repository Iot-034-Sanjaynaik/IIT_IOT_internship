#define LED_PIN 2

void setup() {
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_PIN, HIGH); // ON
  delay(1000);                 // 1 second
  digitalWrite(LED_PIN, LOW);  // OFF
  delay(1000);                 // 1 second
}