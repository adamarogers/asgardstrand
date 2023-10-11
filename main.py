# Web form remote submit program

# Import packages
from selenium import webdriver  # Import selenium to communicate with HTML
from selenium.webdriver.common.by import By  # Get Chrome browser kit
import time  # Allows waiting for form submission

# Load drivers and website
driver = webdriver.Chrome()  # Load Chrome
driver.get("https://nettskjema.no/a/testautofill")  # Load website
driver.implicitly_wait(0.5)  # Wait for website to load before acting

# Get HTML elements
question_1_response_radio = driver.find_element(by=By.ID, value="14011896")  # Get question buttons
send_button = driver.find_element(by=By.ID, value="submit-form")  # Get submit button

# Interact with HTML elements
question_1_response_radio.click()  # Click answers
send_button.click()  # Submit
time.sleep(2)  # Wait to allow form to be submitted

driver.quit()  # Close connection
