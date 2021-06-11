from instagram.domain.instagramFunctions import InstagramFunctions


class InstagramInstance:
    def configureSession(self, session, maxFollowers, minFollowers, maxFollowing, minFollowing):
        session.set_relationship_bounds(enabled=True,
                                        max_followers=maxFollowers,
                                        min_followers=minFollowers,
                                        max_following=maxFollowing,
                                        min_following=minFollowing)

    # Follow activity
    def followByLocation(self, session, location):
        InstagramFunctions.followByLocation( session, location, 100)

    def followByTags(self, session, tagList):
        InstagramFunctions.followByTags( session, tagList)

    # Like activity
    def likePhotosByTags(self, session, tagList, probability):
        InstagramFunctions.likePhotosByTags( session, tagList, probability)

    def likeVideosByTags(self, session, comments):
        InstagramFunctions.setComments( session, comments)

    def likeVideosByTags(self, session, tagList, probability):
            InstagramFunctions.likeVideosByTags( session, tagList, probability)
        # UNFOLLOW activity

    def unfollowNonFollowers(self, session, amount, unfollowDelay):
        InstagramFunctions.unfollowNonFollowers( session, amount,
                                                unfollowDelay)

    def unfollowNewFollowers(self, session, amount, unfollowDelay):
        InstagramFunctions.unfollowNewFollowers( session, amount,
                                                unfollowDelay)

    def setPods(self, session, toppic, mode):
        InstagramFunctions.setPods( session, toppic, mode)
