from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

# Browser Init
browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

# Opening WebSite
browser.get('https://www.instagram.com/')

# Checking Cookies
if browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]') != 0:
    browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]').click()

# Finding LogIn Elem by Name
login = "patrykgaweda1"
passwd = "YouKnowNothingJonSnow"

browser.find_element_by_name('password').send_keys(passwd)
browser.find_element_by_name('username').send_keys(login)

# LogIn
browser.find_element_by_tag_name('button').find_element_by_class_name('sqdOP  L3NKy   y3zKF     ').click()

# Saving Data Notification
if browser.current_url == 'https://www.instagram.com/accounts/onetap/?next=%2F':
    browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
