from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://strefakursow.pl/")

element = driver.find_element_by_class_name('b-site-header__bottom-login-button')
element.click() #klikamy clear -> czyści elementy typu input text itp.

time.sleep(5)

element2 = driver.find_element_by_id('customer_login')
element2.clear() #dobrze jest wyczyścić by mieć pewność, że wpisuje się swoje dane.
element2.send_keys('marcin@gazda.pl')

time.sleep(5)

element3 = driver.find_element_by_id('customer_password')
element3.clear()
element3.send_keys('password')

time.sleep(5)

element3.send_keys(Keys.RETURN)

time.sleep(5)

driver.close()