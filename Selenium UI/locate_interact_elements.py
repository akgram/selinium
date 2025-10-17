import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver  = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")

name = "Aleksandar Krstic"
email = "primer@gmail.com"
cAdr = "adresa123"
pAdr = "adresa456"

driver.find_element(By.ID, "userName").send_keys(name)
driver.find_element(By.CSS_SELECTOR, "#userEmail").send_keys(email)
driver.find_element(By.CSS_SELECTOR, "#currentAddress").send_keys(cAdr)
driver.find_element(By.XPATH, "//*[@id='permanentAddress']").send_keys(pAdr)
time.sleep(2)
sub_btn = driver.find_element(By.XPATH, "//*[@id='submit']")

driver.execute_script("arguments[0].scrollIntoView(true);", sub_btn) #skroluje dok btn ne bude vidljiv, zbog reklama...
time.sleep(2)
sub_btn.click()

output_name = driver.find_element(By.ID, "name").text
output_email = driver.find_element(By.ID, "email").text
output_cAdr = driver.find_element(By.ID, "currentAddress").get_attribute("value")
output_pAdr = driver.find_element(By.ID, "permanentAddress").get_attribute("value")

assert name in output_name, "Test Fail! [name error]"
print("Test Name Passed!")

assert email in output_email, "Test Fail! [email error]"
print("Test Email Passed!")

assert cAdr in output_cAdr, "Test Fail! [current Address error]"
print("Test cAddress Passed!")

assert pAdr in output_pAdr, "Test Fail! [permanent Address error]"
print("Test pAddress Passed!")

driver.quit()

