from enum import Enum

from instapy import InstaPy, smart_run


class InstagramFunctions:
    def __init__(self, username,password):
        self.session =  InstaPy(username=username,
                  password=password,
                  headless_browser=True)
    def startMachine(self, location ,tagList, likeProbability,videPropability,unfolowAmount,unfollowDelay, comments, mode="normal" , topic = "entertainment"):
        with smart_run( self.session):
            if (location != ''):
                self.session.follow_by_locations(location, amount=100)
            if (tagList != ''):
                self.session.follow_by_tags(tagList, amount=100)
    
            if (tagList != '' and likeProbability != ''):
                self.session.set_user_interact(amount=3, randomize=True, percentage=likeProbability, media='Photo')
                self.session.like_by_tags(tagList, amount=10)
                
            if (tagList != '' and videPropability != ''):
                self.session.set_user_interact(amount=3, randomize=True, percentage=videPropability, media='Video')
                self.session.like_by_tags(tagList, amount=10)
            if (unfolowAmount != '' and unfollowDelay != ''):
                self.session.unfollow_users(amount=unfolowAmount,
                                       allFollowing=True,
                                       style="FIFO",
                                       unfollow_after=unfollowDelay,
                                       sleep_delay=600)
            if (comments != ''):
                self.session.set_comments(comments)
                self.session.set_delimit_commenting(enabled=True, max_comments=20, min_comments=0)
                self.session.set_do_comment(enabled=True, percentage=80)
       
            self.session.join_pods(topic=topic, engagement_mode=mode)


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
