from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://web.telegram.org/a/")
sleep(15)

driver.find_element(By.XPATH , '//*[@id="auth-qr-form"]/div/button').click()
sleep(2)

driver.find_element(By.XPATH , '//*[@id="sign-in-phone-number"]').clear() # Clear the number field
driver.find_element(By.XPATH , '//*[@id="sign-in-phone-number"]').send_keys(input("Please write your number with code countery like this : +989125201234")) #input the number
sleep(5)

driver.find_element(By.XPATH , '//*[@id="auth-phone-number-form"]/div/form/button[1]/div').click() #click on the next button
sleep(15)

# Insert the code from telegram ↓
driver.find_element(By.XPATH , '//*[@id="sign-in-code"]').send_keys(input('Pleas enter the code was sended for you: '))
sleep(3)

driver.find_element(By.XPATH , '//*[@id="sign-in-password"]').send_keys(input('Please enter your password in telegram: '))
sleep(1)

# Click on the next button and login ↓
driver.find_element(By.XPATH , '//*[@id="auth-password-form"]/div/form/button/div').click()
sleep(20)

# Click on the menu buttton ↓
driver.find_element(By.XPATH , '//*[@id="LeftMainHeader"]/div[1]/button/div[2]').click()
sleep(2)

# Click on the Setting button ↓
driver.find_element(By.XPATH , '//*[@id="LeftMainHeader"]/div[1]/div/div[2]/div[4]').click()
sleep(2)

# Click on the Privacy and Security button ↓
driver.find_element(By.XPATH , '//*[@id="Settings"]/div/div[2]/div[1]/div[7]/div').click()
sleep(2)

# Click on the Blocked Users button ↓
driver.find_element(By.XPATH , '//*[@id="Settings"]/div[2]/div[2]/div[1]/div[1]/div').click()
sleep(2)

# Click on the us3rs ↓
client = driver.find_elements(By.CLASS_NAME , 'ripple-container')
for i in client:
    driver.find_element(By.XPATH , '//*[@id="Settings"]/div[3]/div[2]/div/div[2]/div/div[1]/div/div[1]').click()
    sleep(2)
    
    # Click on the unblock button 
    driver.find_element(By.XPATH , '//*[@id="Settings"]/div[3]/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div').click()
    sleep(5)
