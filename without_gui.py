import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

chrome_driver_path = 'E:\chromedriver_win32\chromedriver.exe'
test_url = 'https://techstepacademy.com/training-ground'

input_1_css_locator = 'input[name="Input 1"]'
input_2_xpath_locator = '//input[@name="Input 2"]'

input_1 = "Testing input field 1"
input_2 = "Testing input field 2"

service_obj = Service(chrome_driver_path)
browser = webdriver.Chrome(service=service_obj,options=options)
browser.get(test_url)
print(f'Opened the url : {test_url}')

input_ele_1 = browser.find_element(By.CSS_SELECTOR ,input_1_css_locator)
input_ele_2 = browser.find_element(By.XPATH,input_2_xpath_locator)
print('Found the input elements')
input_ele_1.send_keys(input_1)
input_ele_2.send_keys(input_2)
print('Send the input texts')
print('Finding the Price of the Product 1')

product_1_price_xpath='//b[text()="Product 1"]/../../p'
product_1_price_ele = browser.find_element(By.XPATH,product_1_price_xpath)
print(product_1_price_ele.text)

print("Quitting the browser")
browser.quit()
