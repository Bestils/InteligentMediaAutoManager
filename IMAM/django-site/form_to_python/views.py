from django.shortcuts import render, redirect
from django.http import HttpResponse
from instapy import InstaPy, smart_run
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
        session.end()
    return redirect('/Exit/')


def statistics(request):
    return get_login(request, 'Statistics.html')

def dataBase(request):
    return get_login(request, 'Db.html')

def exit(request):
    # clear django session
    kill_browser()
    kill_server()
    return HttpResponse("Bot has been KILLED")
