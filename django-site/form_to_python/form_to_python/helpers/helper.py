import os
import signal
import subprocess
from instagram.external.instagramInstance import InstagramInstance
from django.shortcuts import render
from form_to_python.helpers.mongoService import MongoClientService
import json

comments = [] # empty dict declaration for test

def set_comments(request):
    client = MongoClientService("db", "comments", "localhost", 27017, "mongodbuser", "mongoPassword")
    setting_id = client.db.find_one(sort=[("id", 1)])["id"] + 1
    tags = request.POST.get('tags').split()

    setting = {
                'id': setting_id,
                'author_name': request.POST.get('author_name'),
                'description': request.POST.get('description'),
                'commentsSet': [{
                    'mandatory_words': tags,
                    'comments': request.POST.get('comments_to_add')
                }]
    }
    setting_json = json.dumps(setting)  # json format
    return setting  # return for page

def add_comment(request):
    single_comment = request.POST.get('comment')
    comments.append(single_comment)
    return comments

def clear_comments():
    comments.clear()

def get_login(request, page_url):
    login = request.session.get('log')
    context = {}
    context['login'] = login
    return render(request, page_url, context)


def get_settings(request):
    settings = {
        'username': request.POST.get('username'),
        'password': request.POST.get('password'),
        'photo_tags': request.POST.get('photo_tags'),
        'photo_prob': request.POST.get('like_photo_probability'),
        'video_tags': request.POST.get('video_tag'),
        'video_prob': request.POST.get('like_video_probability'),
        'location': request.POST.get('location'),
        'follow_tags': request.POST.get('follow_tags'),
        'non_followers_amount': request.POST.get('non_followers_amount'),
        'non_followers_delay': request.POST.get('non_followers_delay'),
        'new_followers_amount': request.POST.get('new_followers_amount'),
        'new_followers_delay': request.POST.get('new_followers_delay')
    }
    if check_settings_if_null(settings):
        settings = True
    return settings


def set_settings(session, settings):
    InstagramInstance.likePhotosByTags(session, [settings['photo_tags']], settings['photo_prob'])
    InstagramInstance.likeVideosByTags(session, [settings['video_tags']], settings['video_prob'])
    InstagramInstance.followByTags(session, [settings['follow_tags']])
    InstagramInstance.followByLocation(session, [settings['location']])
    InstagramInstance.unfollowNewFollowers(session, settings['new_followers_amount'], settings['new_followers_delay'])
    InstagramInstance.unfollowNonFollowers(session, settings['non_followers_amount'], settings['non_followers_delay'])


def check_settings_if_null(settings):
    for key in settings:
        if settings[key] != '' and settings[key] != settings['username'] and settings[key] != settings['password']:
            return False
    return True


def kill_browser():
    try:
        if (os.name == 'posix'):
            browser = subprocess.Popen(['pgrep', 'firefox'], stdout=subprocess.PIPE)
            for pid in browser.stdout:
                os.kill(int(pid), signal.SIGTERM)
        if (os.name == 'nt'):
            os.popen("tskill chrome")
    except:
        print("An error occured while exiting browser.")


def kill_server():
    try:
        if (os.name == 'posix'):
            for line in os.popen("ps -a | grep python3"):
                fields = line.split()
                pid = fields[0]
                os.kill(int(pid), signal.SIGTERM)
        elif (os.name == 'nt'):
            os.popen("tskill python")
        else:
            print("Can't find proper OS.")
    except:
        print("An error occured while disabling server.")


def information():
    print('------------------------------------------------------')
    print('------------------------------------------------------')
    print('-----------------------EXITING------------------------')
    print('------------------------------------------------------')
    print('------------------------------------------------------')


class SettingsNullException(Exception):
    pass
