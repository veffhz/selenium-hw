from selenium import webdriver
import time


def calc(xx):
    import math
    return str(math.log(abs(12 * math.sin(int(xx)))))


def main():
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.execute_script("window.scrollBy(0, 100);")

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
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
