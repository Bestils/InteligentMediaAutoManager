from instagram.external.instagramInstance import InstagramInstance
from django.shortcuts import render
from bson.objectid import ObjectId


def get(request):
    settings = {
        'username': request.POST.get('username'),
        'password': request.POST.get('password'),
        'photo_tags': request.POST.get('like_photo_tag'),
        'photo_prob': request.POST.get('like_photo_probability'),
        'video_tags': request.POST.get('video_tag'),
        'video_prob': request.POST.get('like_video_probability'),
        'location': request.POST.get('location'),
        'follow_tags': request.POST.get('follow_tags'),
        'non_followers_amount': request.POST.get('non_followers_amount'),
        'non_followers_delay': request.POST.get('non_followers_delay'),
        'new_followers_amount': request.POST.get('new_followers_amount'),
        'new_followers_delay': request.POST.get('new_followers_delay'),
    }
    if check_if_null(settings):
        settings = True
    return settings


def configure(session, settings):
    InstagramInstance.configureSession(session, 5000, 30, 3000, 30)
    InstagramInstance.likePhotosByTags(session, [settings['photo_tags']], settings['photo_prob'])
    InstagramInstance.likeVideosByTags(session, [settings['video_tags']], settings['video_prob'])
    InstagramInstance.followByTags(session, [settings['follow_tags']])
    InstagramInstance.followByLocation(session, [settings['location']])
    InstagramInstance.unfollowNewFollowers(session, settings['new_followers_amount'], settings['new_followers_delay'])
    InstagramInstance.unfollowNonFollowers(session, settings['non_followers_amount'], settings['non_followers_delay'])


def check_if_null(settings):
    for key in settings:
        if settings[key] != '' and settings[key] != settings['username'] and settings[key] != settings['password']:
            return False
    return True
