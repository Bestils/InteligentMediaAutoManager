from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_exempt
from subprocess import run, PIPE
from django.http import HttpResponse
import sys
import time
from signal import signal, SIGINT
from .helpers.helper import *

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

    run([sys.executable, '//home//darek//GitHubRepositories//InteligentMediaAutoManager//instagram//main.py', username, password], shell=False, stdout=PIPE)
    context['login'] = username
    request.session['log'] = username

    alert =context['alert']
    return render(request, 'Main.html', context)


def main_page(request):
    return get_login(request, 'Main.html')


def functions(request):
    return get_login(request, 'Functions.html')


def statistics(request):
    return get_login(request, 'Statistics.html')