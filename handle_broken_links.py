from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import  time
import requests as requests

driver = webdriver.Chrome()
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

all_links = driver.find_elements(By.TAG_NAME,'a')
count = 0

for link in all_links:
    url = link.get_attribute('href')
    try:
        res = requests.head(url)
    except:
        None
    if res.status_code>=400:
        print(url, " is broken link")
        count+=1
    else:
        print(url, " is valid link")

print("total no of broken links:",count)