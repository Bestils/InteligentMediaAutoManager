from django.shortcuts import render
import subprocess
import signal
import os

from instagram.external.instagramInstance import InstagramInstance


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
    return settings

def set_settings(session, settings):
    InstagramInstance.likePhotosByTags(session, [settings['photo_tags']], settings['photo_prob'])
    InstagramInstance.likeVideosByTags(session, [settings['video_tags']], settings['video_prob'])
    InstagramInstance.followByTags(session, [settings['follow_tags']])
    InstagramInstance.followByLocation(session, settings['location'])
    InstagramInstance.unfollowNewFollowers(session, settings['new_followers_amount'], settings['new_followers_delay'])
    InstagramInstance.unfollowNonFollowers(session, settings['non_followers_amount'], settings['non_followers_delay'])

def kill_browser():
    try:
        browser = subprocess.Popen(['pgrep', 'firefox'], stdout=subprocess.PIPE)
        for pid in browser.stdout:
            os.kill(int(pid), signal.SIGTERM)
        print('----------------------EXITING-------------------------')
        print('------------------------------------------------------')
        print('-----------SERVER-DISABLED-SUCCESSFULLY---------------')
        print('------------------------------------------------------')
    except:
        print("An error occured while exiting browser.")


def kill_server():
    try:
        for line in os.popen("ps -a | grep python3"):
            fields = line.split()
            pid = fields[0]
            os.kill(int(pid), signal.SIGTERM)

    except:
        print("An error occured while disabling server.")