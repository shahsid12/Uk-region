import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:/UK Retail/Uk-region/chromedriver.exe")
driver.get("https://uat.travelex-dev.net/gb/purchase")
driver.maximize_window()
# driver.find_element_by_class_name('autocomplete-holder').click()
time.sleep(2)
# currency = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
# print(len(currency))

# for money in currency:
#     if money.text == "Australia - Australian Dollar (AUD)":
#         money.click()
#         break

amount = driver.find_element_by_id("noItems-buy-amount")
amount.send_keys(Keys.CONTROL + "a")
amount.send_keys(Keys.DELETE)
amount.send_keys("500")
time.sleep(2)
buy_cash = driver.find_element_by_css_selector("#btnBuyCash").click()

driver.execute_script("driver.execute_script("")")
home_delivery = driver.find_element_by_link_text("#homeDelivery")
home_delivery.click()

# time.sleep(30)
# driver.close()
# shahsid12
