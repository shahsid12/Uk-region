# from multiprocessing.connection import wait

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome("C:/UK Retail/Uk-region/chromedriver.exe")
driver.get("https://uat.travelex-dev.net/gb/purchase")  # load the url

cashpassport = driver.find_element_by_id("#cashpassport").click()
# wait 10 seconds before looking for element

try:
    driver.find_element_by_xpath("//input[@name='credit-card-number']").send_keys("5384360000013451")

except NoSuchElementException:
    pass
