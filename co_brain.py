from matplotlib.pylab import rint

from Automation.Automation_Brain import (
    Auto_main_brain,
    clear_file
)

from NetHyTechSTT.listen import listen

from TextToSpeech.Fast_DF_TTS import speak

import threading

from Data.DLG_Data import (
    online_dlg,
    offline_dlg
)

import random

from Automation.Battery import battery_Alert

from Time_Operations.brain import (
    input_manage,
    input_manage_Alam
)

from Brain.brain import Main_Brain

from Features.create_file import create_file

from Vision.Vbrain import *

from Vision.MVbrain import *

from Weather_Check.check_weather import (
    get_weather_by_address
)

from Whatsapp_automation.wa import send_msg_wa

from TextToImage.gen_image import generate_image

from Features.mike_health import mike_health

from Features.speaker_health import (
    speaker_health_test
)

from Features.br_persentage import (
    check_br_persentage
)

from Features.set_br import (
    set_brightness_windows
)

from Features.set_get_volume import *

from Features.check_running_app import *
from os import getcwd
print("CO_BRAIN STARTED")


# ==========================================
# GLOBALS
# ==========================================

numbers = [
    "1:",
    "2:",
    "3:",
    "4:",
    "5:",
    "6:",
    "7:",
    "8:",
    "9:"
]

spl_numbers = [
    "11:",
    "12:"
]

ran_online_dlg = random.choice(
    online_dlg
)

ran_offline_dlg = random.choice(
    offline_dlg
)


# ==========================================
# SAFE SPEAK
# ==========================================

def safe_speak(text):

    try:

        print("\nPilot:", text) 

        speak(text)

    except Exception as e:

        print(
            "\nTTS Error:",
            e
        )

        print(
            "\nPilot:",
            text
        )


# ==========================================
# INPUT CHECKER
# ==========================================
def check_inputs():
    print("CHECK_INPUTS FUNCTION RUNNING")

    output_text = ""

    while True:

        try:

            with open(
    f"{getcwd()}\\input.txt",
                "r",
                encoding="utf-8"
            ) as file:

                input_text = (
                    file.read().lower()
                )

            input_text = input_text.strip()

            if input_text == "":
                continue

            if input_text == output_text:
                continue

            output_text = input_text
            print("INPUT DETECTED")

            print(
                "\nUser:",
                output_text
            )
        except Exception as e:

            print(
                "\nMain Loop Error:",
                e
            )
                # =====================
                # REMINDER
                # =====================
    def check_inputs():

            output_text = ""

    while True:

        try:

            with open(
                "input.txt",
                "r",
                encoding="utf-8"
            ) as file:

                input_text = (
                    file.read().lower()
                )

            input_text = input_text.strip()

            # EMPTY INPUT
            if input_text == "":
                continue

            # STOP DUPLICATE
            if input_text == output_text:
                continue

            output_text = input_text

            print(
                "\nUser:",
                output_text
            )

            # =====================
            # REMINDER
            # =====================

            if output_text.startswith(
                "tell me"
            ):

                output_text = output_text.replace(
                    " p.m.",
                    "PM"
                )

                output_text = output_text.replace(
                    " a.m.",
                    "AM"
                )

                if (
                    "11:" in output_text
                    or
                    "12:" in output_text
                ):

                    input_manage(
                        output_text
                    )

                    clear_file()

                else:

                    for number in numbers:

                        if number in output_text:

                            output_text = (
                                output_text.replace(
                                    number,
                                    f"0{number}"
                                )
                            )

                            input_manage(
                                output_text
                            )

                            clear_file()

            # =====================
            # ALARM
            # =====================

            elif output_text.startswith(
                "set alarm"
            ):

                output_text = output_text.replace(
                    " p.m.",
                    "PM"
                )

                output_text = output_text.replace(
                    " a.m.",
                    "AM"
                )

                if (
                    "11:" in output_text
                    or
                    "12:" in output_text
                ):

                    input_manage_Alam(
                        output_text
                    )

                    clear_file()

                else:

                    for number in numbers:

                        if number in output_text:

                            output_text = (
                                output_text.replace(
                                    number,
                                    f"0{number}"
                                )
                            )

                            input_manage_Alam(
                                output_text
                            )

                            clear_file()

            # =====================
            # PILOT AI
            # =====================

            elif (

                "pilot" in output_text
                or
                "who" in output_text
                or
                "what" in output_text
                or
                "when" in output_text
                or
                "where" in output_text
                or
                "why" in output_text
                or
                "how" in output_text
                or
                "more information" in output_text
                or
                "tell me more" in output_text
                or
                "explain more" in output_text

            ):

                try:

                    with open(
                        "log.txt",
                        "a",
                        encoding="utf-8"
                    ) as f:

                        f.write(
                            '\nYou : '
                            + output_text
                        )

                    response = Main_Brain(
                        output_text
                    )
                    print("AI RESPONSE:", response)

                    with open(
                        "log.txt",
                        "a",
                        encoding="utf-8"
                    ) as f:

                        f.write(
                            '\nPilot : '
                            + response
                        )

                    safe_speak(response)

                    clear_file()

                except Exception as e:

                    print(
                        "\nBrain Error:",
                        e
                    )

            # =====================
            # CREATE FILE
            # =====================

            elif output_text.startswith(
                "create"
            ):

                if "file" in output_text:

                    create_file(
                        output_text
                    )

                    clear_file()

            # =====================
            # VISION
            # =====================

            elif (
                "what is this"
                in output_text
                or
                "what can you see"
                in output_text
            ):

                image_path = (
                    "captured_image.png"
                )

                if capture_image_and_save(
                    image_path
                ):

                    encoded_image = (
                        encode_image_to_base64(
                            image_path
                        )
                    )

                    answer = vision_brain(
                        encoded_image
                    )

                    safe_speak(answer)

                    clear_file()

            # =====================
            # WEATHER
            # =====================

            elif "check weather" in output_text:

                text = output_text.replace(
                    "check weather in",
                    ""
                )

                ans = get_weather_by_address(
                    text
                )

                safe_speak(ans)

                clear_file()

            # =====================
            # FALLBACK AUTOMATION
            # =====================

            else:

                Auto_main_brain(
                    output_text
                )

                clear_file()

        except Exception as e:

            print(
                "\nMain Loop Error:",
                e
            )
# ==========================================
# MAIN PILOT
# ==========================================

def Pilot():

    clear_file()

    safe_speak(
        "Sir, I am online and ready to support"
    )

    t1 = threading.Thread(
        target=listen
    )

    t2 = threading.Thread(
        target=check_inputs
    )

    t1.start()

    t2.start()

    t1.join()

    t2.join()