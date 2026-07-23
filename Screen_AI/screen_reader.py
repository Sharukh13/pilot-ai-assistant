import pyautogui
import pytesseract


# ==========================================
# TESSERACT PATH
# ==========================================

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


# ==========================================
# FIND TEXT LOCATION
# ==========================================

def find_text_location(target_text):

    screenshot = pyautogui.screenshot()

    data = pytesseract.image_to_data(
        screenshot,
        output_type=pytesseract.Output.DICT
    )

    for i, text in enumerate(data["text"]):

        if target_text.lower() in text.lower():

            x = data["left"][i]
            y = data["top"][i]
            w = data["width"][i]
            h = data["height"][i]

            center_x = x + w // 2
            center_y = y + h // 2

            return (
                center_x,
                center_y
            )

    return None