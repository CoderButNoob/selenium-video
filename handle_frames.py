from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/basic_auth")
driver.get("https://vinothqaacademy.com/iframe/")
driver.maximize_window()
driver.switch_to.frame('employeetable')
#checkbox = driver.find_element(By.XPATH,'//*[@id="myTable"]/tbody/tr[1]/td[1]/input')
checkbox = WebDriverWait(driver,10).until(EC.element_to_be_clickable((
                                                    By.XPATH,'//*[@id="myTable"]/tbody/tr[1]/td[1]/input')))
checkbox.click()
time.sleep(2)

driver.switch_to.default_content()

driver.switch_to.frame('popuppage')
driver.find_element(By.XPATH,'//*[@id="main"]/div[2]/div[1]/div/section[3]/div/div[1]/div/div/div/center/button').click()
alert_box = driver.switch_to.alert
print(alert_box.text)
alert_box.accept()
time.sleep(2)

driver.switch_to.default_content()
driver.switch_to.frame('registeruser')
driver.find_element(By.XPATH,'//*[@id="vfb-5"]').send_keys('Aniket')
time.sleep(2)

driver.close()

time.sleep(2)
# driver.switch_to.frame("")
# driver.find_element(By.LINK_TEXT,'WebDriver').click()
# time.sleep(2)
# driver.find_element(By.LINK_TEXT,'Help').click()