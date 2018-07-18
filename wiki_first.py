import unittest
from selenium import webdriver

driver = webdriver.Firefox()
driver.implicity_wait(10)
driver.maximize_window()

driver.get(https://www.wikipedia.org/)
driver.find_element_by_id("js-link-box-ru").click()

driver.quit()
