from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/basic_auth")
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.find_element(By.XPATH,'/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a').click()

# switch_to.frame(webelement)
outer_frame = driver.find_element(By.XPATH,'//*[@id="Multiple"]/iframe')
driver.switch_to.frame(outer_frame)

inner_iframe  = driver.find_element(By.XPATH,'/html/body/section/div/div/iframe')
driver.switch_to.frame(inner_iframe)

driver.find_element(By.XPATH,'/html/body/section/div/div/div/input').send_keys('Aniket')

driver.switch_to.parent_frame()
time.sleep(2)

