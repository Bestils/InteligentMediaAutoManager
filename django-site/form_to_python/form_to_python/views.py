from django.shortcuts import render
import requests
from subprocess import run, PIPE
from django.http import HttpResponse
import sys

def main(request):
    return render(request, 'Home.html')

def get_data(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    run([sys.executable, '//home//darek//GitHubRepositories//InteligentMediaAutoManager//instagram.py', username, password], shell=False, stdout=PIPE)
    return render(request, 'Controller.html')
