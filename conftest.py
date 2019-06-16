from selenium import webdriver
import pytest


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")

    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        print("Browser {} still is not implemented".format(browser_name))
        raise Exception("Browser {} still is not implemented".format(browser_name))

    yield browser
    print("\nquit browser..")
    browser.quit()
