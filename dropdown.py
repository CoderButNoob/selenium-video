import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")
driver.maximize_window()

# drpcountry_ele = driver.find_element(By.XPATH,'//*[@id="input-country"]')
drpcountry = Select(driver.find_element(By.XPATH,'//*[@id="post-2646"]/div[2]/div/div/div/p/select'))

#select option from dropdown
# drpcountry.select_by_visible_text("Anguilla")
# time.sleep(2)
#
# drpcountry.select_by_value("ARM")
# drpcountry.select_by_index(15)

#capture all the options and print them
all_options = drpcountry.options
print("Total No of options ", len(all_options))

for option in all_options:
    print(option.text)

#select option from dropdown without built in func
for option in all_options:
    if option.text == "India":
        option.click()
        break


time.sleep(2)
