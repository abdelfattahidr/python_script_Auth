from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

conection_to_website = webdriver.Chrome()
conection_to_website.get("url")
email_field = conection_to_website.find_element("name", "email")  # input name
password_field = conection_to_website.find_element("name", "password")  # input name
submit_button = conection_to_website.find_element("xpath", "//button[@type='submit']")  # button type

email_field.send_keys("your_email_adresse")
password_field.send_keys("your_password")
submit_button.click()

time.sleep(100)
