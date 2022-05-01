import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:/UK Retail/Uk-region/chromedriver.exe")
driver.get("https://uat.travelex-dev.net/gb/purchase")
driver.maximize_window()
# driver.find_element_by_class_name('autocomplete-holder').click()
# time.sleep(2)
# currency = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
# print(len(currency))

# for money in currency:
#     if money.text == "Australia - Australian Dollar (AUD)":
#         money.click()
#         break
driver.find_element_by_class_name("autocomplete-holder").click()
# driver.find_element_by_id("ui-id-4")
currencies = []
currencies = driver.find_elements_by_xpath(".//*[@id='ui-id-4']/li")
for item in currencies:
    print(item.text)
    if item.text == "Canada - Canadian Dollar (CAD)":
        item.click()
        break
# time.sleep(2)
amount = driver.find_element_by_id("noItems-buy-amount")
amount.send_keys(Keys.CONTROL + "a")
amount.send_keys(Keys.DELETE)
amount.send_keys("500")
time.sleep(2)
buy_cash = driver.find_element_by_css_selector("#btnBuyCash").click()
time.sleep(5)
driver.execute_script("window.scrollTo(0,850)")
time.sleep(3)

home_deliver = driver.find_element_by_xpath(".//*[@class='button delivery buying-options-tab tabnav-3']").click()
driver.implicitly_wait(10)
driver.close()
