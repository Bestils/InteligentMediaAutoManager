from external.instagramInstance import InstagramInstance
from instapy import InstaPy
from instapy import smart_run
import requests
import sys
from multiprocessing.connection import Listener

address = ('localhost', 6000)
listener = Listener(address)


class Main:
    login = sys.argv[1]  # login = "patrykgaweda1"
    passwd = sys.argv[2]  # passwd = "YouKnowNothingJonSnow"
    url = 'http://127.0.0.1:8000/'
    answer = requests.session()
    data = {}
    print(f'Login: {login} | password: {passwd}')

    session = InstaPy(username=login,
                      password=passwd,
                      headless_browser=False)
    data['alert'] = 'Wygrales zycie'
    session.login()
    InstagramInstance.likePhotosByTags(session, ['car', 'mercedes'], 25)
