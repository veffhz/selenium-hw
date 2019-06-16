import time
from selenium import webdriver


class TestUnique:

    welcome = "Поздравляем! Вы успешно зарегистировались!"

    def setup_method(self):
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        self.browser.quit()

    def test_link1(self):
        self.browser.get("http://suninjuly.github.io/registration1.html")
        welcome_text = self.get_result_text()
        assert TestUnique.welcome == welcome_text, "Should be '{}'".format(TestUnique.welcome)

    def test_link2(self):
        self.browser.get("http://suninjuly.github.io/registration2.html")
        welcome_text = self.get_result_text()
        assert TestUnique.welcome == welcome_text, "Should be '{}'".format(TestUnique.welcome)

    def get_result_text(self):
        input_first_name = self.browser.find_element_by_xpath('//input[@placeholder="Введите имя"]')
        input_first_name.send_keys("Ivan")

        input_last_name = self.browser.find_element_by_xpath('//input[@placeholder="Введите фамилию"]')
        input_last_name.send_keys("Ivanov")

        input_email = self.browser.find_element_by_xpath('//input[@placeholder="Введите Email"]')
        input_email.send_keys("Ivanov@mail.ru")

        button = self.browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        return welcome_text_elt.text
