import httplib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from bs4 import BeautifulSoup, SoupStrainer
import time
import datetime

header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'}
name = "Mithil V. Kumar"
email = "mithil.v.k@gmail.com"
tel = "1234567890"
address = "123 Mithil Rd"
apt = "#123"
country = "CANADA"
province = "ON"
city = "Toronto"
postal = "M1T1L3"
number = "214245682348621"
expM = "13"
expY = "2020"
cvv = "654"
# ###### If The program is not running make sure to check this value #####
minute = 00
second = 00

binary = FirefoxBinary('usr/local/bin/geckodriver')
driver = webdriver.Firefox()
while (datetime.datetime.utcnow().minute != minute) and (datetime.datetime.utcnow().second != second):
    time.sleep(0.008)
    print(datetime.datetime.utcnow())


def urls_to_visit():
    all_items_page = httplib2.Http()
    status, all_items_page_response = all_items_page.request('http://www.supremenewyork.com/shop/sweatshirts',  headers=header)
    list_of_urls = []
    for link in BeautifulSoup(all_items_page_response, parseOnlyThese=SoupStrainer('a')):
        if link.has_key('href'):
            if not str(link['href']).__contains__('supreme'):
                if str(link['href']).count('/') > 3:
                    list_of_urls.append(str('http://www.supremenewyork.com' + str(link['href'])))
    return list_of_urls


urls = urls_to_visit()

for i in range(len(urls)/2):
    driver.get(urls[i])
    try:
        elem = driver.find_element_by_name("commit")
        elem.click()
    except:
        pass
elem = driver.find_element_by_link_text('checkout now')
elem.click()
if driver.current_url == 'http://www.supremenewyork.com/shop/cart':
    try:
        elem = driver.find_elements_by_link_text('remove')
        for each in elem:
            each.click()
        elem = driver.find_elements_by_link_text('checkout now')
    except:
        pass
elem = driver.find_element_by_id("order_billing_name")
elem.send_keys(name)
elem = driver.find_element_by_id("order_email")
elem.send_keys(email)
elem = driver.find_element_by_id("order_tel")
elem.send_keys(tel)
elem = driver.find_element_by_id("bo")
elem.send_keys(address)
elem = driver.find_element_by_id("oba3")
elem.send_keys(apt)
elem = driver.find_element_by_id("order_billing_zip")
elem.send_keys(postal)
elem = driver.find_element_by_id("order_billing_city")
elem.send_keys(city)
elem = driver.find_element_by_id("nnaerb")
elem.send_keys(number)
elem = driver.find_element_by_id("orcer")
elem.send_keys(cvv)
elem.send_keys(Keys.RETURN)

elem = driver.find_element_by_id("order_terms")
elem.click()

elem = driver.find_element_by_id("credit_card_year")
for i in elem.find_elements_by_tag_name('option'):
    if i.text == expY:
        i.click()
        break
elem = driver.find_element_by_id("credit_card_month")
for i in elem.find_elements_by_tag_name('option'):
    if i.text == expM:
        i.click()
        break
elem = driver.find_element_by_id("order_billing_country")
for i in elem.find_elements_by_tag_name('option'):
    if i.text == country:
        i.click()
        break
elem = driver.find_element_by_id("order_billing_state")
for i in elem.find_elements_by_tag_name('option'):
    if i.text == province:
        i.click()
        break

time.sleep(1000)
driver.close()
