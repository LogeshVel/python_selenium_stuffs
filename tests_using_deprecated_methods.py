import time

from selenium import webdriver

# use the deprecated method for demo purpose
chrome_driver_path = 'E:\chromedriver_win32\chromedriver.exe'
test_url = 'https://techstepacademy.com/training-ground'

depcrecated_browser = webdriver.Chrome(chrome_driver_path)
depcrecated_browser.get(test_url)

input_1_css_locator = 'input[name="Input 1"]'
input_2_xpath_locator = '//input[@name="Input 2"]'

input_1 = "Testing input field 1"
input_2 = "Testing input field 2"

input_ele_1 = depcrecated_browser.find_element_by_css_selector(input_1_css_locator)
input_ele_2 = depcrecated_browser.find_element_by_xpath(input_2_xpath_locator)

input_ele_1.send_keys(input_1)
input_ele_2.send_keys(input_2)
time.sleep(2)
depcrecated_browser.quit()
