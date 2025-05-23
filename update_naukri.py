import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
options = Options()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Navigate to Naukri login page
    driver.get("https://www.naukri.com/nlogin/login")
    driver.implicitly_wait(10)

    # Login to Naukri
    email = os.getenv("NAUKRI_EMAIL")
    password = os.getenv("NAUKRI_PASSWORD")
    email_element = driver.find_element(By.ID, "usernameField")
    email_element.send_keys(email)
    password_element = driver.find_element(By.ID, "passwordField")
    password_element.send_keys(password)
    password_element.send_keys(Keys.RETURN)
    time.sleep(5)  # Wait for login to complete

    # Navigate to profile page
    driver.get("https://www.naukri.com/mnjuser/profile")
    driver.implicitly_wait(10)

    # Click on 'Edit' button for resume headline
    edit_button = driver.find_element(By.XPATH, "//span[text()='Edit']")
    edit_button.click()
    time.sleep(2)

    # Update resume headline
    headline_input = driver.find_element(By.XPATH, "//textarea[@name='resumeHeadline']")
    new_headline = "Updated Resume Headline - " + time.strftime("%Y-%m-%d %H:%M:%S")
    headline_input.clear()
    headline_input.send_keys(new_headline)
    headline_input.send_keys(Keys.RETURN)
    time.sleep(2)

    print("Resume headline updated successfully!")

finally:
    driver.quit()
