import math
import time

from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = None
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_xpath('//img[@id="treasure"]')
    x = x_element.get_attribute('valuex')
    res = calc(x)

    res_input = browser.find_element_by_xpath('//input[@id="answer"][@required]')
    res_input.send_keys(res)

    checkbox = browser.find_element_by_xpath('//input[@id="robotCheckbox"][@required]')
    checkbox.click()

    robot_radiobutton = browser.find_element_by_xpath('//input[@id="robotsRule"][@value="robots"]')
    robot_radiobutton.click()

    submit_button = browser.find_element_by_xpath('//button[@type="submit"][contains(@class, "btn")]')
    submit_button.click()

finally:
    if browser:
        time.sleep(4)
        browser.quit()
