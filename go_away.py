import tkinter as tk
import serial
import threading
import time
import random
import pygame


# =====================================================
# SETTINGS
# =====================================================

SERIAL_PORT = "COM7"       # CHANGE THIS
BAUD_RATE = 9600


# =====================================================
# INITIALIZE AUDIO
# =====================================================

pygame.mixer.init()


# =====================================================
# WARNING MESSAGES
# =====================================================

warning_messages = [
    "You're getting a little close...",
    "Could we have some personal space?",
    "Umm... back up please.",
    "I can see you coming.",
]

too_close_messages = [
    "Bro. Seriously?",
    "You're literally in my bubble.",
    "I don't know you like that.",
    "Personal space, please.",
]

go_away_messages = [
    "GO AWAY.",
    "BACK UP.",
    "PERSONAL SPACE VIOLATION!",
    "WHY ARE YOU STILL COMING?!",
]


# =====================================================
# GLOBAL VARIABLES
# =====================================================

distance = 999
zone = 0

violations = 0
closest_distance = 999

social_battery = 100

last_zone = -1
last_audio_time = 0


# =====================================================
# PLAY AUDIO
# =====================================================

def play_sound(filename):

    try:
        pygame.mixer.music.load("sounds/" + filename)
        pygame.mixer.music.play()

    except Exception as e:
        print("Audio error:", e)


# =====================================================
# READ ARDUINO
# =====================================================

def read_arduino():

    global distance
    global zone
    global violations
    global closest_distance
    global social_battery
    global last_zone
    global last_audio_time

    try:

        arduino = serial.Serial(
            SERIAL_PORT,
            BAUD_RATE,
            timeout=1
        )

        time.sleep(2)

        print("Connected to Arduino!")

        while True:

            line = arduino.readline().decode(
                "utf-8",
                errors="ignore"
            ).strip()

            if not line:
                continue

            print(line)

            # Example:
            # DISTANCE:45.2,ZONE:2

            if line.startswith("DISTANCE:"):

                try:

                    parts = line.split(",")

                    distance = float(
                        parts[0].split(":")[1]
                    )

                    zone = int(
                        parts[1].split(":")[1]
                    )

                    # Track closest distance
                    if distance < closest_distance:
                        closest_distance = distance

                    # Social battery
                    if zone >= 2:
                        social_battery -= 0.1

                    else:
                        social_battery += 0.2

                    social_battery = max(
                        0,
                        min(100, social_battery)
                    )

                    # Count violations
                    if zone == 3 and last_zone != 3:

                        violations += 1

                    # Play audio only when zone changes
                    current_time = time.time()

                    if (
                        zone != last_zone
                        and current_time - last_audio_time > 2
                    ):

                        if zone == 1:

                            play_sound("warning.mp3")

                        elif zone == 2:

                            play_sound("close.mp3")

                        elif zone == 3:

                            play_sound("go_away.mp3")

                        last_audio_time = current_time

                    last_zone = zone

                except Exception as e:

                    print("Data error:", e)

    except Exception as e:

        print("Could not connect to Arduino:")
        print(e)


# =====================================================
# UPDATE DASHBOARD
# =====================================================

def update_dashboard():

    global distance
    global zone

    distance_label.config(
        text=f"{distance:.1f} cm"
    )

    # ---------------------------------------------
    # SAFE
    # ---------------------------------------------

    if zone == 0:

        root.configure(bg="#071a12")

        title_label.config(
            bg="#071a12",
            fg="#00ff88"
        )

        status_label.config(
            text="🟢 SAFE",
            bg="#071a12",
            fg="#00ff88"
        )

        message_label.config(
            text="You're fine. For now.",
            bg="#071a12",
            fg="white"
        )

    # ---------------------------------------------
    # WARNING
    # ---------------------------------------------

    elif zone == 1:

        root.configure(bg="#191704")

        title_label.config(
            bg="#191704",
            fg="#ffd000"
        )

        status_label.config(
            text="🟡 GETTING CLOSE",
            bg="#191704",
            fg="#ffd000"
        )

        message_label.config(
            text=random.choice(warning_messages),
            bg="#191704",
            fg="white"
        )

    # ---------------------------------------------
    # TOO CLOSE
    # ---------------------------------------------

    elif zone == 2:

        root.configure(bg="#1c0d02")

        title_label.config(
            bg="#1c0d02",
            fg="#ff8800"
        )

        status_label.config(
            text="🟠 TOO CLOSE",
            bg="#1c0d02",
            fg="#ff8800"
        )

        message_label.config(
            text=random.choice(too_close_messages),
            bg="#1c0d02",
            fg="white"
        )

    # ---------------------------------------------
    # GO AWAY
    # ---------------------------------------------

    elif zone == 3:

        root.configure(bg="#250000")

        title_label.config(
            bg="#250000",
            fg="#ff2222"
        )

        status_label.config(
            text="🚨 PERSONAL SPACE VIOLATION 🚨",
            bg="#250000",
            fg="#ff2222"
        )

        message_label.config(
            text=random.choice(go_away_messages),
            bg="#250000",
            fg="white"
        )

    # ---------------------------------------------
    # STATISTICS
    # ---------------------------------------------

    battery_label.config(
        text=f"Social Battery: {social_battery:.0f}%"
    )

    violation_label.config(
        text=f"Violations: {violations}"
    )

    closest_label.config(
        text=f"Closest Approach: {closest_distance:.1f} cm"
    )

    # Run again after 100 ms
    root.after(100, update_dashboard)


# =====================================================
# CREATE WINDOW
# =====================================================

root = tk.Tk()

root.title("THE GO-AWAY MACHINE™")

root.attributes(
    "-fullscreen",
    True
)

root.configure(
    bg="#071a12"
)


# =====================================================
# TITLE
# =====================================================

title_label = tk.Label(

    root,

    text="THE GO-AWAY MACHINE™",

    font=("Arial", 42, "bold"),

    bg="#071a12",

    fg="#00ff88"
)

title_label.pack(
    pady=(50, 20)
)


# =====================================================
# DISTANCE
# =====================================================

distance_label = tk.Label(

    root,

    text="--- cm",

    font=("Arial", 80, "bold"),

    bg="#071a12",

    fg="white"
)

distance_label.pack(
    pady=20
)


# =====================================================
# STATUS
# =====================================================

status_label = tk.Label(

    root,

    text="🟢 SAFE",

    font=("Arial", 32, "bold"),

    bg="#071a12",

    fg="#00ff88"
)

status_label.pack(
    pady=10
)


# =====================================================
# MESSAGE
# =====================================================

message_label = tk.Label(

    root,

    text="Waiting for humans...",

    font=("Arial", 28),

    bg="#071a12",

    fg="white"
)

message_label.pack(
    pady=30
)


# =====================================================
# SOCIAL BATTERY
# =====================================================

battery_label = tk.Label(

    root,

    text="Social Battery: 100%",

    font=("Arial", 24),

    bg="#071a12",

    fg="white"
)

battery_label.pack(
    pady=10
)


# =====================================================
# STATISTICS
# =====================================================

violation_label = tk.Label(

    root,

    text="Violations: 0",

    font=("Arial", 20),

    bg="#071a12",

    fg="#cccccc"
)

violation_label.pack(
    pady=5
)


closest_label = tk.Label(

    root,

    text="Closest Approach: ---",

    font=("Arial", 20),

    bg="#071a12",

    fg="#cccccc"
)

closest_label.pack(
    pady=5
)


# =====================================================
# EXIT INSTRUCTION
# =====================================================

exit_label = tk.Label(

    root,

    text="Press ESC to exit",

    font=("Arial", 14),

    bg="#071a12",

    fg="#666666"
)

exit_label.pack(
    pady=30
)


# =====================================================
# ESCAPE KEY
# =====================================================

root.bind(
    "<Escape>",
    lambda event: root.destroy()
)


# =====================================================
# START ARDUINO THREAD
# =====================================================

arduino_thread = threading.Thread(

    target=read_arduino,

    daemon=True
)

arduino_thread.start()


# =====================================================
# START DASHBOARD
# =====================================================

update_dashboard()

root.mainloop()