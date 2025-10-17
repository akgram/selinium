import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver  = webdriver.Chrome()
driver.get("https://demoqa.com/dynamic-properties")

exWait = WebDriverWait(driver, 5)
btn = exWait.until(expected_conditions.element_to_be_clickable((By.ID, "enableAfter")))

driver.execute_script("arguments[0].scrollIntoView(true);", btn)
time.sleep(2)

btn.click()
print("Button clicked.\nTest Passed!")

driver.quit()