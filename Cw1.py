from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

driver.get("https://strefakursow.pl/")
search_by_id = driver.find_element_by_id('js-b-site-header__bottom-search')
print("My search from element by id is: ")
print(search_by_id)

search_by_id.clear()
search_by_id.send_keys("Linux")
search_by_id.send_keys(Keys.RETURN)
time.sleep(5)

search_by_name = driver.find_element_by_name('search_course[name]')
print("My search from element by name is: ")
print(search_by_name)

search_by_name.clear()
search_by_name.send_keys("Python")
search_by_name.send_keys(Keys.RETURN)
time.sleep(5)

search_by_path = driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/div[2]/div/form/input')
print("My search from element by path is: ")
print(search_by_path)

search_by_path.clear()
search_by_path.send_keys("Django")
search_by_path.send_keys(Keys.RETURN)
time.sleep(5)

search_by_class = driver.find_element_by_class_name('c-search-btn__input')
print("My search from element by class is: ")
print(search_by_class)

search_by_class.clear()
search_by_class.send_keys("DevOps")
search_by_class.send_keys(Keys.RETURN)
time.sleep(5)

driver.close()