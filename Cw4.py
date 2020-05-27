from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.set_page_load_timeout(30)
driver.get("http://strefakursow.pl/contact.html")

driver.find_element_by_id('contact[full_name]').send_keys('Marcin')
driver.find_element_by_id('contact[address]').send_keys('marcin@gazda.pl')
driver.find_element_by_id('contact[subject]').send_keys('Kurs Python')
driver.find_element_by_id('contact[body]').send_keys('Kurs Python jest bardzo interesujący :)')

time.sleep(15)
driver.quit()