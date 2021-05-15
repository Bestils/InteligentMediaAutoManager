import requests
from django.shortcuts import render

def get_login(request, page_url):
    login = request.session.get('log')
    context = {}
    context['login'] = login
    return render(request, page_url, context)