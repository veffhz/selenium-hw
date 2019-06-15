from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time


def calc(xx):
    import math
    return str(math.log(abs(12 * math.sin(int(xx)))))


def main():
    link = "http://suninjuly.github.io/explicit_wait2.html"

    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "10000")
    )

    book = browser.find_element_by_id("book")
    book.click()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    result = calc(x)

    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(result)

    button = browser.find_element_by_id("solve")
    button.click()

    time.sleep(7)


if __name__ == "__main__":
    main()
