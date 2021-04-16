from django.shortcuts import render
import requests
from subprocess import run, PIPE
import sys

def main(request):
    return render(request, 'home.html')

def send_username_and_password(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    run([sys.executable, '//home//darek//GitHubRepositories//InteligentMediaAutoManager//instagram.py', username, password], shell=False, stdout=PIPE)