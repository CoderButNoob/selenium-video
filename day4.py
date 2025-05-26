from selenium import  webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://money.rediff.com/gainers")
driver.maximize_window()
time.sleep(2)

#self
# text_msg = driver.find_element(By.XPATH,"//a[contains(text(),'Reliance Power')]/self::a").text
# print(text_msg)

#parent
# text_msg = driver.find_element(By.XPATH,"//a[contains(text(),'Reliance Power')]/parent::td").text
# print(text_msg)

# #child
# child = driver.find_elements(By.XPATH,"//a[contains(text(),'Reliance Power')]/ancestor::tr/child::td")
# print(len(child))
#
# #ancestor
# text_msg = driver.find_element(By.XPATH,"//a[contains(text(),'Reliance Power')]/ancestor::tr").text
# print(text_msg)

#descendant
# descendant = driver.find_elements(By.XPATH,"//a[contains(text(),'Reliance Power')]/ancestor::tr/descendant::*")
# print(len(descendant))

#following
# following = driver.find_elements(By.XPATH,"//a[contains(text(),'Reliance Power')]/ancestor::tr/following::*")
# print(len(following))

#following-sibling
# following_sibling = driver.find_elements(By.XPATH,"//a[contains(text(),'Reliance Power')]/ancestor::tr/following-sibling::*")
# print(len(following_sibling))

#preceding
# precedings = driver.find_elements(By.XPATH,"//a[contains(text(),'Reliance Power')]/ancestor::tr/preceding::*")
# print(len(precedings))

#preceding-sibling
preceding_sibling = driver.find_elements(By.XPATH,"//a[contains(text(),'Reliance Power')]/ancestor::tr/preceding-sibling::*")
print(len(preceding_sibling))
