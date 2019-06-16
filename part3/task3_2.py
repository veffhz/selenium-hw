import time
import pytest


@pytest.fixture(autouse=True)
def prepare_data():
    print("preparing some critical data for every test")


class TestUnique:

    welcome = "Поздравляем! Вы успешно зарегистировались!"

    @pytest.mark.work
    def test_link1(self, browser):
        browser.get("http://suninjuly.github.io/registration1.html")
        welcome_text = self.get_result_text(browser)
        assert TestUnique.welcome == welcome_text, "Should be '{}'".format(TestUnique.welcome)

    #@pytest.mark.broken
    #@pytest.mark.skip(reason="broken")
    @pytest.mark.xfail
    def test_link2(self, browser):
        browser.get("http://suninjuly.github.io/registration2.html")
        welcome_text = self.get_result_text(browser)
        assert TestUnique.welcome == welcome_text, "Should be '{}'".format(TestUnique.welcome)

    @staticmethod
    def get_result_text(browser):
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
        return welcome_text_elt.text
