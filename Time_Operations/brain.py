import os
import re


# ============================================================
# PILOT AI - TIME OPERATIONS
# ============================================================

# Automatically find the main Pilot AI project folder
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

SCHEDULE_FILE = os.path.join(BASE_DIR, "schedule.txt")
ALARM_FILE = os.path.join(BASE_DIR, "Alam_data.txt")

last_text = ""


# ============================================================
# REMINDER / SCHEDULE
# ============================================================

def parse_input(input_text):
    # Example: 07:30 PM / 8:00pm
    time_regex = r'(\d{1,2}:\d{2} ?(?:AM|PM|am|pm))'

    times = re.findall(time_regex, input_text)

    if times:
        time_match = times[0]

        formatted_time = (
            time_match
            .strip()
            .replace(" ", "")
            .upper()
        )

        updated_input_text = (
            input_text
            .replace(time_match, "")
            .replace("at", "")
            .replace("tell me", "")
            .replace("Tell me", "")
            .replace("to", "")
            .strip()
        )

        formatted_output = (
            f"{formatted_time} = "
            f"Sir this is your {updated_input_text} time"
        )

        return formatted_output, formatted_time

    return "No valid time found in input", None


def save_to_file(output_text, time, filename=SCHEDULE_FILE):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()

    except FileNotFoundError:
        lines = []

    time_found = False

    with open(filename, "w", encoding="utf-8") as file:
        for line in lines:

            if line.startswith(time):
                file.write(output_text + "\n")
                time_found = True

            else:
                file.write(line)

        if not time_found:
            file.write(output_text + "\n")


def input_manage(input_text):
    output, time = parse_input(input_text)

    if output != "No valid time found in input":
        save_to_file(
            output,
            time,
            SCHEDULE_FILE
        )

        print("Schedule_Data_Saved")
        return True

    print(output)
    return False


# ============================================================
# ALARM
# ============================================================

def parse_input_Alarm(input_text):
    time_regex = r'(\d{1,2}:\d{2} ?(?:AM|PM|am|pm))'

    times = re.findall(time_regex, input_text)

    if times:
        time_match = times[0]

        formatted_time = (
            time_match
            .strip()
            .replace(" ", "")
            .upper()
        )

        return formatted_time

    return None


def save_to_Alarmfile(time, filename=ALARM_FILE):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(str(time) + "\n")

        return True

    except OSError as error:
        print(f"Unable to save alarm: {error}")
        return False


def input_manage_Alam(input_text):
    time = parse_input_Alarm(input_text)

    if time:
        save_to_Alarmfile(
            time,
            ALARM_FILE
        )

        print("Alarm_Data_Saved")
        return True

    print("No valid alarm time found")
    return False


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":
    print("Pilot AI Time Operations Ready")
    print("Schedule:", SCHEDULE_FILE)
    print("Alarm:", ALARM_FILE)