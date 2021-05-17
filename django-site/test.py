from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys
import requests


class Main:
    # Making session for communication with django
    login = sys.argv[1]
    passwd = sys.argv[2]
    session = requests.session()
    url = 'http://127.0.0.1:8000/'
    data = {}
    data['odp'] = 'Wygrales zycie'

    session.post(url, data = data)
    # Exit Browser after end session
    # time.sleep(2)
    # browser.quit()
