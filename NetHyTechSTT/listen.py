import speech_recognition as sr
import time


# ==========================================
# STATES
# ==========================================

is_listening = True
last_text = ""


# ==========================================
# LISTEN
# ==========================================

def listen():

    global is_listening
    global last_text

    recognizer = sr.Recognizer()

    while True:

        try:

            # MIC PAUSE
            if not is_listening:

                time.sleep(0.1)

                continue

            with sr.Microphone() as source:

                print("\nListening...")

                recognizer.adjust_for_ambient_noise(
                    source,
                    duration=1
                )

                audio = recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=5
                )

            text = recognizer.recognize_google(
                audio
            )

            text = text.lower().strip()

            # EMPTY IGNORE
            if len(text) <= 1:
                continue

            # DUPLICATE IGNORE
            if text == last_text:
                continue

            last_text = text

            # STOP COMMAND
           

            print(
                "\nUser:",
                text
            )

            return text

        except sr.WaitTimeoutError:

            continue

        except sr.UnknownValueError:

            continue

        except sr.RequestError as e:

            print(
                "\nSpeech Recognition Error:",
                e
            )

        except Exception as e:

            print(
                "\nListening Error:",
                e
            )