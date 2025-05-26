# 🧪 Selenium Automation Practice with Python

This repository contains my **hands-on practice scripts** using **Selenium WebDriver with Python**.  
These scripts cover a wide range of browser automation tasks like form submissions, UI element handling, XPath operations, and real-world validations on popular websites.

---

## 🧰 Technologies Used

- **Language**: Python  
- **Browser**: Google Chrome  
- **Library**: Selenium WebDriver  
- **Driver Path**: `C:\Drivers\chromedriver-win64\chromedriver.exe`  
- **IDE**: PyCharm / VS Code

---

## 📂 Project Overview

Here’s a breakdown of the **practical automation projects** I’ve worked on:

### 1. 🔐 Login Automation
- **Website**: [OrangeHRM Demo](https://opensource-demo.orangehrmlive.com/)
- **Actions**:
  - Inputs username and password
  - Submits the login form
  - Validates successful login by checking page title

---

### 2. 🛒 E-commerce Interaction
- **Website**: [NopCommerce Demo](https://demo.nopcommerce.com/)
- **Actions**:
  - Searches for a product (e.g., *iPhone 16*)
  - Navigates to the Registration page
  - Uses various locators like `By.NAME`, `By.LINK_TEXT`, `By.ID`

---

### 3. 📊 UI Element Count
- **Website**: [Automation Exercise](https://automationexercise.com/)
- **Actions**:
  - Counts the number of dropdown panels using `By.CLASS_NAME`
  - Demonstrates use of `find_elements()`

---

### 4. 👤 Facebook Login Simulation
- **Website**: [Facebook](https://facebook.com/)
- **Actions**:
  - Fills in dummy email and password
  - Uses `By.CSS_SELECTOR` for element selection
  - Highlights form interaction using CSS locators

---

### 5. 🔍 Search Box Interaction
- **Website**: [NopCommerce - Apparel Page](https://demo.nopcommerce.com/apparel-shoes)
- **Actions**:
  - Enters product name into search input
  - Clicks using XPath with parent-child relationship
  - Demonstrates relative XPath and XPath axes

---

## 💡 What I’ve Learned

- ✅ Locators:
  - `By.ID`, `By.NAME`, `By.XPATH`, `By.CSS_SELECTOR`, `By.LINK_TEXT`
- ✅ XPath Techniques:
  - Relative XPath vs Absolute XPath
  - XPath functions: `contains()`, `starts-with()`, `text()`
  - XPath axes: `child::`, `parent::`, `following::`, `ancestor::`
- ✅ Waits and Synchronization:
  - `WebDriverWait` with `expected_conditions`
  - `time.sleep()` for simple pauses (only when necessary)
- ✅ Browser Control:
  - `driver.get()`, `driver.close()`, `driver.quit()`
  - Navigation: `driver.back()`, `driver.forward()`, `driver.refresh()`
- ✅ Real-World Testing:
  - Interacted with real websites for hands-on learning
  - Dealt with dynamic elements, slow loading, and structural variations

---


