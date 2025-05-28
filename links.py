from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import  time

driver =  webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
wait = WebDriverWait(driver,10)

#click on link
# driver.find_element(By.LINK_TEXT,'Digital downloads').click()

#find no of links in page
links = driver.find_elements(By.TAG_NAME,'a')
print("Total no. of links",len(links))
for link in links:
    print(link.text)

