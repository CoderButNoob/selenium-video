import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# #check specific checkbox
# checkbox = driver.find_element(By.XPATH,'//*[@id="checkBoxOption1"]')
# checkbox.click()

#check all checkboxes
checkboxes = driver.find_elements(By.XPATH,'//input[@type="checkbox" and contains(@id,"checkBoxOption")]')
print(len(checkboxes))
for checkbox in checkboxes:
    checkbox.click()
time.sleep(1)

#check  last 2 checkbox
# for i in range(len(checkboxes)-2,len(checkboxes)):
#     checkboxes[i].click()

#check first2 checkbox
# for i in range(len(checkboxes)):
#     if i < 2:
#         checkboxes[i].click()

#clear all checkbox
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()
time.sleep(2)
