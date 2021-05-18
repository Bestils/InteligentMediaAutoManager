import requests
from django.shortcuts import render
from instapy import InstaPy
session = InstaPy(username='patrykgaweda1',
                  password='YouKnowNothingJonSnow',
                  headless_browser=False)
from instagram.external.instagramInstance import InstagramInstance

def get_login(request, page_url):
    login = request.session.get('log')
    context = {}
    context['login'] = login
    return render(request, page_url, context)

def getTagAndProb(request):
    tag = request.POST.get('tag')
    probability = request.POST.get('probability')
    data = [tag, probability]
    return data

def getAmountAndDelay(request):
    amount = request.POST.get('amount')
    delay = request.POST.get('delay')
    data = [amount, delay]
    return data