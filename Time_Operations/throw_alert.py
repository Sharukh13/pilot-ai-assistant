import os
import time
import threading

from Alert import Alert
from TextToSpeech.Fast_DF_TTS import speak


# ============================================================
# PILOT AI - ALERT / SCHEDULE SYSTEM
# ============================================================

# Automatically detect project root
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

SCHEDULE_PATH = os.path.join(BASE_DIR, "schedule.txt")
ALARM_PATH = os.path.join(BASE_DIR, "Alam_data.txt")


# ============================================================
# SCHEDULE
# ============================================================

def load_schedule(file_path):
    schedule = {}

    try:
        with open(file_path, "r", encoding="utf-8") as file:

            for line in file:
                line = line.strip()

                if " = " in line:
                    line_time, activity = line.split(" = ", 1)

                    schedule[line_time.strip()] = activity.strip()

    except FileNotFoundError:
        print(f"Schedule file not found: {file_path}")

    except Exception as error:
        print(f"Error loading schedule: {error}")

    return schedule


def trigger_alert(text):
    print(f"Pilot Alert: {text}")

    alert_thread = threading.Thread(
        target=Alert,
        args=(text,)
    )

    speech_thread = threading.Thread(
        target=speak,
        args=(text,)
    )

    alert_thread.start()
    speech_thread.start()


def check_schedule(file_path=SCHEDULE_PATH):

    last_modified = None
    schedule = {}
    last_triggered = None

    print("Pilot schedule monitor started.")

    while True:

        current_time = time.strftime("%I:%M%p")

        try:
            if os.path.exists(file_path):

                modified = os.path.getmtime(file_path)

                if modified != last_modified:
                    last_modified = modified
                    schedule = load_schedule(file_path)

                if current_time in schedule:

                    # Prevent same alert firing repeatedly
                    if last_triggered != current_time:

                        text = schedule[current_time]

                        trigger_alert(text)

                        last_triggered = current_time

                elif last_triggered != current_time:
                    last_triggered = None

        except Exception as error:
            print(f"Schedule Error: {error}")

        time.sleep(5)


# ============================================================
# ALARM
# ============================================================

def load_alarm_time(file_path):

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read().strip()

    except FileNotFoundError:
        return ""

    except Exception as error:
        print(f"Error loading alarm: {error}")
        return ""


def check_Alam(Alam_path=ALARM_PATH):

    last_modified = None
    alarm_time = ""
    last_triggered = None

    print("Pilot alarm monitor started.")

    while True:

        current_time = time.strftime("%I:%M%p")

        try:

            if os.path.exists(Alam_path):

                modified = os.path.getmtime(Alam_path)

                if modified != last_modified:
                    last_modified = modified
                    alarm_time = load_alarm_time(Alam_path)

                if alarm_time and current_time == alarm_time:

                    if last_triggered != current_time:

                        trigger_alert("This is your alarm, sir.")

                        last_triggered = current_time

                elif current_time != last_triggered:
                    last_triggered = None

        except Exception as error:
            print(f"Alarm Error: {error}")

        time.sleep(5)


# ============================================================
# START BOTH MONITORS
# ============================================================

def start_time_operations():

    print("Starting Pilot AI Time Operations...")

    schedule_thread = threading.Thread(
        target=check_schedule,
        daemon=True
    )

    alarm_thread = threading.Thread(
        target=check_Alam,
        daemon=True
    )

    schedule_thread.start()
    alarm_thread.start()

    return schedule_thread, alarm_thread


# ============================================================
# DIRECT TEST
# ============================================================

if __name__ == "__main__":

    print("Pilot AI Alert System Ready")
    print("Schedule:", SCHEDULE_PATH)
    print("Alarm:", ALARM_PATH)

    start_time_operations()

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nPilot AI Alert System stopped.")