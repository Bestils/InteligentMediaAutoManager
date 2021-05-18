from django.shortcuts import render
from django.http import HttpResponse
from instapy import InstaPy
from instagram.external.instagramInstance import InstagramInstance
from .helpers.helper import *

session = InstaPy(username='patrykgaweda1',
                  password='YouKnowNothingJonSnow',
                  headless_browser=False)
# GLOBAL ONLY FOR TEST FUNCTIONS
context = {}


def main(request):
    context['alert'] = "alert"
    if request.method == 'POST':
        alert = request.POST.get('alert')
        context['alert'] = alert
        return render(request, 'Login.html', context)
    return render(request, 'Login.html')


def get_data(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    session.login()
    context['login'] = username
    return render(request, 'Main.html', context)


def main_page(request):
    return get_login(request, 'Main.html')


def functions(request):
    return get_login(request, 'Functions.html')


def statistics(request):
    return get_login(request, 'Statistics.html')


# przygotuje ci do końca te zapisy i odczyty do bazy i niech te funkcje typu like by tag będą robione na bazie zapisanych w bazie danych tagów
# to by bylo typowo pod one tag
def like_photos_by_tags(request):
    data = getTagAndProb(request)
    InstagramInstance.likePhotosByTags(session, data[0], data[1])

def like_videos_by_tags(request):
    data = getTagAndProb(request)
    InstagramInstance.likeVideosByTags(session, data[0], data[1])

def follow_by_location(request):
    location = request.POST.get('location')
    InstagramInstance.likeVideosByTags(session, location)

def follow_by_tags(request):
    tag = request.POST.get('tag')
    InstagramInstance.followByTags(session, tag)

def unfollow_non_followers(request):
    data = getAmountAndDelay(request)
    InstagramInstance.unfollowNonFollowers(session, data[0], data[1])

def unfollow_new_followers(request):
    data = getAmountAndDelay(request)
    InstagramInstance.unfollowNewFollowers(session, data[0], data[1])