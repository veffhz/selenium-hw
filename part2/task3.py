from selenium import webdriver
import time


def main():
    link = "http://suninjuly.github.io/selects1.html"
    link2 = "http://suninjuly.github.io/selects2.html"

    browser = webdriver.Chrome()
    browser.get(link2)

    num1 = browser.find_element_by_id("num1")
    num2 = browser.find_element_by_id("num2")

    sum_1_2 = int(num1.text) + int(num2.text)

    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(sum_1_2))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(5)


if __name__ == "__main__":
    main()
