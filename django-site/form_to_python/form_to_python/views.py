from django.shortcuts import render
import requests
from subprocess import run, PIPE
import sys

def button(request):
    return render(request, 'home.html')

def output(request):
    data = requests.get("https://www.google.com")
    print(data.text)
    data = data.text
    return render(request, 'home.html', {'data': data})

def external(request):
    login = request.POST.get('login')
    password = request.POST.get('password')
    out = run([sys.executable, '//home//darek//GitHubRepositories//InteligentMediaAutoManager//django-site//form_to_python//test.py', login, password], shell=False, stdout=PIPE)
    print(out)
    return render(request, 'home.html', {'login_data': out.stdout, 'password_data': out.stdout})
