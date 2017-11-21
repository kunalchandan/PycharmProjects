from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import datetime
import time

thingy = datetime.datetime
for i in range(100000):
    time.sleep(.005)
    print thingy.utcnow()


binary = FirefoxBinary('usr/local/bin/geckodriver')
driver = webdriver.Firefox()
driver.get("http://www.facebook.com")
assert "Facebook" in driver.title
elem = driver.find_element_by_name("commit")
elem.click()
elem.send_keys(Keys.RETURN)
driver.close()
