import os
import math
import time

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = None
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    cur_window = browser.current_window_handle

    submit = browser.find_element_by_xpath('//button[@type="submit"]')
    submit.click()

    time.sleep(0.5)

    new_window = [window for window in browser.window_handles if window != cur_window][0]
    browser.switch_to.window(new_window)

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
