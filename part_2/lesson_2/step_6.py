import math
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = None
try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_xpath('//span[@id="input_value"]').text
    res = calc(x)

    res_input = browser.find_element_by_xpath('//input[@id="answer"][@required]')
    res_input.send_keys(res)

    checkbox = browser.find_element_by_xpath('//label[@for="robotCheckbox"]')
    checkbox.click()

    robot_radiobutton = browser.find_element_by_xpath('//label[@for="robotsRule"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_radiobutton)
    robot_radiobutton.click()

    submit_button = browser.find_element_by_xpath('//button[@type="submit"][contains(@class, "btn")]')
    submit_button.click()

finally:
    if browser:
        time.sleep(4)
        browser.quit()
        # 28.90600572831194
        # 28.906005691376183
