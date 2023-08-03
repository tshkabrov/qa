import time
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By

#открываетм сайт
driver.get("https://practice.automationtesting.in/")
time.sleep(2)
driver.execute_script("window.scrollBy(0, 600);")

#находим продукт
btn = driver.find_element(By.CLASS_NAME, "woocommerce-LoopProduct-link")
btn.click()
time.sleep(2)

#проставляем пятерку
btn = driver.find_element(By.CSS_SELECTOR, "[href='#tab-reviews']")
btn.click()
btn = driver.find_element(By.CLASS_NAME, "star-5")
btn.click()

#пишем коммент
text = driver.find_element(By.ID, "comment")
text.send_keys("Nice Book!")

#пишет имя
text = driver.find_element(By.ID, "author")
text.send_keys("Timer")

#пишем почту
text = driver.find_element(By.ID, "email")
text.send_keys("tshkabrov@gmail.com")

#отправляем отзыв
btn = driver.find_element(By.ID, "submit")
btn.click


time.sleep(10)