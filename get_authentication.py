# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 17:42:04 2019

@author: fz
"""
from selenium import webdriver
##chrome_options = Options()
##chrome_options.add_argument('--headless')
##chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome()
driver.get('url')
elems = driver.find_elements_by_tag_name('input')
for elem in elems:
    if elem.get_attribute('name')=='username':
        elem.send_keys("username")
    elif elem.get_attribute('name')=='password':
        elem.send_keys("password")

elems = driver.find_elements_by_tag_name('button')
for elem in elems:
    if elem.get_attribute('html-type')=='submit':
        elem.click()

for i in range(10):
    if driver.current_url=='url/#home.html':
        for i in driver.get_cookies():
                if i['name']=='_TOKEN':Authorization=i['value']
        break
    else:time.sleep(1)
##time.sleep(3)
##driver.find_element_by_class_name('enjoyhint_skip_btn').click()
##driver.maximize_window()
##driver.save_screenshot('1.png')
driver.quit()

