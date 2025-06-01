from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
time.sleep(2)

#scroll the page by pixel number
# driver.execute_script("window.scrollBy(0,3000)","")
# time.sleep(3)
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of pixels moved:",value)

#scroll the page till element is visible
# flag =  driver.find_element(By.XPATH,'//*[@id="ct-list"]/table[1]/tbody/tr[86]/td[1]/img')
# driver.execute_script("arguments[0].scrollIntoView();",flag)
# time.sleep(2)
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of Pixels moved",value)

#scroll the page till end of page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of Pixels moved",value)
time.sleep(5)

#scroll up to start
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
time.sleep(2)
value = driver.execute_script("return window.pageYOffset;")
print("Number of Pixels moved",value)