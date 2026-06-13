// GND/continuity tester
// Pin 2 = "signal probe", GND = "ground probe"
// Touch the two probes to the ends of whatever you're testing.
// If they're electrically connected (button pressed , or wires touching) it will print "working".

const int SIGNAL_PIN = 2; 

void setup() {
  Serial.begin(9600);
  pinMode(SIGNAL_PIN, INPUT_PULLUP);
}

void loop () {
  if ( digitalRead(SIGNAL_PIN) == LOW) {
    Serial.println("working");
  }
  delay(100);
}
