from selenium.webdriver import ActionChains

from  selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()

driver.switch_to.frame("iframeResult")

field1 = driver.find_element(By.XPATH,'//*[@id="field1"]')
field1.clear()
field1.send_keys("Aniket")

button = driver.find_element(By.XPATH,"/html/body/button")
act = ActionChains(driver)
act.double_click(button)
time.sleep(4)
