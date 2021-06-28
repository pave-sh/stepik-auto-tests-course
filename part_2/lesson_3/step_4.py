import os
import math
import time

from selenium import webdriver


cur_path = os.path.dirname(os.path.abspath(__file__))
file_to_upload = os.path.join(cur_path, 'text.txt')

with open(file_to_upload, mode='w', encoding='utf-8') as f:
    f.write('test')


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = None
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    submit = browser.find_element_by_xpath('//button[@type="submit"]')
    submit.click()

    time.sleep(0.5)

    alert = browser.switch_to.alert
    alert.accept()

    time.sleep(0.5)

    x = browser.find_element_by_xpath('//span[@id="input_value"]').text
    res = calc(x)

    res_input = browser.find_element_by_xpath('//input[@id="answer"][@required]')
    res_input.send_keys(res)


    button = browser.find_element_by_xpath('//button[@type="submit"][text()="Submit"]')
    button.click()

    time.sleep(0.5)

    alert = browser.switch_to.alert
    alert_text = alert.text
    needed_value = alert_text.split('Stepik quiz: ')[-1]
    print(needed_value)

finally:
    if browser:
        browser.quit()
