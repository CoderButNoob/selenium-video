from selenium.webdriver import ActionChains

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

min_slider = driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[1]')
max_slider = driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[2]')

print("Location of slider before moving...")
print(min_slider.location) #{'x': 59, 'y': 256}
print(max_slider.location) #{'x': 613, 'y': 256}

act = ActionChains(driver)
act.drag_and_drop_by_offset(min_slider,100,0).perform()
act.drag_and_drop_by_offset(max_slider,-13,0).perform()
print("Location of slider after moving...")
print(min_slider.location) #{'x': 59, 'y': 256}
print(max_slider.location)