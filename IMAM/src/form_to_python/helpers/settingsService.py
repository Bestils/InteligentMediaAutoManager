from instagram.domain.instagramFunctions import InstagramFunctions
from form_to_python.helpers.commentService import read_one


def get(request):
    settings = {
        'username': request.POST.get('username'),
        'password': request.POST.get('password'),
        'photo_tags': request.POST.get('like_photo_tag').split(' '),
        'photo_prob': request.POST.get('like_photo_probability'),
        'video_tags': request.POST.get('video_tag').split(' '),
        'video_prob': request.POST.get('like_video_probability'),
        'location': request.POST.get('location').split(' '),
        'follow_tags': request.POST.get('follow_tags').split(' '),
        'unfollow_amount': request.POST.get('unfollow_amount'),
        'unfollow_delay': request.POST.get('unfollow_delay'),
        'option': request.POST.get('option')
    }
    settings['option'] = getComments(settings)
    if check_if_null(settings):
        settings = True
    return settings


def configure(settings):
    instagram = InstagramFunctions(settings['username'], settings['password'])
    instagram.startMachine(settings['photo_tags'], settings['photo_prob'], settings['video_tags'], settings['video_prob'], settings['location'], settings['unfollow_amount'], settings['unfollow_delay'], settings['option'], settings['follow_tags'])


def check_if_null(settings):
    for key in settings:
        if settings[key] != '' and settings[key] != settings['username'] and settings[key] != settings['password']:
            return False
    return True


def getComments(settings):
    comments = {}
    if (settings['option'] != 'first'):
        commentSet = read_one(settings['option'])
        comments = commentSet['commentsSet']
        comments = comments[0]
    return comments