from multiprocessing.connection import wait

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome("C:/Siddhi/Python/GB Travlex/funnel/funnel/Driver/chromedriver.exe")
driver.get("https://uat.travelex-dev.net/gb/purchase") # load the url

cashpassport = driver.find_element_by_id("#cashpassport").click()
# wait 10 seconds before looking for element
try:
    
    cardnumber = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//input[@name='credit-card-number'")))
    cardnumber.send_keys("5384360000013451")
finally:
    pass
    
