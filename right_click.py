from selenium.webdriver import ActionChains

from  selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

button = driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
act = ActionChains(driver)
act.context_click(button).perform() #right click
time.sleep(5)
