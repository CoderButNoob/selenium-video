from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()

#is_displayed   is_enabled
search_box = driver.find_element(By.XPATH,'//*[@id="small-searchterms"]')
print("Display Status:",search_box.is_displayed())
print("Enable Status:",search_box.is_enabled())

#is_selected --- for radio button and check-box
male_select = driver.find_element(By.XPATH,'//*[@id="gender-male"]')
female_select = driver.find_element(By.XPATH, '//*[@id="gender-female"]')
male_select.click()
print(female_select.is_selected())
print(male_select.is_selected())



