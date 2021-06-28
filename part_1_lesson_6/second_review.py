from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector('.first_block .first')
    input1.send_keys('A')
    input2 = browser.find_element_by_css_selector('.first_block .second')
    input2.send_keys('R')
    input3 = browser.find_element_by_css_selector('.first_block .third')
    input3.send_keys('nechto@mail')

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    time.sleep(3)

    welcome_text_elt = browser.find_element_by_tag_name('h1')
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
