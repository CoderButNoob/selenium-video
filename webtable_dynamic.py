from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.NAME,'username').send_keys("Admin")
driver.find_element(By.NAME,'password').send_keys("admin123")
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
time.sleep(3)

#Admin-->user management-->users
driver.find_element(By.XPATH,"//span[normalize-space()='Admin']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//span[normalize-space()='Admin']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//span[normalize-space()='Admin']").click()
time.sleep(1)

#total number of rows
noOfRows = driver.find_elements(By.XPATH,"//div[@class='oxd-table-card']")
print(len(noOfRows))

count = 0
for row in noOfRows:
    status = row.find_element(By.XPATH,".//div[@role='cell'][5]").text
    if status == "Enabled":
        count = count+1

print("Total Number of users ",len(noOfRows))
print("Number of Enabled users ",count)
print("Number of Disabled users ", (len(noOfRows)-count))

driver.close()