import pyautogui
import pygetwindow as gw
import threading
import time
import sys
import os

ROOT_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from Screen_AI.screen_reader import find_text_location


# ==========================================
# GLOBALS
# ==========================================

scrolling = False

locked_window = None


# ==========================================
# GET ACTIVE WINDOW
# ==========================================

def get_active_window():

    try:

        return gw.getActiveWindow()

    except:
        return None


# ==========================================
# CONTINUOUS SCROLL
# ==========================================

def continuous_scroll(direction):

    global scrolling
    global locked_window

    while scrolling:

        try:

            current_window = gw.getActiveWindow()

            # STOP if user changed window
            if current_window != locked_window:

                scrolling = False

                break

            if direction == "down":

                pyautogui.scroll(-80)

            elif direction == "up":

                pyautogui.scroll(80)

            time.sleep(0.2)

        except Exception as e:

            print(
                "Scroll Error:",
                e
            )

            scrolling = False


# ==========================================
# SCROLL DOWN
# ==========================================

def scroll_down():

   

    global scrolling
    global locked_window

    # FORCE RESET
    scrolling = False

    time.sleep(0.1)

    locked_window = get_active_window()

    scrolling = True

    threading.Thread(

        target=continuous_scroll,

        args=("down",),

        daemon=True

    ).start()


# ==========================================
# SCROLL UP
# ==========================================

def scroll_up():

    global scrolling
    global locked_window

    # FORCE RESET
    scrolling = False

    time.sleep(0.1)

    locked_window = get_active_window()

    scrolling = True

    threading.Thread(

        target=continuous_scroll,

        args=("up",),

        daemon=True

    ).start()

# ==========================================
# STOP SCROLL
# ==========================================

def stop_scroll():

    global scrolling

    scrolling = False

    print(
        "\nScrolling stopped."
    )
# ==========================================
# TYPE TEXT
# ==========================================

def type_text(text):

    try:

        time.sleep(0.5)

        # FORCE CLICK CENTER
        pyautogui.click()

        time.sleep(0.3)

        # SELECT ALL
        pyautogui.hotkey(
            "ctrl",
            "a"
        )

        time.sleep(0.2)

        # DELETE OLD TEXT
        pyautogui.press(
            "backspace"
        )

        time.sleep(0.2)

        # TYPE NEW TEXT
        pyautogui.write(

            text,

            interval=0.05

        )

    except Exception as e:

        print(
            "Typing Error:",
            e
        )

# ==========================================
# PRESS ENTER
# ==========================================

def press_enter():

    try:

        pyautogui.press(
            "enter"
        )

    except Exception as e:

        print(
            "Enter Error:",
            e
        )


# ==========================================
# LEFT CLICK
# ==========================================

def left_click():

    try:

        pyautogui.click()

    except Exception as e:

        print(
            "Click Error:",
            e
        )


# ==========================================
# DOUBLE CLICK
# ==========================================

def double_click():

    try:

        pyautogui.doubleClick()

    except Exception as e:

        print(
            "Double Click Error:",
            e
        )


# ==========================================
# RIGHT CLICK
# ==========================================

def right_click():

    try:

        pyautogui.rightClick()

    except Exception as e:

        print(
            "Right Click Error:",
            e
        )
        
# ==========================================
# CLICK TEXT
# ==========================================

def click_text(target):

    location = find_text_location(
        target
    )

    if location:

        pyautogui.click(location)

        return True

    return False
# ==========================================
# PRESS TAB
# ==========================================

def press_tab():

    pyautogui.press("tab")


# ==========================================
# PRESS ESC
# ==========================================

def press_escape():

    pyautogui.press("esc")