from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.NAME,'username').send_keys("Admin")
driver.find_element(By.NAME,'password').send_keys("admin123")
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
time.sleep(3)

#Admin-->user management-->users
admin = driver.find_element(By.XPATH,"//span[normalize-space()='Admin']")
user_management = driver.find_element(By.XPATH,"//span[normalize-space()='Admin']")
users = driver.find_element(By.XPATH,"//span[normalize-space()='Admin']")

#MouseHover
act  = ActionChains(driver)
act.move_to_element(admin).move_to_element(user_management).move_to_element(users).click().perform()
time.sleep(5)