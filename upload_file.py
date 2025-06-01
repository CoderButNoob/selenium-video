from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import  By
import time

driver = webdriver.Chrome()
driver.get("https://ps.uci.edu/~franklin/doc/file_upload.html")
driver.find_element(By.NAME,"userfile").send_keys("C:/Users/anike/Downloads/sample3.pdf")
time.sleep(3)