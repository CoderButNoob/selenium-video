from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(10)
# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()
#
# reg_link = Keys.CONTROL+Keys.RETURN
# driver.find_element(By.LINK_TEXT,'Register').send_keys(reg_link)
# time.sleep(5)

# # New Tab - Selenium4 : Opens new tab and switches to new tab
# driver.get("https://www.opencart.com/index.php?route=account/register&__cf_chl_tk=Vb8MGE_5JCWp4.y.10C9ELo4OPCAcnnb_dkhD.BDV40-1748431917-1.0.1.1-n0pY.nOOdaZfDIccayI5q0QDtBL0UYfew1O8nrGY7R4")
# driver.switch_to.new_window('tab')
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

## New Window - Selenium4 : Opens new browser window and switches to new window
driver.get("https://www.opencart.com/index.php?route=account/register&__cf_chl_tk=Vb8MGE_5JCWp4.y.10C9ELo4OPCAcnnb_dkhD.BDV40-1748431917-1.0.1.1-n0pY.nOOdaZfDIccayI5q0QDtBL0UYfew1O8nrGY7R4")
driver.switch_to.new_window('window')
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)