import time

from selenium import webdriver
from selenium.webdriver.common.by import By

ops = webdriver.ChromeOptions()
ops.add_argument('--disable-notifications')

driver = webdriver.Chrome(options=ops)

driver.get('https://whatmylocation.com/')
driver.maximize_window()
time.sleep(2)