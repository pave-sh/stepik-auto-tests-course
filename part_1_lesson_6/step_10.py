from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_xpath_form"

browser = None
try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    # input1 = browser.find_element_by_tag_name('input')
    # input1.send_keys("Ivan")
    # input2 = browser.find_element_by_name('last_name')
    # input2.send_keys("Petrov")
    # input3 = browser.find_element_by_class_name('city')
    # input3.send_keys("Smolensk")
    # input4 = browser.find_element_by_id('country')
    # input4.send_keys("Russia")
    first_name_input = browser.find_element_by_css_selector('.first_block input.first')
    first_name_input.send_keys("Ivan")
    last_name_input = browser.find_element_by_css_selector('.first_block input.second')
    last_name_input.send_keys("Petrov")
    email_input = browser.find_element_by_css_selector('.first_block input.third')
    email_input.send_keys("petrov@example.com")
    button = browser.find_element_by_xpath('//button[@type="submit"][text()="Submit"]')
    button.click()

    # # Отправляем заполненную форму
    # button = browser.find_element_by_css_selector("button.btn")
    # button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()