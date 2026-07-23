import pyttsx3
import threading


# ==========================================
# ENGINE
# ==========================================

engine = pyttsx3.init()

engine.setProperty(
    'rate',
    170
)

engine.setProperty(
    'volume',
    1.0
)

voices = engine.getProperty(
    'voices'
)

engine.setProperty(
    'voice',
    voices[0].id
)


# ==========================================
# SPEECH LOCK
# ==========================================

speech_lock = threading.Lock()


# ==========================================
# SPEAK CORE
# ==========================================

def Co_speak(message):

    try:

        from NetHyTechSTT import listen

        # STOP MIC
        listen.is_listening = False

        with speech_lock:

            engine.say(message)

            engine.runAndWait()

        # START MIC AGAIN
        listen.is_listening = True

    except Exception as e:

        print(
            "\nTTS Error:",
            e
        )

        try:

            listen.is_listening = True

        except:
            pass


# ==========================================
# MAIN SPEAK
# ==========================================

def speak(text):

    try:

        # DIRECT SPEAK
        Co_speak(text)

    except Exception as e:

        print(
            "Speak Error:",
            e
        )