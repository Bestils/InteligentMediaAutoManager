from instapy import InstaPy, smart_run

class InstagramFunctions:
    def __init__(self, username,password):
        self.session =  InstaPy(username=username,
                  password=password,
                  headless_browser=False)

    def startMachine(self, photo_tags, photo_prob, video_tags, video_prob, location, unfollow_amount, unfollow_delay, comments, follow_tags):
        with smart_run(self.session):
            print(follow_tags.length)

            if location.length > 0:
                self.session.follow_by_locations(location, amount=100)

            if follow_tags.length > 0:
                self.session.follow_by_tags(follow_tags, amount=100)

            if (photo_tags != '' and photo_prob != ''):
                self.session.set_user_interact(amount=3, randomize=True, percentage=photo_prob, media='Photo')
                self.session.like_by_tags(photo_tags, amount=100)

            if (video_tags != '' and video_prob != ''):
                self.session.set_user_interact(amount=3, randomize=True, percentage=video_prob, media='Video')
                self.session.like_by_tags(video_tags, amount=100)

            if (unfollow_amount != '' and unfollow_delay != ''):
                self.session.unfollow_users(amount=unfollow_amount,
                                       allFollowing=True,
                                       style="FIFO",
                                       unfollow_after=unfollow_delay*60000,
                                       sleep_delay=600)

            if comments != '':
                self.session.set_comments(comments)
                self.session.set_do_comment(enabled=True, percentage=80)
                self.session.set_delimit_commenting(enabled=True, max_comments=20, min_comments=0)
                self.session.join_pods()


