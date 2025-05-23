
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def main():
    options = Options()
    options.add_argument("--headless=new")  # Use new headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-software-rasterizer")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    wait = WebDriverWait(driver, 20)

    try:
        email = os.getenv("NAUKRI_EMAIL")
        password = os.getenv("NAUKRI_PASSWORD")

        if not email or not password:
            raise ValueError("Missing NAUKRI_EMAIL or NAUKRI_PASSWORD environment variables")

        driver.get("https://www.naukri.com/nlogin/login")

        email_element = wait.until(EC.presence_of_element_located((By.ID, "usernameField")))
        email_element.send_keys(email)

        password_element = wait.until(EC.presence_of_element_located((By.ID, "passwordField")))
        password_element.send_keys(password)
        password_element.send_keys(Keys.RETURN)

        wait.until(EC.url_contains("naukri.com"))

        driver.get("https://www.naukri.com/mnjuser/profile")

        edit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Edit']")))
        edit_button.click()

        headline_input = wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@name='resumeHeadline']")))
        new_headline = "Updated Resume Headline - " + time.strftime("%Y-%m-%d %H:%M:%S")
        headline_input.clear()
        headline_input.send_keys(new_headline)
        headline_input.send_keys(Keys.RETURN)

        print("✅ Resume headline updated successfully.")

    except Exception as e:
        print("❌ An error occurred:", e)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
