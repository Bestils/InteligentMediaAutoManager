from external.instagramInstance import InstagramInstance
import sys

class Main:
    login = sys.argv[1]  # login = "patrykgaweda1"
    passwd = sys.argv[2]  # passwd = "YouKnowNothingJonSnow"
    print(f'Login: {login} | password: {passwd}')

    session = InstagramInstance(login, passwd, False) # setting session
