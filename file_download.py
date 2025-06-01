from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import  By
import time

def chrome_setup():
    driver = webdriver.Chrome()
    return driver

driver = chrome_setup()
driver.get("https://filesamples.com/formats/doc")
driver.maximize_window()

wait = WebDriverWait(driver,20)
download_link = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/main/div[3]/div[1]/div/div[2]/a')))
download_link.click()
time.sleep(3)
