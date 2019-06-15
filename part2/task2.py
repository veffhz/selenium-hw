from selenium import webdriver
import time


def calc(xx):
    import math
    return str(math.log(abs(12 * math.sin(int(xx)))))


def main():
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element_input = browser.find_element_by_id("treasure")
    x = x_element_input.get_attribute("valuex")
    result = calc(x)

    input_field = browser.find_element_by_css_selector("input#answer")
    input_field.send_keys(result)

    box = browser.find_element_by_id("robotCheckbox")
    box.click()

    radio = browser.find_element_by_id("robotsRule")
    radio.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(5)


if __name__ == "__main__":
    main()
