# from multiprocessing.connection import wait
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:/UK Retail/Uk-region/chromedriver.exe")
driver.maximize_window()
driver.get("https://uat.travelex-dev.net/gb/purchase")  # load the url
cashpassport = driver.find_element_by_id("#cashpassport").click()
iframe = driver.find_elements_by_tag_name('iframe')[1]
driver.switch_to.frame(iframe)
driver.find_element_by_name("credit-card-number").send_keys("5384360000013451")
driver.implicitly_wait(20)
driver.find_element_by_xpath("//*[@id='noItems']/div/form/div/div[2]/div[3]/button").click()

# card_number.send_keys(Keys.TAB)
# card_number.send_keys(Keys.ENTER)





# # wait 10 seconds before looking for element
#
# time.sleep(5)
# try:
#     driver.find_element_by_xpath("//input[@name='credit-card-number']").send_keys("5384360000013451")
#
# except NoSuchElementException:
#     pass
