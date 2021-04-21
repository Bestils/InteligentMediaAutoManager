from django.shortcuts import render
import requests

from subprocess import run, PIPE
from django.http import HttpResponse
import sys
from signal import signal, SIGINT

def main(request):
    return render(request, 'Login.html')

def get_data(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    run([sys.executable, '//home//darek//GitHubRepositories//InteligentMediaAutoManager//instagram.py', username, password], shell=False, stdout=PIPE)
    context = {}
    context['login'] = username
    request.session['log'] = username
    return render(request, 'Main.html', context)

def main_page(request):
    login = request.session.get('log')
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

def exit(request):
    return signal(SIGINT, handler)

def handler(signal_received, frame):
    exit(0)