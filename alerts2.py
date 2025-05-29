from selenium import  webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://mypage.rediff.com/login/dologin")

driver.find_element(By.XPATH,'//*[@id="pass_div"]/input[3]').click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(1)

driver.close()


