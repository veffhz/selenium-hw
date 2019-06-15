import time
from selenium import webdriver

link_one = "http://suninjuly.github.io/registration1.html"
link_two = "http://suninjuly.github.io/registration2.html"

browser = webdriver.Chrome()
browser.get(link_two)

input_first_name = browser.find_element_by_xpath('//input[@placeholder="Введите имя"]')
input_first_name.send_keys("Ivan")

input_last_name = browser.find_element_by_xpath('//input[@placeholder="Введите фамилию"]')
input_last_name.send_keys("Ivanov")

input_email = browser.find_element_by_xpath('//input[@placeholder="Введите Email"]')
input_email.send_keys("Ivanov@mail.ru")

button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(1)

welcome_text_elt = browser.find_element_by_tag_name("h1")
welcome_text = welcome_text_elt.text

assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
