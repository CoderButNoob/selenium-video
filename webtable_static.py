# 1. Read number of rows and cols
# 2. Read specific row and col data
# 3. Read all row and col data
# 4. Read data based on conditions(List book name whose author is Mukesh)

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# 1. Read number of rows and cols
rows =  driver.find_elements(By.XPATH,'//table[@name="BookTable"]/tbody/tr')
print("No of rows -> ",len(rows))

cols = driver.find_elements(By.XPATH,'//table[@name="BookTable"]/tbody/tr/th')
print("No of cols -> ",len(cols))


# 2. Read specific row and col data
data = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[1]")
print(data.text)

# 3. Read all row and col data
# print("Printing all the rows and cols data")
#
# for r in range(2,len(rows)+1):
#     for c in range(1,len(cols)+1):
#         data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]")
#         print(data.text,end='              ')
#     print()

# 4. Read data based on conditions(List book name whose author is Mukesh)
for r in range(2,len(rows)+1):
    author_name = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if author_name == 'Mukesh':
        book_name = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text
        print(book_name,"    ",author_name,"     ",price)
    print()


