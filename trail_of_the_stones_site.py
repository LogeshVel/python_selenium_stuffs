import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = 'E:\chromedriver_win32\chromedriver.exe'
test_url = 'https://techstepacademy.com/trial-of-the-stones'

service_obj = Service(chrome_driver_path)
browser = webdriver.Chrome(service=service_obj)
browser.get(test_url)
print(f'Opened the url : {test_url}')

riddle_input_css_locator = 'input#r1Input'  # this is equal to input[id="r1Input"] - id can be return as # in css
riddle_answer = 'rock'
riddle_button_css_locator = 'button[name="r1Btn"]'

riddle_input_ele = browser.find_element(By.CSS_SELECTOR,riddle_input_css_locator)
riddle_input_ele.send_keys(riddle_answer)
riddle_answer_button_ele = browser.find_element(By.CSS_SELECTOR,riddle_button_css_locator)
riddle_answer_button_ele.click()

pass_banner_css_selector = 'div#passwordBanner h4'
pass_banner_ele = browser.find_element(By.CSS_SELECTOR,pass_banner_css_selector)
password = pass_banner_ele.text
print(f"The password is : {password}")

riddle_of_secret_input_css_locator = 'input#r2Input'
riddle_secret_ele = browser.find_element(By.CSS_SELECTOR,riddle_of_secret_input_css_locator)
riddle_secret_ele.send_keys(password)

riddle_secret_button_css_locator = 'button[name="r2Butn"]'
riddle_secret_answer_button_ele = browser.find_element(By.CSS_SELECTOR,riddle_secret_button_css_locator)
riddle_secret_answer_button_ele.click()

riddle_secret_result_css_selector = 'div#successBanner1 h4'
riddle_secret_result_ele = browser.find_element(By.CSS_SELECTOR,riddle_secret_result_css_selector)
print(f"The Riddle of secrets result : {riddle_secret_result_ele.text}")

# finding richest merchant
total_wealth_xpath = "//label[text()='Total Wealth ($):']/../p"
merchants_name_xpath = "//label[text()='Total Wealth ($):']/../span/b"
# we are going to loop through that and find the highest wealth dynamically
total_wealth_ele = browser.find_elements(By.XPATH,total_wealth_xpath)
merchants_name_ele = browser.find_elements(By.XPATH,merchants_name_xpath)

merchants_dict ={}
for merchant_name,wealth_ele in zip(merchants_name_ele,total_wealth_ele):
    merchants_dict[wealth_ele.text] = merchant_name.text

merchants_sorted_list = sorted(merchants_dict)
print(f"merchants Dicts : {merchants_dict}")
print(f"Merchants sorted lists : {merchants_sorted_list}")
wealth_person = merchants_dict[merchants_sorted_list[-1]]
print(f"The Richest Merchant is {wealth_person}")

wealth_person_input_css = 'input#r3Input'
wealth_input_ele = browser.find_element(By.CSS_SELECTOR,wealth_person_input_css)
wealth_input_ele.send_keys(wealth_person)

rich_answer_css = 'button#r3Butn'
rich_answer_button = browser.find_element(By.CSS_SELECTOR,rich_answer_css)
rich_answer_button.click()

rich_result_css_selector = 'div#successBanner2 h4'
rich_result_ele = browser.find_element(By.CSS_SELECTOR,rich_result_css_selector)
print(f"The Richest Merchant result is : {rich_result_ele.text}")

chk_button_css = 'button#checkButn'
chk_button_ele = browser.find_element(By.CSS_SELECTOR,chk_button_css)
chk_button_ele.click()

end_banner_css = 'div#trialCompleteBanner h4'
end_banner_ele = browser.find_element(By.CSS_SELECTOR,end_banner_css)
print(f"The trail result : {end_banner_ele.text}")

time.sleep(2)
print("Quitting the browser")
browser.quit()



