import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")
price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)

button = browser.find_element_by_id('book')
button.click()

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


browser.quit()
