from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import re
import time


# -----------------------------
# CREATE DRIVER FUNCTION
# -----------------------------
def create_driver():

    chrome_options = Options()

    # REMOVE headless for debugging
    # chrome_options.add_argument("--headless")

    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    return driver


# -----------------------------
# START DRIVER
# -----------------------------
driver = create_driver()

driver.get("https://www.google.com")


# -----------------------------
# CHECK BROWSER STATUS
# -----------------------------
def is_browser_alive():
    global driver

    try:
        driver.title
        return True

    except:
        return False


# -----------------------------
# RESTART BROWSER
# -----------------------------
def restart_browser():
    global driver

    try:
        driver.quit()
    except:
        pass

    print("Restarting Browser...")

    driver = create_driver()

    driver.get("https://www.google.com")


# -----------------------------
# SEARCH FUNCTION
# -----------------------------
def search_brain(text):

    global driver

    try:

        # CHECK IF BROWSER IS DEAD
        if not is_browser_alive():
            restart_browser()

        # FIND SEARCH BOX
        search_box = driver.find_element(By.NAME, "q")

        # CLEAR OLD TEXT
        search_box.clear()

        # TYPE QUERY
        search_box.send_keys(text)

        # PRESS ENTER
        search_box.send_keys(Keys.RETURN)

        # WAIT
        time.sleep(2)

        # FIRST RESULT
        first_result = driver.find_element(By.CSS_SELECTOR, "div.g")

        # EXTRACT TEXT
        first_result_text = first_result.text

        sentences = re.split(r'(?<=[.!?])\s', first_result_text)

        # REMOVE LINKS / DATES
        filtered_sentences = [
            sentence
            for sentence in sentences
            if not re.search(
                r'https?://\S+|(\d{1,2} [A-Za-z]+ \d{4})',
                sentence
            )
        ]

        result_text = ". ".join(filtered_sentences[:5])

        result_text = result_text.replace(
            "Featured snippet from the web",
            ""
        )

        return result_text

    except Exception as e:

        print("Search Error:", e)

        restart_browser()

        return "Sorry sir, browser crashed and restarted."


# -----------------------------
# TEST
# -----------------------------
while True:

    query = input("Enter Search: ")

    if query.lower() == "exit":
        break

    answer = search_brain(query)

    print("\nResult:\n")
    print(answer)