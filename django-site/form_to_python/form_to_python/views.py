from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_exempt
from subprocess import run, PIPE
from django.http import HttpResponse
import sys
import time
from signal import signal, SIGINT

def main(request):
    context={}
    if request.method == 'POST':
        alert = request.POST.get('alert')
        request.session['alert'] = alert
        print(request.session['alert'])
        print(alert)
        context['alert'] = alert
        return render(request, 'Login.html', context)
    return render(request, 'Login.html')

def get_data(request):
    context = {}
    username = request.POST.get('username')
    password = request.POST.get('password')

    run([sys.executable, '//home//darek//GitHubRepositories//InteligentMediaAutoManager//django-site//form_to_python//test.py', username, password], shell=False, stdout=PIPE)
    context['login'] = username
    request.session['log'] = username
    alert = request.session['alert']
    print(alert)
    context['alert'] = alert
    alert = request.session.get('alert')
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

def exit(request):
    return signal(SIGINT, handler)

def handler(signal_received, frame):
    exit(0)