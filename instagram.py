from webdriver_manager.firefox import GeckoDriverManager

from Helpers.helper import *
import time
from selenium import webdriver
from time import sleep
import random


browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
class Main:

    comments = [' I am a robotttt', 'Nice ', 'loool very nice! ', 'I like it!', 'Super ;) ', 'hmmm, interesting ',
                ' hi', 'I am a sheep ', 'learn something new ', 'Mind blowing ', 'I like to eat wires', ]

    # This are some variables to keep tracking of the posts
    posts = 0

    def likeAndComm(browser,comments):  # Likes and Comments the first 9 posts
        global posts
        for y in range(1, 4):
            for x in range(1, 4):
                post = browser.find_element_by_xpath(
                    '/html/body/div[1]/section/main/div/div[1]/div/div[' + str(y) + ']/div[' + str(x) + ']')
                browser.implicitly_wait(1)
                post.click()
                sleep(2)
                postLike = browser.find_element_by_xpath(
                    '/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button/div').click()
                # postLike.click()
                sleep(2)
                # comment = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form').click()
                print("click1")
                sleep(3)
                comment = browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form').click()
                print("click2")
                comment = browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(
                    random.choice(comments))
                print("send1")
                sleep(3)
                sendComment = browser.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button')
                sendComment.click()
                print("click3")
                sleep(4)
                posts += 1
                closePost = browser.find_element_by_xpath('/html/body/div[4]/div[3]/button/div')
                closePost.click()
                sleep(3)
            print('Nr. of posts: ' + str(posts))

        sleep(5)
        browser.get('https://www.instagram.com/explore/')
        sleep(6)


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
    browser.get('https://www.instagram.com/explore/')
    sleep(6)
    likeAndComm(browser,comments)
    # Exit Browser after end session
    time.sleep(10)
    browser.quit()
