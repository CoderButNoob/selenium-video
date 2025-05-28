from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()
driver.maximize_window()
#driver.implicitly_wait(5)

driver.get("https://demo.nopcommerce.com/login")
#
# email = driver.find_element(By.XPATH, "//input[@id='Email']")
# email.clear()
# email.send_keys("sonar@gmail.com")
#
# driver.quit()

#-----------------------------------------------------------------------------------------------------------

wait = WebDriverWait(driver, 10, poll_frequency=2 , ignored_exceptions=[Exception])
email = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='Email']")))

email.clear()
email.send_keys("sonar@gmail.com")

driver.quit()