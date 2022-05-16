from select import select

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://uat.travelex-dev.net/gb/purchase")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_id("btnBuyCash").click()
time.sleep(3)
driver.execute_script("window.scrollTo(0,700)")
driver.find_element_by_xpath(".//*[@class='button delivery buying-options-tab tabnav-3']").click()
time.sleep(3)
# driver.execute_script("window.scrollTo(0,150)")
dates = driver.find_elements_by_xpath(".//*[@data-month='4']")
# driver.execute_script("window.scrollTo(0,)")
# date = input("Please enter the date which u want ur order to be delivered:- ")

for date in dates:
    data = date.text
    # print(data)
    if data == '20':
        date.click()
        print(data)
        break


next = driver.find_element_by_id("submitBtn").click()



# Contact Details

title_sel = Select( driver.find_element_by_xpath("//select[@id='title']"))
title_sel.select_by_visible_text("Miss.")
first_name = driver.find_element_by_id("firstname")
first_name.send_keys("Siddhi")
last_name = driver.find_element_by_id("lastname")
last_name.send_keys("Shah")
phone_number = driver.find_element_by_id("phonenumber").send_keys("0987654321")
email=driver.find_element_by_id("email").send_keys("siddhi.shah@travelex.com")
confirm_email=driver.find_element_by_id("confirmemail").send_keys("siddhi.shah@travelex.com")

# address details


addressfindername = driver.find_element_by_id("addressfindername").send_keys("24")
addressfinderpostcode = driver.find_element_by_id("addressfinderpostcode").send_keys("PE27AD")
find_address=driver.find_element_by_id("find-address").click()

time.sleep(3)


# card details

cardtype = Select(driver.find_element_by_xpath('//select[@id="cardtype"]'))
cardtype.select_by_visible_text("Visa ( Debit )")
iframe = driver.find_elements_by_tag_name("iframe")[1]
driver.switch_to.frame(iframe)
driver.find_element_by_xpath(".//*[@name='credit-card-number']").send_keys("4111111111111111")
driver.switch_to.parent_frame()
expmonth = Select(driver.find_element_by_xpath('//select[@id="expmonth"]'))
expmonth.select_by_visible_text("01")
expyear = Select(driver.find_element_by_xpath('//select[@id="expyear"]'))
expyear.select_by_visible_text("2025")
securitycode = driver.find_element_by_id("securitycode").send_keys("123")


dobday = driver.find_element_by_id("dobday").send_keys("01")
dobmonth = Select(driver.find_element_by_xpath("//select[@id='dobmonth']"))
dobmonth.select_by_visible_text("January")
dobyear = driver.find_element_by_id("dobyear").send_keys("1990")
time.sleep(3)
submitBtn = driver.find_element_by_id("submitBtn").click()

# newsletter_32= driver.find_element_by_id("newsletter-32").click()
# span_rr2= driver.find_element_by_id("span_rr2").click()
#
# submitBtn_2 = driver.find_element_by_id("submitBtn").click()
driver.execute_script("window.scrollTo(0,700)")

try:
    newsletter_32 = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,"//label[@for='newsletter-32']")))
    newsletter_32.click()
    span_rr2= WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,"//label[@id='lbl_rr2']")))
    span_rr2.click()
    submitBtn_2 = driver.find_element_by_id("submitBtn")
    submitBtn_2.click()
    time.sleep(40)
finally:
    # time.sleep(10)
    # driver.implicitly_wait(5)
    driver.close()

time.sleep(5)