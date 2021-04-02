from django.shortcuts import render
import requests
from subprocess import run, PIPE
import sys

def button(request):
    return render(request, 'home.html')

def output(request):
    data = requests.get("https://www.google.com/")
    print(data.text)
    data=data.text;
    return render(request,'home.html', {'data':data})

def external(request):
    input = request.POST.get('login')
    out = run(sys.executable, '')