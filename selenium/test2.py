# from selenium import webdriver
# from selenium.webdriver.common.by import By

# # driver = webdriver.Chrome()
# # driver.get("https://opensource-demo.orangehrmlive.com/")

# # driver.find_element(By.NAME,"username").send_keys("Admin")
# # driver.find_element_by_name("password").send_keys("admin123")
# # driver.find_element_by_type("submit").click()

# # actual_title = driver.title
# # expected_title = "OrangeHRM"

# # if actual_title == expected_title:
# #     print("Login Passed")
# # else:
# #     print("Login Failed")

# # driver.close()

# driver = webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/")

# driver.find_element(By.NAME, "username").send_keys("Admin")
# driver.find_element(By.NAME, "password").send_keys("admin123")
# driver.find_element(By.XPATH, "//button[@type='submit']").click()  # no find_element_by_type

# actual_title = driver.title
# expected_title = "OrangeHRM"

# if actual_title == expected_title:
#     print("Login Passed")
# else:
#     print("Login Failed")

# driver.close()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")

# Wait until the username input is present
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))

# Now perform login
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Check the page title after login
actual_title = driver.title
expected_title = "OrangeHRM"
time.sleep(2)
if actual_title == expected_title:
    print("Login Passed")
else:
    print("Login Failed")

# driver.quit()
