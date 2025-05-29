from selenium import  webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

#opens alert window
driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[3]/button').click()

alert_window = driver.switch_to.alert
print(alert_window.text)
alert_window.send_keys("Welcome")
#click OK button
# alert_window.accept()
#clcik CANCEL button
alert_window.dismiss()

time.sleep(2)
