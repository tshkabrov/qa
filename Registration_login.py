import time
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
driver.maximize_window()

# #регистрация в системе
# driver.get("https://practice.automationtesting.in/")
# time.sleep(1)
#
# btn = driver.find_element(By.CSS_SELECTOR, "[href='https://practice.automationtesting.in/my-account/']")
# btn.click()
# time.sleep(2)
#
# email = driver.find_element(By.ID, "reg_email")
# emailsave = "tshkabrov@gmail.com"
# email.send_keys(emailsave)
#
# password = driver.find_element(By.ID, "reg_password")
# passwordsave = "p6Tv01TZ4P1u"
# password.send_keys(passwordsave)
# time.sleep(1)
#
# register = driver.find_element(By.CSS_SELECTOR, "[name='register']")
# register.click()

#логин в систему
driver.get("https://practice.automationtesting.in/")
time.sleep(1)

btn = driver.find_element(By.CSS_SELECTOR, "[href='https://practice.automationtesting.in/my-account/']")
btn.click()
time.sleep(2)

email = driver.find_element(By.ID, "username")
email.send_keys("tshkabrov@gmail.com")

password = driver.find_element(By.ID, "password")
password.send_keys("p6Tv01TZ4P1u")

login = driver.find_element(By.CSS_SELECTOR, "[name='login']")
login.click()
time.sleep(3)

islogout = driver.find_element(By.LINK_TEXT, "Sigh Out")
islogouttext = islogout.text
assert islogouttext == "Sign out"
time.sleep(3)