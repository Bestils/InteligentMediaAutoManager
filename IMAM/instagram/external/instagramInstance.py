# imports
from IMAM.instagram.domain.instagramFunctions import InstagramFunctions


class InstagramInstance:
    def configureSession(session, maxFollowers, minFollowers, maxFollowing, minFollowing):
        session.set_relationship_bounds(enabled=True,
                                        max_followers=maxFollowers,
                                        min_followers=minFollowers,
                                        max_following=maxFollowing,
                                        min_following=minFollowing)

    # Follow activity
    def followByLocation(self, location):
        InstagramFunctions.followByLocation(self, location, 100)

    def followByTags(self, tagList):
        InstagramFunctions.followByTags(self, tagList, 100)

    # Like activity
    def likePhotosByTags(self, tagList, probability):
        InstagramFunctions.likePhotosByTags(self, tagList, probability)

    def likeVideosByTags(self, tagList, probability):
        InstagramFunctions.likeVideosByTags(self, tagList, probability)

        # UNFOLLOW activity

    def unfollowNonFollowers(self, amount, unfollowDelay):
        InstagramFunctions.unfollowNonFollowers(self, amount,
                                                unfollowDelay)

    def unfollowNewFollowers(self, amount, unfollowDelay):
        InstagramFunctions.unfollowNewFollowers(self, amount,
                                                unfollowDelay)

    def setPods(self, toppic, mode):
        InstagramFunctions.setPods(self, toppic, mode)
