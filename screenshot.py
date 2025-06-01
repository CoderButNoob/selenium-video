from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# driver.save_screenshot("C:\\Users\\anike\\OneDrive\\Desktop\\selenium_screenshot\\homepage.png")
driver.get_screenshot_as_file("C:\\Users\\anike\\OneDrive\\Desktop\\selenium_screenshot\\homepage_file.png")
driver.quit()