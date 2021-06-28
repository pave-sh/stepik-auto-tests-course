import math
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select


browser = None
try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_1 = browser.find_element_by_xpath('//span[@id="num1"]').text
    x_2 = browser.find_element_by_xpath('//span[@id="num2"]').text

    res = int(x_1) + int(x_2)

    selected = browser.find_element_by_xpath(f'//select[@id="dropdown"]/option[@value="{res}"]')
    selected.click()
    # select = Select(browser.find_element_by_tag_name("select"))
    # select.select_by_value(f"{res}")

    submit_button = browser.find_element_by_xpath('//button[@type="submit"][contains(@class, "btn")]')
    submit_button.click()

finally:
    if browser:
        time.sleep(4)
        browser.quit()
        # 28.90600572831194
        # 28.906005691376183
