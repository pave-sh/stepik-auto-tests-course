import os
import time

from selenium import webdriver


cur_path = os.path.dirname(os.path.abspath(__file__))
file_to_upload = os.path.join(cur_path, 'text.txt')

with open(file_to_upload, mode='w', encoding='utf-8') as f:
    f.write('test')


browser = None
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name_input = browser.find_element_by_css_selector('input[name="firstname"]')
    first_name_input.send_keys("Ivan")
    last_name_input = browser.find_element_by_css_selector('input[name="lastname"]')
    last_name_input.send_keys("Petrov")
    email_input = browser.find_element_by_css_selector('input[name="email"]')
    email_input.send_keys("petrov@example.com")

    file_input = browser.find_element_by_css_selector('input#file')
    file_input.send_keys(file_to_upload)


    button = browser.find_element_by_xpath('//button[@type="submit"][text()="Submit"]')
    button.click()

finally:
    if browser:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(4)
        # закрываем браузер после всех манипуляций
        browser.quit()
