<img width="1280" height="640" alt="git (1)" src="https://github.com/user-attachments/assets/8920b256-2ba8-4988-b824-5351134eb4bd" />



###Poyi Pani Nokku


## Basic Details
### Team Name: ENIGMA


### Team Members
- Team Lead: ABHITHA ABHILASH - SCHOOL OF ENGINEERING, CUSAT
- Member 2: ANAINA VIBIN - SCHOOL OF ENGINEERING, CUSAT

### Project Description
A sensor-based personal space alarm that detects proximity and escalates from polite warnings to a full dramatic meltdown as someone gets too close. The ironic twist: the louder and more theatrical the alarm gets trying to keep people away, the more attention it actually attracts — making it the exact opposite of what it was built for.

### The Problem (that doesn't exist)
Somewhere right now, an introvert is trying to enjoy some peace and personal space.

But then someone gets too close.

They don't want to start a conversation. They don't want to awkwardly ask the person to move. They just want them to stay out of their personal space.

A completely unnecessary problem, obviously. You could simply move away or say “excuse me.”

But where's the technology in that?

### The Solution (that nobody asked for)
We built a device that detects when someone enters an introvert's personal space and immediately triggers an alarm to warn them to back off.

There's just one tiny flaw:

The alarm attracts everyone's attention.

So instead of quietly avoiding social interaction, the introvert now has a loud device announcing:

“PLEASE STAY AWAY FROM ME.”

A problem that could have been solved by simply moving two steps away — now requires a sensor, a microcontroller, an alarm, and unnecessary amounts of engineering.

Useless? Absolutely.
Did we build it anyway? Of course.

## Technical Details
### Technologies/Components Used
For Software:
- [Languages used]
- [Frameworks used]
- [Libraries used]
- [Tools used]

For Hardware:
- Arduino UNO R4 WiFi Board
- Ultrasonic Sensor
- Joystick Module
- RGB LED
- Active Buzzer
- Resistor
- Jumper Wire
- Breadboard
  
### Implementation
For Software:

# Installation
[commands] 

# Run
[commands] 

### Project Documentation
For Software:

# Screenshots (Add at least 3)
![Screenshot1](Add screenshot 1 here with proper name)
*Add caption explaining what this shows*

![Screenshot2](Add screenshot 2 here with proper name)
*Add caption explaining what this shows*

![Screenshot3](Add screenshot 3 here with proper name)
*Add caption explaining what this shows*

# Diagrams

For Hardware:

# Schematic & Circuit
![Circuit](Add your circuit diagram here)
*Add caption explaining connections*


*Schematic Diagram*: 
     https://drive.google.com/file/d/1WoCpQxfyuBmXq9MsLYIJtNRhqxrkRKkx/view?usp=sharing

The schematic shows the connections between the Arduino UNO R4 WiFi and the main hardware components. The HC-SR04 ultrasonic sensor is connected to the Arduino’s digital pins D7 and D6 for distance measurement, while the joystick uses A0 and A1 for X–Y movement and D4 for its switch input. The buzzer is connected to D9 and GND to provide an audio warning. All components share the Arduino’s 5V and GND connections for power and a common reference.

*Workflow:*
    https://drive.google.com/file/d/1Kvz9-FfMWnnXPn41Gz0i3yATkmZgLu30/view?usp=sharing

The ultrasonic sensor detects the distance of an approaching person and sends the readings to the Arduino UNO. Based on the detected distance, the Arduino activates the buzzer and LED to provide different warning levels. At the same time, the Arduino communicates with a website running on the laptop, where the user is given a specific direction to move the joystick. The system checks the joystick input against the given command, allowing the warning response to be controlled through the interaction.

# Build Photos

COMPONENTS:

https://drive.google.com/file/d/1Kk0cS6gF6cYpLYAnyJ_DtCycNqC2V7ZD/view?usp=sharing
- Arduino UNO R4 WiFi Board
- Ultrasonic Sensor
- Joystick Module
- RGB LED
- Active Buzzer
- Resistor
- Jumper Wire
- Breadboard


BUILD:

https://drive.google.com/file/d/1jYhTxi8LCW6jd78FHnsCWT5MU-diSsvD/view?usp=sharing
https://drive.google.com/file/d/1uUCA53P7-1NxrSe88kuW4rMJ08tW6s42/view?usp=sharing
https://drive.google.com/file/d/1jYhTxi8LCW6jd78FHnsCWT5MU-diSsvD/view?usp=sharing

The components were connected to the Arduino according to the circuit design. The ultrasonic sensor was used to detect the distance, while the buzzer and speaker provided the audio responses. The joystick was integrated to control the mini-game, and the Arduino was programmed to connect all these functions into one working system.


FINAL

https://drive.google.com/file/d/1Kk0cS6gF6cYpLYAnyJ_DtCycNqC2V7ZD/view?usp=sharing

The ultrasonic sensor continuously measures the distance between the device and the approaching person. Based on the detected distance, the Arduino triggers different audio warnings through the buzzer/speaker. As the person gets closer, the warnings become more noticeable. When the system reaches the final alert stage, the joystick-controlled mini-game is activated. The user must play and complete the game to stop the audio and reset the system. Once the person moves away and the conditions return to normal, the system is ready to detect the next approach.


### Project Demo
# Video
[Add your demo video link here]
*Explain what the video demonstrates*

# Additional Demos
[Add any extra demo materials/links]

## Team Contributions
- ABHITHA ABHILASH: Contributed to the overall development and implementation of the project, including system integration, testing, and refinement. Worked on selecting and integrating the audio responses, developing the project concept and interaction flow, and preparing the documentation, README, and presentation materials.
  
- ANAINA VIBIN: Contributed to the overall development and implementation of the project, with a primary focus on the hardware and circuit setup. Designed and assembled the circuit, connected and tested the Arduino, ultrasonic sensor, buzzer/speaker, and joystick, and worked on integrating and debugging the system.

---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProjects--26-26?link=https%3A%2F%2Ftinkerhub.org%2Fevents%2F1M8ORET9A1%2Fuseless-projects-3.0)



