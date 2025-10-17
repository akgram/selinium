import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver  = webdriver.Chrome()
driver.get("https://demoqa.com/checkbox")

checkBox = driver.find_element(By.CLASS_NAME, "rct-checkbox")

input = driver.find_element(By.XPATH, "//input[@id='tree-node-home']") 

print("Checkbox displayed:", checkBox.is_displayed())
print("Checkbox enabled:", checkBox.is_enabled())
print("Checkbox selected:", input.is_selected())

if not input.is_selected():
    checkBox.click()
    time.sleep(2)
    print("Checkbox is selected now.")
else:
    print("Checkbox is already selected.")

driver.quit()