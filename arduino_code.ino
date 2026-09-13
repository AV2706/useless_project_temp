/*
   THE GO-AWAY MACHINE™

   Arduino UNO R4 WiFi
   --------------------

   HC-SR04:
   VCC  -> 5V
   GND  -> GND
   TRIG -> D7
   ECHO -> D6

   Joystick:
   VCC -> 5V
   GND -> GND
   VRx -> A0
   VRy -> A1
   SW  -> D4

   Buzzer:
   + / SIG -> D9
   GND     -> GND

   Serial:
   115200 baud

   Browser commands:
   ALARM:0
   ALARM:1
   ALARM:2
   ALARM:3
   ALARM:4
   ALARM:5
   ESCAPED
   BEEP
*/


// ============================================================
// PIN DEFINITIONS
// ============================================================

const int TRIG_PIN = 7;
const int ECHO_PIN = 6;

const int BUZZER_PIN = 9;

const int JOY_X = A0;
const int JOY_Y = A1;

const int JOY_BUTTON = 4;


// ============================================================
// DISTANCE SETTINGS
// ============================================================

const int NUM_DISTANCE_READINGS = 5;

// Maximum time to wait for echo.
// 30000 microseconds ≈ 5 meters.
const unsigned long ECHO_TIMEOUT = 30000;


// ============================================================
// VARIABLES
// ============================================================

float distanceCM = 999.0;

int joystickX = 512;
int joystickY = 512;

int alarmLevel = 0;


// Timing
unsigned long lastSensorUpdate = 0;
unsigned long lastDataSend = 0;
unsigned long lastBuzzerUpdate = 0;


// ============================================================
// SETUP
// ============================================================

void setup() {

  Serial.begin(115200);

  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  pinMode(BUZZER_PIN, OUTPUT);

  pinMode(JOY_BUTTON, INPUT_PULLUP);

  digitalWrite(TRIG_PIN, LOW);

  // Seed random generator
  randomSeed(analogRead(A2));

  Serial.println("GO_AWAY_MACHINE_READY");
}


// ============================================================
// SINGLE HC-SR04 READING
// ============================================================

float readSingleDistance() {

  // Make sure trigger starts LOW
  digitalWrite(TRIG_PIN, LOW);

  delayMicroseconds(3);

  // Send 10 microsecond trigger pulse
  digitalWrite(TRIG_PIN, HIGH);

  delayMicroseconds(10);

  digitalWrite(TRIG_PIN, LOW);


  // Measure echo pulse
  unsigned long duration =
      pulseIn(
        ECHO_PIN,
        HIGH,
        ECHO_TIMEOUT
      );


  // No echo received
  if (duration == 0) {

    return 999.0;

  }


  /*
     Speed of sound ≈ 0.0343 cm/us

     Distance =
       time × speed / 2

     Divide by 2 because sound travels:
       sensor -> object
       object -> sensor
  */

  float distance =
      (duration * 0.0343) / 2.0;


  // Reject physically unreasonable values

  if (distance < 2.0 || distance > 400.0) {

    return 999.0;

  }


  return distance;
}


// ============================================================
// SORT ARRAY
// ============================================================

void sortReadings(
  float readings[],
  int count
) {

  for (int i = 0; i < count - 1; i++) {

    for (int j = i + 1; j < count; j++) {

      if (readings[j] < readings[i]) {

        float temp =
            readings[i];

        readings[i] =
            readings[j];

        readings[j] =
            temp;

      }

    }

  }

}


// ============================================================
// ROBUST DISTANCE READING
// ============================================================

float readDistance() {

  float readings[
    NUM_DISTANCE_READINGS
  ];

  int validReadings = 0;


  /*
     Take several measurements.

     We wait between measurements because
     the previous ultrasonic pulse can still
     be bouncing around the room.
  */

  for (
    int i = 0;
    i < NUM_DISTANCE_READINGS;
    i++
  ) {

    float reading =
        readSingleDistance();


    // Only store valid readings

    if (reading < 400.0) {

      readings[validReadings] =
          reading;

      validReadings++;

    }


    // Small gap between ultrasonic pulses

    delay(20);

  }


  // No valid readings

  if (validReadings == 0) {

    return 999.0;

  }


  // Sort valid readings

  sortReadings(
    readings,
    validReadings
  );


  /*
     Return MEDIAN rather than average.

     Example:

       18
       19
       20
       20
       95

     Average = 34.4 cm ❌

     Median = 20 cm ✅

     This is much better for an ultrasonic
     sensor because occasional bad reflections
     won't destroy the result.
  */

  return readings[
    validReadings / 2
  ];
}


// ============================================================
// JOYSTICK
// ============================================================

void readJoystick() {

  joystickX =
      analogRead(JOY_X);

  joystickY =
      analogRead(JOY_Y);

}


// ============================================================
// SEND DATA TO BROWSER
// ============================================================

void sendData() {

  int button =
      !digitalRead(JOY_BUTTON);


  Serial.print("DATA,");

  Serial.print(
    distanceCM,
    1
  );

  Serial.print(",");

  Serial.print(
    joystickX
  );

  Serial.print(",");

  Serial.print(
    joystickY
  );

  Serial.print(",");

  Serial.println(
    button
  );

}


// ============================================================
// BUZZER
// ============================================================

void updateBuzzer() {

  if (alarmLevel <= 0) {

    noTone(BUZZER_PIN);

    return;

  }


  int frequency;


  switch (alarmLevel) {

    case 1:

      frequency = 700;

      break;


    case 2:

      frequency = 1000;

      break;


    case 3:

      frequency = 1300;

      break;


    case 4:

      frequency = 1700;

      break;


    case 5:

      frequency = 2200;

      break;


    default:

      frequency = 700;

      break;

  }

  // Keep the buzzer sounding continuously while an alarm is active.
  tone(BUZZER_PIN, frequency);

}


// ============================================================
// PROCESS BROWSER COMMAND
// ============================================================

void processCommand(
  String command
) {

  command.trim();


  if (
    command ==
    "ALARM:0"
  ) {

    alarmLevel = 0;

    noTone(
      BUZZER_PIN
    );

  }


  else if (
    command ==
    "ALARM:1"
  ) {

    alarmLevel = 1;

  }


  else if (
    command ==
    "ALARM:2"
  ) {

    alarmLevel = 2;

  }


  else if (
    command ==
    "ALARM:3"
  ) {

    alarmLevel = 3;

  }


  else if (
    command ==
    "ALARM:4"
  ) {

    alarmLevel = 4;

  }


  else if (
    command ==
    "ALARM:5"
  ) {

    alarmLevel = 5;

  }


  else if (
    command ==
    "ESCAPED"
  ) {

    alarmLevel = 0;

    noTone(
      BUZZER_PIN
    );

    Serial.println(
      "SYSTEM:ESCAPED"
    );

  }


  else if (
    command ==
    "BEEP"
  ) {

    tone(
      BUZZER_PIN,
      1200,
      200
    );

  }

}


// ============================================================
// READ SERIAL COMMANDS
// ============================================================

void readSerialCommands() {

  if (!Serial.available()) {

    return;

  }


  String command =
      Serial.readStringUntil('\n');


  processCommand(
    command
  );

}


// ============================================================
// MAIN LOOP
// ============================================================

void loop() {

  // Check browser commands

  readSerialCommands();


  // Update sensors every 200 ms

  if (
    millis() -
    lastSensorUpdate
    >= 200
  ) {

    lastSensorUpdate =
        millis();


    // Read ultrasonic sensor

    distanceCM =
        readDistance();


    // Read joystick

    readJoystick();

  }


  // Send data to browser every 100 ms

  if (
    millis() -
    lastDataSend
    >= 100
  ) {

    lastDataSend =
        millis();


    sendData();

  }


  // Update physical buzzer

  updateBuzzer();

}