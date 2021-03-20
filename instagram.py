from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException
import time


def check_exists_element_by_xpath(xpath):
    try:
        browser.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def find_and_click(xpath):
    browser.find_element_by_xpath(xpath).click()

# Browser Init
browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

# Opening WebSite
browser.get('https://www.instagram.com/')

# Checking Cookies
if check_exists_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]'):
    find_and_click('/html/body/div[2]/div/div/div/div[2]/button[1]')
else:
    browser.quit()

# Finding LogIn Elem by Name
login = "patrykgaweda1"
passwd = "YouKnowNothingJonSnow"

browser.find_element_by_name('password').send_keys(passwd)
browser.find_element_by_name('username').send_keys(login)

# LogIn
find_and_click('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button')

# Saving Data Notification
time.sleep(3)

if browser.current_url == 'https://www.instagram.com/accounts/onetap/?next=%2F':
    find_and_click('/html/body/div[1]/section/main/div/div/div/div/button')

# Turn Off Notifications
time.sleep(3)
find_and_click('/html/body/div[5]/div/div/div/div[3]/button[2]')

# Exit Browser after end session
time.sleep(10)
browser.quit()