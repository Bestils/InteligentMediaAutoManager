from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_exempt
from subprocess import run, PIPE
from django.http import HttpResponse
import sys
import time
from signal import signal, SIGINT

from instapy import InstaPy

from .helpers.helper import *
from multiprocessing.connection import Client
address = ('localhost', 6000)

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

    session = InstaPy(username=username,
                      password=password,
                      headless_browser=False)
    session.login()

    context['login'] = username
    request.session['log'] = username

    alert =context['alert']
    return render(request, 'Main.html', context)


def main_page(request):
    return get_login(request, 'Main.html')


def dataBase(request):
    return get_login(request, 'Db.html')

def functions(request):
    return get_login(request, 'Functions.html')


def statistics(request):
    return get_login(request, 'Statistics.html')

# przygotuje ci do końca te zapisy i odczyty do bazy i niech te funkcje typu like by tag będą robione na bazie zapisanych w bazie danych tagów
    # to by bylo typowo pod one tag
def like_photos_by_tags(request): # MULTIPROCESSING
    connection = Client(address)
    action = 'like_photos_by_tags'
   # InstagramInstance.likePhotosByTags(session,tagFromREquest , 25) # tak mniej więcej to ma wyglądać

    # coś mi importy nie działają a jestem off time , postaraj się to porpawić pls jak coś zajme się tym jutro po 20
    tag = request.POST.get('tag')
    #tags_arr = tags.split(' ') # ['tag1', 'tag2', 'tag3']
    probability = request.POST.get('probability')
    connection.send(action, tag, probability)
    connection.close()



