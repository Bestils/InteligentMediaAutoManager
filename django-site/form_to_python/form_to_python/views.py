from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_exempt
from subprocess import run, PIPE
from django.http import HttpResponse
import sys
import time
from signal import signal, SIGINT

context = {}


def main(request):
    context['alert'] = "alert"
    if request.method == 'POST':
        alert = "request.POST.get('alert')"
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
    login = request.session.get('log')
    context = {}
    context['login'] = login
    return render(request, 'Main.html', context)


def functions(request):
    login = request.session.get('log')
    context = {}
    context['login'] = login
    return render(request, 'Functions.html', context)


def statistics(request):
    login = request.session.get('log')
    context = {}
    context['login'] = login
    return render(request, 'Statistics.html', context)