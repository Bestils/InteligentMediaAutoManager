from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium import webdriver
from time import sleep
import random
# imports
from instapy import InstaPy
from instapy import smart_run


class InstagramInstance:

    def __init__(self, username, password, headless):
        session = InstaPy(username=username,
                          password=password,
                          headless_browser=headless)
        self.session = session  # instance variable unique to each instance
        self.session.login()

    def configureSession(session, maxFollowers, minFollowers, maxFollowing, minFollowing):
        session.set_relationship_bounds(enabled=True,
                                        max_followers=maxFollowers,
                                        min_followers=minFollowers,
                                        max_following=maxFollowing,
                                        min_following=minFollowing)

    # Follow activity
    def folowByLocation(self, location):
        InstagramFunctions.folowByLocation(self.session, location, 100)

    def folowByTags(self, tagList):
        InstagramFunctions.folowByTags(self.session, tagList, 100)

    # Like activity
    def likePhotosByTags(self, tagList, probability):
        InstagramFunctions.likePhotosByTags(self, tagList, probability)

    def likeVideosByTags(self, tagList, probability):
        InstagramFunctions.likeVideosByTags(self.session, tagList, probability)

        # UNFOLLOW activity

    def unfollowNonFollowers(self, amount, unfollowDelay):
        InstagramFunctions.unfollowNonFollowers(self.session, amount,
                                                unfollowDelay)

    def unfollowNewFollowers(self, amount, unfollowDelay):
        InstagramFunctions.unfollowNewFollowers(self.session, amount,
                                                unfollowDelay)

    def setPods(self, toppic, mode):
        InstagramFunctions.setPods(self.session, toppic, mode)
