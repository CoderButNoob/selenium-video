# from selenium import webdriver

# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.keys import Keys
# import  time
# import  random
#
# driver = webdriver.Chrome()
#
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#
#
# block = driver.find_elements(By.CLASS_NAME,"block large-row-spacer")
# print(len(block))

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
import time
time.sleep(2)
driver.maximize_window()
try:
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    time.sleep(2)
    driver.maximize_window()

    sliders = driver.find_elements(By.CLASS_NAME, "block large-row-spacer")
    print(len(sliders))

except Exception as e:
    print("Error:", e)
finally:
    driver.quit()
