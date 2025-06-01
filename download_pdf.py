from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import  By
import time

def chrome_setup():
    prefernces = {"plugins.always_open_pdf_externally":True}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",prefernces)
    driver = webdriver.Chrome(options=ops)
    return driver

driver = chrome_setup()

driver.get("https://filesamples.com/formats/pdf")
driver.maximize_window()
time.sleep(2)

wait = WebDriverWait(driver,20)
download_link = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/main/div[3]/div[1]/div/div[1]/a')))
# Scroll to the element to avoid iframe interception
driver.execute_script("arguments[0].scrollIntoView(true);", download_link)
time.sleep(1)

# Click using JavaScript (to bypass iframe/ad issues)
driver.execute_script("arguments[0].click();", download_link)

time.sleep(3)