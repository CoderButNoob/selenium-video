from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://snapdeal.com/")
driver.get("https://www.amazon.in/")

driver.back()
time.sleep(1)
driver.forward()
time.sleep(1)
driver.refresh()
driver.quit()
