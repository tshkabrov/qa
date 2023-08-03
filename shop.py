import time
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
driver.maximize_window()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.implicitly_wait(5)

#покупка товара
driver.get("https://practice.automationtesting.in/")
time.sleep(1)
btn = driver.find_element(By.LINK_TEXT, "Shop")
btn.click()
driver.execute_script("window.scrollBy(0, 300);")
cart = driver.find_element(By.XPATH, "//a[@data-product_id='182']")
cart.click()
time.sleep(1)
cart = driver.find_element(By.CLASS_NAME, "cartcontents")
cart.click()

order = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout-button.button.alt.wc-forward")))
order.click()

name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "billing_first_name")))
name.send_keys("Timur")
lastname = driver.find_element(By.ID, "billing_last_name")
lastname.send_keys("Shkabrov")
email = driver.find_element(By.ID, "billing_email")
email.send_keys("tshkabrov")
phone = driver.find_element(By.ID, "billing_phone")
phone.send_keys("+77057048282")
country = driver.find_element(By.ID, "s2id_billing_country")
country.click()
time.sleep(1)
select = driver.find_element(By.CSS_SELECTOR, ".select2-input.select2-focused")
select.send_keys("Russia")
russia = driver.find_element(By.CLASS_NAME, "select2-result-label")
russia.click()
adress = driver.find_element(By.ID, "billing_address_1")
adress.send_keys("Samara")
adress1 = driver.find_element(By.ID, "billing_city")
adress1.send_keys("Samara")
adress2 = driver.find_element(By.ID, "billing_postcode")
adress2.send_keys("123456")
country = driver.find_element(By.ID, "billing_state")
country.send_keys("Russia")
driver.execute_script("window.scrollBy(0, 1000);")
time.sleep(1)
check = driver.find_element(By.XPATH, "//div[@id='payment']/ul/li[2]/input")
check.click()
time.sleep(1)
order = driver.find_element(By.ID, "place_order")
order.click()
time.sleep(1)
thanks = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "woocommerce-thankyou-order-received")))
thanks_text = thanks.text
assert thanks_text == "Thank you. Your order has been received."

method = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//tfoot/tr[3]/td")))
method_text = method.text
assert thanks_text == "Check Payments"


time.sleep(10)


#работа в корзине
driver.get("https://practice.automationtesting.in/")
time.sleep(1)
btn = driver.find_element(By.LINK_TEXT, "Shop")
btn.click()
time.sleep(2)
driver.execute_script("window.scrollBy(0, 800);")
cart = driver.find_element(By.XPATH, "//a[@data-product_id='182']")
cart.click()
time.sleep(1)
cart = driver.find_element(By.XPATH, "//a[@data-product_id='180']")
cart.click()

cart = driver.find_element(By.CLASS_NAME, "wpmenucart-contents")
cart.click()
time.sleep(2)


remove = driver.find_element(By.XPATH, "//a[@data-product_id='182']")
remove.click()

undo = driver.find_element(By.LINK_TEXT, "Undo?")
undo.click()

qty = driver.find_element(By.XPATH, "//tbody/tr[2]/td[5]/div/input")
qty.clear()
time.sleep(1)
qty.send_keys("3")

update = driver.find_element(By.CSS_SELECTOR, "[name='update_cart']")
update.click()
time.sleep(1)

value = driver.find_element(By.XPATH, "//tbody/tr[2]/td[5]/div/input")
value_atr = value.get_attribute("value")
assert value_atr == "3"

time.sleep(1)
coupon = driver.find_element(By.CSS_SELECTOR, "[name='apply_coupon']")
coupon.click()

error = driver.find_element(By.CLASS_NAME, "woocommerce-error")

time.sleep(5)




#проверка цены в корзине
driver.get("https://practice.automationtesting.in/")
time.sleep(1)

btn = driver.find_element(By.LINK_TEXT, "Shop")
btn.click()
time.sleep(2)
driver.execute_script("window.scrollBy(0, 600);")
cart = driver.find_element(By.XPATH, "//a[@data-product_id='182']")
cart.click()
time.sleep(2)
item = driver.find_element(By.CLASS_NAME, "cartcontents")
item_text = item.text
assert item_text == "1 Item"
cost = driver.find_element(By.CLASS_NAME, "amount")
cost_text = cost.text
assert cost_text == "₹180.00"
btn = driver.find_element(By.CLASS_NAME, "wpmenucart-contents")
btn.click()
time.sleep(2)

subtotal = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//tr[@class='cart-subtotal']/td/span")) )
total = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//tr[@class='order-total']/td/strong/span")) )

time.sleep(5)



#проверка товара хтмбл 5
# driver.get("https://practice.automationtesting.in/")
# time.sleep(1)
# btn = driver.find_element(By.CSS_SELECTOR, "[href='https://practice.automationtesting.in/my-account/']")
# btn.click()
# time.sleep(2)
#
# email = driver.find_element(By.ID, "username")
# email.send_keys("tshkabrov@gmail.com")
#
# password = driver.find_element(By.ID, "password")
# password.send_keys("p6Tv01TZ4P1u")
#
# login = driver.find_element(By.CSS_SELECTOR, "[name='login']")
# login.click()
# time.sleep(1)
#
# btn = driver.find_element(By.LINK_TEXT, "Shop")
# btn.click()
# time.sleep(1)
#
# product = driver.find_element(By.XPATH, ".//*[@class='products masonry-done']/li[3]/a")
# product.click()
# time.sleep(2)
#
# title = driver.find_element(By.CLASS_NAME, "product_title")
# titletext = title.text
# assert titletext == 'HTML5 Forms'
# time.sleep(5)

# #подсчет количества товаров в категории
# btn = driver.find_element(By.CSS_SELECTOR, "[href='https://practice.automationtesting.in/my-account/']")
# btn.click()
# time.sleep(2)
#
# email = driver.find_element(By.ID, "username")
# email.send_keys("tshkabrov@gmail.com")
#
# password = driver.find_element(By.ID, "password")
# password.send_keys("p6Tv01TZ4P1u")
#
# login = driver.find_element(By.CSS_SELECTOR, "[name='login']")
# login.click()
# time.sleep(1)
#
# btn = driver.find_element(By.LINK_TEXT, "Shop")
# btn.click()
# time.sleep(1)
#
# btn = driver.find_element(By.LINK_TEXT, "HTML")
# btn.click()
# time.sleep(1)
#
# item_count = driver.find_elements(By.CLASS_NAME, "woocommerce-LoopProduct-link")
# if len(item_count) == 3:
#     print("торваров 3")
# else:
#     print("товаров не 3")
#
# time.sleep(10)

# #сортировка товаров
# btn = driver.find_element(By.CSS_SELECTOR, "[href='https://practice.automationtesting.in/my-account/']")
# btn.click()
# time.sleep(2)
# email = driver.find_element(By.ID, "username")
# email.send_keys("tshkabrov@gmail.com")
# password = driver.find_element(By.ID, "password")
# password.send_keys("p6Tv01TZ4P1u")
# login = driver.find_element(By.CSS_SELECTOR, "[name='login']")
# login.click()
# time.sleep(1)
# btn = driver.find_element(By.LINK_TEXT, "Shop")
# btn.click()
# time.sleep(1)
#
# element_item = driver.find_element(By.CSS_SELECTOR, "[value='menu_order']")
# element = element_item.get_attribute("selected")
# if element == "selected":
#     print("сортировка выбрана")
# else:
#     print("сортировка по умлочанию не выбрана")
#
# select_item = driver.find_element(By.CSS_SELECTOR, "[value='price-desc']")
# select_item.click()
# time.sleep(2)
#
# element = driver.find_element(By.CSS_SELECTOR, "[value='menu_order']")
# select_item = driver.find_element(By.CSS_SELECTOR, "[value='price-desc']")
# select = select_item.get_attribute("value")
# if select == "price-desc":
#     print("сортировка выбрана")
# else:
#     print("сортировка  не выбрана")
#
# time.sleep(1)


