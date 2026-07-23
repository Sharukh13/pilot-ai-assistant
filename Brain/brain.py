import requests
import webbrowser
import time
import pyautogui

from Automation.screen_control import *


# ==========================================
# MEMORY
# ==========================================

last_topic = ""
detail_level = 0


# ==========================================
# OLLAMA AI
# ==========================================

def ask_ollama(prompt, level=0):

    if level == 0:

        style_instruction = (
            "Reply in 2 short sentences only."
        )

        num_predict = 80

    elif level == 1:

        style_instruction = """
Give a medium detailed explanation.

Include:
- Background
- Main achievements
- Current status
"""

        num_predict = 250

    else:

        style_instruction = """
Give a VERY detailed explanation.

Include:
- Early life
- Education
- Career
- Achievements
- Personal life
- Future goals

Use many bullet points.
"""

        num_predict = 800

    try:

        print("\nSending to Ollama...")

        response = requests.post(

            "http://127.0.0.1:11434/api/generate",

            json={

                "model": "llama3",

                "prompt": f"""
You are Pilot AI, an intelligent personal desktop assistant.

{style_instruction}

Question:
{prompt}
""",

                "stream": False,

                "options": {

                    "num_predict": num_predict,
                    "temperature": 0.7,
                    "top_k": 40,
                    "top_p": 0.9

                }

            },

            timeout=90

        )

        print("Ollama replied")

        data = response.json()

        answer = data.get(
            "response",
            ""
        )

        return answer.strip()

    except Exception as e:

        print(
            "\nOllama Error:",
            e
        )

        return (
            "Sorry sir, AI brain is offline."
        )


# ==========================================
# MAIN BRAIN
# ==========================================

def Main_Brain(text):

    global last_topic
    global detail_level

    try:

        text = text.lower().strip()

        # ==========================
        # OPEN YOUTUBE
        # ==========================

        if "open youtube" in text:

            webbrowser.open(
                "https://www.youtube.com"
            )

            return (
                "Opening YouTube sir."
            )

        # ==========================
        # OPEN GOOGLE
        # ==========================

        elif "open google" in text:

            webbrowser.open(
                "https://www.google.com"
            )

            return (
                "Opening Google sir."
            )

        # ==========================
        # OPEN CHROME
        # ==========================

        elif "open chrome" in text:

            webbrowser.open(
                "https://www.google.com"
            )

            return (
                "Opening Chrome sir."
            )

        # ==========================
        # UNIVERSAL SEARCH
        # ==========================

        elif text.startswith("search"):

            query = text.replace(
                "search",
                ""
            ).strip()

            try:

                # RESET FOCUS
                pyautogui.press("esc")

                time.sleep(0.5)

                found = False

                # TAB NAVIGATION
                for _ in range(15):

                    press_tab()

                    time.sleep(0.4)

                    found = True

                    break

                if found:

                    # CLEAR OLD TEXT
                    pyautogui.hotkey(
                        "ctrl",
                        "a"
                    )

                    pyautogui.press(
                        "backspace"
                    )

                    # TYPE SEARCH
                    type_text(query)

                    time.sleep(0.5)

                    press_enter()

                    return (
                        f"Searching {query}"
                    )

                return (
                    "Input field not found."
                )

            except Exception as e:

                print(
                    "Search Error:",
                    e
                )

                return (
                    "Search failed."
                )

        # ==========================
        # SCROLL DOWN
        # ==========================

        elif "scroll down" in text:

            scroll_down()

            return (
                "Scrolling down."
            )

        # ==========================
        # SCROLL UP
        # ==========================

        elif "scroll up" in text:

            scroll_up()

            return (
                "Scrolling up."
            )

        # ==========================
        # STOP SCROLL
        # ==========================

        elif any(word in text for word in [

            "stop scrolling",
            "stop scroll",
            "stop",
            "niruthu",
            "niruththu",
            "podhum",
            "pause scrolling",
            "pause scroll"

        ]):

            stop_scroll()

            return (
                "Stopping scrolling."
            )

        # ==========================
        # TYPE TEXT
        # ==========================

        elif text.startswith("type"):

            query = text.replace(
                "type",
                ""
            ).strip()

            type_text(query)

            return (
                f"Typing {query}"
            )

        # ==========================
        # PRESS ENTER
        # ==========================

        elif "press enter" in text:

            press_enter()

            return (
                "Pressed enter."
            )

        # ==========================
        # LEFT CLICK
        # ==========================

        elif "click" in text:

            left_click()

            return (
                "Clicking."
            )

        # ==========================
        # DOUBLE CLICK
        # ==========================

        elif "double click" in text:

            double_click()

            return (
                "Double clicking."
            )

        # ==========================
        # RIGHT CLICK
        # ==========================

        elif "right click" in text:

            right_click()

            return (
                "Right clicking."
            )

        # ==========================
        # MORE INFORMATION
        # ==========================

        elif any(phrase in text for phrase in [

            "more information",
            "tell me more",
            "give me more",
            "more detail",
            "explain more",
            "elaborate",
            "expand"

        ]):

            if last_topic == "":

                return (
                    "Please ask a topic first sir."
                )

            if detail_level < 2:

                detail_level += 1

            answer = ask_ollama(

                f"""
Continue explaining this topic in more detail:

{last_topic}

Do not introduce yourself.
Do not talk about being an AI.
Only continue the topic.
""",

                level=detail_level

            )

            return answer

        # ==========================
        # NORMAL AI
        # ==========================

        else:

            detail_level = 0

            last_topic = text

            answer = ask_ollama(
                text,
                level=0
            )

            return answer

    except Exception as e:

        print(
            "\nBrain Error:",
            e
        )

        return (
            "Sorry sir, I encountered an error."
        )