from selenium import webdriver
from selenium.webdriver.common.by import By

driver  = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/html_tables.asp")


names = []
for i in range(2, 7):
    name = driver.find_element(By.XPATH, f"//*[@id='customers']/tbody/tr[{i}]/td[1]").text
    names.append(name)

print(names, "\n")
assert "Island Trading" in names, "Test Fail! [Island Trading NOT present]"

print("Island Trading is present.\nTest Passed!")

