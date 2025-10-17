import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def validData():
    driver  = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")

    userInput = driver.find_element(By.ID, "username")
    passInput = driver.find_element(By.ID, "password")

    login_btn = driver.find_element(By.CSS_SELECTOR, "button.radius")

    username = driver.find_element(By.XPATH, "//*[@id='content']/div/h4/em[1]").text
    #print(username)
    password = driver.find_element(By.XPATH, "//*[@id='content']/div/h4/em[2]").text
    #print(password)

    userInput.clear()
    passInput.clear()
    userInput.send_keys(username)
    passInput.send_keys(password)
    time.sleep(2)

    login_btn.click()
    time.sleep(2)

    check_messages = driver.find_element(By.ID, "flash").text.replace("×", "").strip() # uzima poruku i brise 'x' koji je visak
    #print(check_messages)

    assert check_messages == "You logged into a secure area!", "Login Test Fail! [Invalid data or message]"
    print("Login Test Passed!\n")

    #driver.find_element(By.XPATH, "//*[@id='content']/div/a/i").click()
    driver.quit()

def invalidData(uORp):
    if (uORp != "username" and uORp != "password"):
        return

    try:
        driver  = webdriver.Chrome()
        driver.get("https://the-internet.herokuapp.com/login")

        userInput = driver.find_element(By.ID, "username")
        passInput = driver.find_element(By.ID, "password")

        login_btn = driver.find_element(By.CSS_SELECTOR, "button.radius")

        username = driver.find_element(By.XPATH, "//*[@id='content']/div/h4/em[1]").text
        #print(username)
        password = driver.find_element(By.XPATH, "//*[@id='content']/div/h4/em[2]").text
        #print(password)

        userInput.clear()
        passInput.clear()

        if(uORp == "username"):
            userInput.send_keys("invalidName")
            passInput.send_keys(password)

        elif (uORp == "password"):
            userInput.send_keys(username)
            passInput.send_keys("invalidPass")
        time.sleep(2)

        login_btn.click()
        time.sleep(2)

        check_messages = driver.find_element(By.ID, "flash").text.replace("×", "").strip()
        #print(check_messages)


        assert check_messages == "Your username is invalid!", "Login Test Fail! [Invalid password]"

        assert check_messages == "Your password is invalid!", "Login Test Fail! [Invalid username]"

        print("Login Test Failed!\n")

    except AssertionError as e:

        print(str(e))
        driver.save_screenshot("invalid_login_fail.png")
        print("Test Failed, screenshot saved!\n")

    finally:
        driver.quit()

validData()
invalidData(2)
invalidData("username")
invalidData("password")
