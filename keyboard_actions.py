# Ctrl + A
# Ctrl + c
# Tab
# Ctrl + V
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://text-compare.com/")
driver.maximize_window()

text_area1 = driver.find_element(By.XPATH,'//*[@id="inputText1"]')
text_area2 = driver.find_element(By.XPATH,'//*[@id="inputText2"]')
text_area1.clear()
text_area1.send_keys("Hello I am Aniket")
act = ActionChains(driver)

#text_area1 --> Ctrl + A select the text
# act.key_down(Keys.CONTROL)
# act.send_keys('a')
# act.key_up(Keys.CONTROL)
# act.perform()
act.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()  #ctrl + a action
time.sleep(1)
#text_area1 --> Ctrl+C Copy text
act.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
time.sleep(1)

#tab key
act.send_keys(Keys.TAB).perform()
time.sleep(1)

#text_area2 --> Ctrl+V Paste the text
act.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
time.sleep(1)

