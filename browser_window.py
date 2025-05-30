from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
# window_id = driver.current_window_handle
# print(window_id) #32E00568309158EBB979509801AF7A32
#                  #46056CB1C954C73EB48D29CB1545432A

link = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.LINK_TEXT,'OrangeHRM, Inc')))
link.click()
window_ids = driver.window_handles

#Approach 1 (only if one or 2 window browsers are available)
# parent_windowID = window_ids[0]
# child_windowID = window_ids[1]
# print(parent_windowID,child_windowID)
#
# driver.switch_to.window(child_windowID)
# print("Title of Child window --> ",driver.title)
#
# driver.switch_to.window(parent_windowID)
# print("Title of Parent window --> ",driver.title)
# time.sleep(5)
# driver.close()

#Appraoch 2 (multiple browser windows)

# for winID in window_ids:
#     driver.switch_to.window(winID)
#     print(driver.title, winID)


#closing browser window based upon choice
for winID in window_ids:
    driver.switch_to.window(winID)
    if driver.title ==  "Human Resources Management Software | OrangeHRM HR Software":
        time.sleep(2)
        driver.close()
