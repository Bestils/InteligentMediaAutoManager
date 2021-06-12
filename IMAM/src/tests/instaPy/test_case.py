import unittest

from instapy import InstaPy, smart_run

from instagram.external.instagramInstance import InstagramInstance

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.session = InstaPy(username="patrykgaweda1",
                          password="YouKnowNothingJonSnow1",
                          headless_browser=False)

        self.donLikeTags = ['sad','mad','bad' , 'depression']

        self.comments = [
            u'What a  shot! :heart_eyes: What do '
            u'you think of my  shot?',
            u'What an amazing shot! :heart_eyes: LOL nice',
            u'What an amazing shot! :heart_eyes: What do '
            u'you think of my recent shot?'
            u'What an amazing shot! :heart_eyes: I think ']

        self.my_hashtags = ['lol', 'nice', 'pasion']

        self.my_locations = ['sopot', 'gdynia', 'Zalesie']

        self.ignore_list = ['zalesie', 'cyclist', 'raw']

    def testBaseInstapyCommentWithDecentRatio(self):
            with smart_run(self.session):
                self.session.set_dont_like(self.donLikeTags)
                self.session.set_do_follow(enabled=True, percentage=40, times=1)
                self.session.set_do_comment(enabled=True, percentage=20)
                self.session.set_comments(self.comments)

    def testBaseInstapyCommentWithFullRation(self):
        with smart_run(self.session):
            self.session.set_dont_like(self.donLikeTags)
            self.session.set_do_follow(enabled=True, percentage=100, times=1)
            self.session.set_do_comment(enabled=True, percentage=100)
            self.session.set_comments(self.comments)

        
    def testOurCodeCommentWithFullRation(self):
        with smart_run(self.session):
            self.session.set_dont_like(self.donLikeTags)
            self.session.set_do_follow(enabled=True, percentage=100, times=1)
            self.session.set_do_comment(enabled=True, percentage=100)
            InstagramInstance.likePhotosByTags(self.session, self.my_hashtags, 22)(self.comments)


    def testHybidlikePhotosByTags(self):
        with smart_run(self.session):
            self.session.set_ignore_if_contains(self.ignore_list)
            self.session.set_user_interact(amount=2, randomize=True, percentage=60)
            self.session.set_do_follow(enabled=True, percentage=40)
            self.session.set_do_like(enabled=True, percentage=80)
            InstagramInstance.likePhotosByTags(self.session, self.my_hashtags, 22)

    def testHybidlikeVideosByTags(self):
        with smart_run(self.session):
            self.session.set_ignore_if_contains(self.ignore_list)
            self.session.set_user_interact(amount=2, randomize=True, percentage=60)
            self.session.set_do_follow(enabled=True, percentage=40)
            self.session.set_do_like(enabled=True, percentage=80)
            InstagramInstance.likeVideosByTags(self.session, self.my_hashtags, 25)

    def testHybidfollowByTags(self):
        with smart_run(self.session):
            self.session.set_ignore_if_contains(self.ignore_list)
            self.session.set_user_interact(amount=2, randomize=True, percentage=60)
            self.session.set_do_follow(enabled=True, percentage=40)
            self.session.set_do_like(enabled=True, percentage=80)
            InstagramInstance.followByTags(self.session,self.my_hashtags)

    def testHybidfollowByLocation(self):
        with smart_run(self.session):
            self.session.set_ignore_if_contains(self.ignore_list)
            self.session.set_user_interact(amount=2, randomize=True, percentage=60)
            self.session.set_do_follow(enabled=True, percentage=40)
            self.session.set_do_like(enabled=True, percentage=80)
            InstagramInstance.followByLocation(self.session, self.my_locations)

    def testHybidunfollowNewFollowers(self):
        with smart_run(self.session):
            self.session.set_ignore_if_contains(self.ignore_list)
            self.session.set_user_interact(amount=2, randomize=True, percentage=60)
            self.session.set_do_follow(enabled=True, percentage=40)
            self.session.set_do_like(enabled=True, percentage=80)
            InstagramInstance.unfollowNewFollowers(self.session, 34, 111)

    def testHybidunfollowNonFollowers(self):
        with smart_run(self.session):
            self.session.set_ignore_if_contains(self.ignore_list)
            self.session.set_user_interact(amount=2, randomize=True, percentage=60)
            self.session.set_do_follow(enabled=True, percentage=40)
            self.session.set_do_like(enabled=True, percentage=80)
            InstagramInstance.unfollowNonFollowers(self.session, 500,200)


    def testOurCodelikePhotosByTags(self):
        with smart_run(self.session):
            InstagramInstance.likePhotosByTags(self.session, self.my_hashtags, 22)

    def testOurCodelikeVideosByTags(self):
        with smart_run(self.session):
            InstagramInstance.likeVideosByTags(self.session, self.my_hashtags, 25)

    def testOurCodefollowByTags(self):
        with smart_run(self.session):
            InstagramInstance.followByTags(self.session,self.my_hashtags)

    def testOurCodefollowByLocation(self):
        with smart_run(self.session):
            InstagramInstance.followByLocation(self.session, self.my_locations)

    def testOurCodeunfollowNewFollowers(self):
        with smart_run(self.session):
             InstagramInstance.unfollowNewFollowers(self.session, 34, 111)

    def testOurCodeunfollowNonFollowers(self):
        with smart_run(self.session):
            InstagramInstance.unfollowNonFollowers(self.session, 500,200)
