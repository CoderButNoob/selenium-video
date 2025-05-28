from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
#application commands
# print(driver.title)
# print(driver.current_url)
# print(driver.page_source)

#browser commands
link = driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc")
time.sleep(1)
link.click()
time.sleep(5)
# driver.close()
driver.quit()
time.sleep(2)