from django.shortcuts import render
from django.http import HttpResponse
from instapy import InstaPy, smart_run
from instagram.external.instagramInstance import InstagramInstance
from .helpers.helper import *


def main(request):
    return render(request, 'Start.html')


def botSettings(request):
    settings = get_settings(request)

    session = InstaPy(username=settings['username'],
                      password=settings['password'],
                      headless_browser=False)
    with smart_run(session):
        set_settings(session, settings)
    return HttpResponse("Done")


def statistics(request):
    return get_login(request, 'Statistics.html')


def exit(request):
    kill_browser()
    kill_server()
    return HttpResponse("Bot has been KILLED")
