import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = 'E:\chromedriver_win32\chromedriver.exe'
test_url = 'https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407'

service_obj = Service(chrome_driver_path)
browser = webdriver.Chrome(service=service_obj)
browser.get(test_url)
print(f'Opened the url : {test_url}')
browser.maximize_window()
print("Maximized the window")

# working with the radio buttons
male_radio_button_xpath = '//label[text()="Male"]'
male_radio_button_ele = browser.find_element(By.XPATH, male_radio_button_xpath)
male_radio_button_ele.click()
print("Selected Male")

# working with check boxes
sunday_chk_box_xpath = '//label[text()="Sunday"]'
sunday_chk_box_ele = browser.find_element(By.XPATH,sunday_chk_box_xpath)
sunday_chk_box_ele.click()
print("Selected Sunday")

monday_chk_box_xpath = '//label[text()="Monday"]'
monday_chk_box_ele = browser.find_element(By.XPATH,monday_chk_box_xpath)
monday_chk_box_ele.click()
print("Selected Monday")

time.sleep(2)
print("Quitting the browser")
browser.quit()


