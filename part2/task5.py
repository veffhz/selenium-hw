import time
from selenium import webdriver


def get_file():
    import os
    with open("mock.txt", 'w+'):
        current_dir = os.path.abspath(os.path.dirname(__file__))
        return os.path.join(current_dir, "mock.txt")


def main():
    link = "http://suninjuly.github.io/file_input.html"

    browser = webdriver.Chrome()
    browser.get(link)

    input_first_name = browser.find_element_by_xpath('//input[@placeholder="Введите имя"]')
    input_first_name.send_keys("Ivan")

    input_last_name = browser.find_element_by_xpath('//input[@placeholder="Введите фамилию"]')
    input_last_name.send_keys("Ivanov")

    input_email = browser.find_element_by_xpath('//input[@placeholder="Введите Email"]')
    input_email.send_keys("Ivanov@mail.ru")

    file_form = browser.find_element_by_id("file")
    file_form.send_keys(get_file())

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)


if __name__ == "__main__":
    main()
