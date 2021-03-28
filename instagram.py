from Helpers.helper import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


class Main:
    # Browser Init
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    #   Opening WebSite
    browser.get('https://www.instagram.com/')

    # Checking Cookies
    if check_exists_element_by_xpath(browser, '/html/body/div[2]/div/div/div/div[2]/button[1]'):
        find_by_XPath(browser, '/html/body/div[2]/div/div/div/div[2]/button[1]')
    else:
        browser.quit()

    # Finding LogIn Elem by Name
    login = "patrykgaweda1"
    passwd = "YouKnowNothingJonSnow"

    time.sleep(3)
    browser.find_element_by_name('password').send_keys(passwd)
    browser.find_element_by_name('username').send_keys(login)

    # LogIn
    find_by_XPath(browser, '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button')

    # Saving Data Notification
    time.sleep(3)
    if browser.current_url == 'https://www.instagram.com/accounts/onetap/?next=%2F':
        find_by_XPath(browser, '/html/body/div[1]/section/main/div/div/div/div/button')

    # Turn Off Notifications
    time.sleep(2)
    find_by_CssSelector(browser, 'button.aOOlW:nth-child(2)')

    # Exit Browser after end session
    time.sleep(10)
    browser.quit()
