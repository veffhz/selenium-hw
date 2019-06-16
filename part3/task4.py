import time
import math
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]


class TestUnique:
    correct = "Correct!"

    @pytest.mark.parametrize('link', links)
    def test_next_link(self, browser, link):
        browser.get(link)
        result_text = self.get_result_text(browser)
        assert TestUnique.correct == result_text, \
            "Should be '{}', but got {}".format(TestUnique.correct, result_text)

    @property
    def value(self):
        return str(math.log(int(time.time())))

    def get_result_text(self, browser):

        WebDriverWait(browser, 7).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div textarea"))
        )

        input_field = browser.find_element_by_css_selector("div textarea")
        input_field.send_keys(self.value)

        button = browser.find_element_by_css_selector("button.submit-submission")
        button.click()

        time.sleep(1)

        result = browser.find_element_by_tag_name("pre")
        return result.text
