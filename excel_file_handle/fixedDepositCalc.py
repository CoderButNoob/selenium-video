from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from excel_file_handle import xlutils
import time

# Setup WebDriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()

# File path and sheet name
file = "C:/Users/anike/Downloads/Investment_Report.xlsx"
sheet_name = "InvestmentData"

# Read number of rows
rows = xlutils.getRowCount(file, sheet_name)

# Loop through each row
for r in range(2, rows + 1):
    # Reading data from Excel
    principal = xlutils.readData(file, sheet_name, r, 1)
    roi = xlutils.readData(file, sheet_name, r, 2)
    period = xlutils.readData(file, sheet_name, r, 3)
    freq = xlutils.readData(file, sheet_name, r, 4)
    type = xlutils.readData(file, sheet_name, r, 5)
    exp_maturity_val = xlutils.readData(file, sheet_name, r, 6)

    # Passing data to the application
    driver.find_element(By.ID, 'principal').send_keys(principal)
    driver.find_element(By.ID, 'interest').send_keys(roi)
    driver.find_element(By.ID, 'tenure').send_keys(period)

    period_drp = Select(driver.find_element(By.NAME, 'tenurePeriod'))
    period_drp.select_by_visible_text(freq)

    frequency = Select(driver.find_element(By.NAME, 'frequency'))
    frequency.select_by_visible_text(type)

    driver.find_element(By.XPATH, '//*[@id="fdMatVal"]/div[2]/a[1]/img').click()

    # Get result
    actual_maturity_val = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text

    # Validation
    if round(float(exp_maturity_val), 2) == round(float(actual_maturity_val), 2):
        print(f"Row {r} - Test Passed")
        xlutils.writeData(file, sheet_name, r, 8, "Pass")
        xlutils.fillGreenColor(file, sheet_name, r, 8)
    else:
        print(f"Row {r} - Test Failed | Expected: {exp_maturity_val}, Actual: {actual_maturity_val}")
        xlutils.writeData(file, sheet_name, r, 8, "Fail")
        xlutils.fillRedColor(file, sheet_name, r, 8)

    # Clear all fields before next input
    driver.find_element(By.XPATH, '//*[@id="fdMatVal"]/div[2]/a[2]/img').click()
    time.sleep(2)

driver.close()
