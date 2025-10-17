from selenium import webdriver

driver  = webdriver.Chrome()
driver.get("https://example.com")

exp_title = "Example Domain"

assert driver.title == exp_title, f"Expected title: {exp_title} \nBut title is: {driver.title}!"

print("Test Title Passed!")

driver.quit()