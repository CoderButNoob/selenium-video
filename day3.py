from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(1)

#Absolute xpath
# search_box = driver.find_element(By.XPATH,"/html/body/div[6]/div[1]/div[2]/div[2]/form/input")
# search_box.send_keys("Dell")

#and
# search_box = driver.find_element(By.XPATH,"//input[@type='text' and @name='q']")
# search_box.send_keys("Dell")

#or
search_box = driver.find_element(By.XPATH,"//input[@type='text' or @name='q']")
search_box.send_keys("Dell")

#contains --- ISSUE
# search_box = driver.find_element(By.XPATH,"//input[contains (@name,'q')]")
# search_box.send_keys("Dell")



#relative xpath
# search_click = driver.find_element(By.XPATH,"//*[@id='small-search-box-form']/button")
# search_click.click()

##starts-with
# search_click = driver.find_element(By.XPATH,"//button[starts-with(@type,'submit')]")
# time.sleep(1)
# search_click.click()

#text()
search_click = driver.find_element(By.XPATH,"//button[text()='Search']")
time.sleep(1)
search_click.click()

time.sleep(1)

