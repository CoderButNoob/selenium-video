from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#capture cookies from browser
cookies = driver.get_cookies()
print("Length of cookies",len(cookies))

#print details of cookies
# for cookie in cookies:
#     print(cookie.get('name'),":",cookie.get('value'))

#add cookie to browser
driver.add_cookie({"name":"MyCookie","value":"12345678"})
cookies = driver.get_cookies()
print("Length of cookies after new add",len(cookies))

#delete specific cookie from browser
driver.delete_cookie("MyCookie")
cookies = driver.get_cookies()
print("Length of cookies after deletetion",len(cookies))

#delete all cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print("Length of cookies after deletetion",len(cookies))
