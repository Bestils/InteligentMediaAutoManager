from selenium.common.exceptions import NoSuchElementException


def check_exists_element_by_xpath(browser, xpath):
    try:
        browser.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


def find_by_XPath(browser, xpath):
    browser.find_element_by_xpath(xpath).click()


def find_by_CssSelector(browser, css_selector):
    browser.find_element_by_css_selector(css_selector).click()
