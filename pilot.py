from NetHyTechSTT.listen import listen

from Brain.brain import Main_Brain

from TextToSpeech.Fast_DF_TTS import speak


print("_____started___")


while True:

    try:

        # LISTEN
        text = listen()

        # EMPTY
        if not text:
            continue

        print(
            "\nUser:",
            text
        )

        # AI RESPONSE
        response = Main_Brain(text)

        # PRINT RESPONSE
        print(
            "\nPilot:",
            response
        )

        # SPEAK RESPONSE
        speak(response)

    except Exception as e:

        print(
            "\nMAIN LOOP ERROR:",
            e
        )