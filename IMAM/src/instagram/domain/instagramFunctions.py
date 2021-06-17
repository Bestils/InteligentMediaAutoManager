from enum import Enum

from instapy import InstaPy, smart_run


class InstagramFunctions:
    def __init__(self, username, password):
        self.session = InstaPy(username=username,
                               password=password,
                               headless_browser=False)

    def startMachine(self, location, tagList, likeProbability, videPropability, followingNames, unfolowAmount=100,
                     unfollowDelay=100, comments=["nice picture", "you look amazing"], mode='normal',
                     topic="entertainment"):
        with smart_run(self.session):
            self.session.set_relationship_bounds(enabled=True,
                                                 delimit_by_numbers=True,
                                                 max_followers=4590,
                                                 min_followers=45,
                                                 min_following=77)
            self.session.join_pods(topic=topic, engagement_mode=mode)
            print(location, tagList, likeProbability, videPropability, followingNames, unfolowAmount, unfollowDelay,
                  comments)
            if (comments != ''):
                print("comments")
                print(comments)
                self.session.set_do_comment(enabled=True, percentage=80)
                self.session.set_comments(comments)
                self.session.set_delimit_commenting(enabled=True, max_comments=20, min_comments=0)

            if (location == ''):
                self.session.follow_by_locations(location, amount=5)

            if (tagList != ''):
                print("follow")
                self.session.follow_user_followers(followingNames, amount=5)

            if (tagList != '' and likeProbability != ''):
                print("likeByTags")
                print(likeProbability)
                print(tagList)
                self.session.set_user_interact(amount=3, randomize=True, percentage=likeProbability)
                self.session.like_by_tags(tagList, amount=10)

            if (unfolowAmount != '' and unfollowDelay != ''):
                print("unfollowDelay")
                print(unfolowAmount)
                print(unfollowDelay)
                self.session.unfollow_users(amount=unfolowAmount,
                                            allFollowing=True,
                                            style="FIFO",
                                            unfollow_after=unfollowDelay,
                                            sleep_delay=60)
                self.session.unfollow_users(amount=200, instapy_followed_enabled=True,
                                       instapy_followed_param="nonfollowers", style="FIFO", unfollow_after=12 * 60 * 60,
                                       sleep_delay=601)


# engagement_mode: Desided engagement mode for your posts.
# There are four levels of engagement modes 'no_comments', 'light', 'normal' and 'heavy'(normal by default).
# Setting engagement_mode to 'no_comments' makes you receive zero comments on your posts from pod members,
# 'light' encourages approximately 10% of pod members to comment on your post,
# similarly it's around 30% and 90% for 'normal'
# 'heavy' modes respectively.
# Note: Liking, following or any other kind of engagements doesn't follow these modes.

class podstMode(Enum):
    noComment = 'no_comment'
    heavy = 'heavy'
    light = 'light'
    normal = 'normal'