import pywhatkit as kit
import datetime
from TextToSpeech.Fast_DF_TTS import speak
from os import getcwd

# Add contacts here locally.
# Do not commit real phone numbers to a public GitHub repository.
CONTACTS = {
    # "sameer": "+91XXXXXXXXXX",
    # "john": "+91XXXXXXXXXX",
}


def clear_file():
    with open(f"{getcwd()}\\input.txt", "w") as file:
        file.truncate(0)


def send_msg_wa():
    speak("Who do you want to send the message to?")

    previous_input = ""

    while True:
        with open("input.txt", "r") as file:
            input_text = file.read().strip().lower()

        if not input_text or input_text == previous_input:
            continue

        previous_input = input_text

        if input_text.startswith(("send to ", "send tu ")):
            contact_name = (
                input_text
                .replace("send to ", "", 1)
                .replace("send tu ", "", 1)
                .strip()
            )

            if contact_name not in CONTACTS:
                speak(f"I could not find {contact_name} in your contacts.")
                return

            phone_number = CONTACTS[contact_name]

            speak("What message should I send?")

            while True:
                with open("input.txt", "r") as file:
                    message_input = file.read().strip()

                if not message_input or message_input.lower() == previous_input.lower():
                    continue

                if message_input.lower().startswith("message is"):
                    message = message_input[10:].strip()

                    now = datetime.datetime.now()
                    send_time = now + datetime.timedelta(minutes=2)

                    kit.sendwhatmsg(
                        phone_number,
                        message,
                        send_time.hour,
                        send_time.minute
                    )

                    speak("Message scheduled successfully.")
                    return