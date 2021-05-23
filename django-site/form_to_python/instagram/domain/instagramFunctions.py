from enum import Enum

class InstagramFunctions:
    def followByLocation(session, location):
        if (location != ''):
            session.follow_by_locations(location, amount=100)

    def followByTags(session, tagList):
        if (tagList != ''):
            session.follow_by_tag(tagList, amount=100)

    def likePhotosByTags(session, tagList, probability):
        # Like posts based on hashtags and like 3 posts of its poster
        # this will allow us to make higher impact on user
        if (tagList != '' and probability != ''):
            session.set_user_interact(amount=3, randomize=True, percentage=probability, media='Photo')
            session.like_by_tags(tagList, amount=10)

    def likeVideosByTags(session, tagList, probability):
        # Like posts based on hashtags and like 3 posts of its poster
        # this will allow us to make higher impact on user
        if (tagList != '' and probability != ''):
            session.set_user_interact(amount=3, randomize=True, percentage=probability, media='Video')
            session.like_by_tags(tagList, amount=10)

    # UNFOLLOW activity
    def unfollowNonFollowers(session, amount, unfollowDelay):
        if (amount != '' and unfollowDelay != ''):
            session.unfollow_users(amount=amount,
                                   nonFollowers=True,
                                   style="FIFO",
                                   unfollow_after=unfollowDelay,
                                   sleep_delay=600)

    def unfollowNewFollowers(session, amount, unfollowDelay):
        if (amount != '' and unfollowDelay != ''):
            session.unfollow_users(amount=amount,
                                   allFollowing=True,
                                   style="FIFO",
                                   unfollow_after=unfollowDelay,
                                   sleep_delay=600)

    def setPods(self, session, topic, mode):
        session.join_pods(topic=topic, engagement_mode=mode)


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
