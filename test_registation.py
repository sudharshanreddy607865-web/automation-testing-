
from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path
import time

# Open Chrome browser
driver = webdriver.Chrome()

# Open registration form
file_path = Path("index.html").resolve().as_uri()
driver.get(file_path)

driver.maximize_window()


def clear_form():
    fields = ["name", "email", "phone",
              "password", "confirmPassword"]

    for field in fields:
        driver.find_element(By.ID, field).clear()


def enter_details(name, email, phone, password, confirm):
    driver.find_element(By.ID, "name").send_keys(name)
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "phone").send_keys(phone)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "confirmPassword").send_keys(confirm)


def submit_form():
    driver.find_element(By.ID, "submit").click()
    time.sleep(0.5)


def check_result(element_id):
    return driver.find_element(By.ID, element_id).text


# TEST CASE 1: Empty name
clear_form()
enter_details("", "test@gmail.com", "9876543210",
              "password123", "password123")
submit_form()

print("Test 1 - Empty Name:",
      check_result("nameError"))


# TEST CASE 2: Invalid email
clear_form()
enter_details("Ganesh", "invalidemail", "9876543210",
              "password123", "password123")
submit_form()

print("Test 2 - Invalid Email:",
      check_result("emailError"))


# TEST CASE 3: Invalid phone number
clear_form()
enter_details("Ganesh", "test@gmail.com", "12345",
              "password123", "password123")
submit_form()

print("Test 3 - Invalid Phone:",
      check_result("phoneError"))


# TEST CASE 4: Short password
clear_form()
enter_details("Ganesh", "test@gmail.com", "9876543210",
              "123", "123")
submit_form()

print("Test 4 - Short Password:",
      check_result("passwordError"))


# TEST CASE 5: Password mismatch
clear_form()
enter_details("Ganesh", "test@gmail.com", "9876543210",
              "password123", "password456")
submit_form()

print("Test 5 - Password Mismatch:",
      check_result("confirmError"))


# TEST CASE 6: Valid registration
clear_form()
enter_details("Ganesh", "test@gmail.com", "9876543210",
              "password123", "password123")
submit_form()

print("Test 6 - Valid Registration:",
      check_result("success"))

time.sleep(3)

# Close browser
driver.quit()
