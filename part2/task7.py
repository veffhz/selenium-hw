from selenium import webdriver
import time


def calc(xx):
    import math
    return str(math.log(abs(12 * math.sin(int(xx)))))


def main():
    link = "http://suninjuly.github.io/redirect_accept.html"

    browser = webdriver.Chrome()
    browser.get(link)

    start_button = browser.find_element_by_css_selector(".container button")
    start_button.click()

    next_window_name = browser.window_handles[1]  # like a "CDwindow-E4680A3919D45BB5D887AFA81575C338"
    browser.switch_to.window(next_window_name)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    result = calc(x)

    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(result)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(7)


if __name__ == "__main__":
    main()
