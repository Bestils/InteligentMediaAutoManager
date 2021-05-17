from subprocess import run, PIPE
import sys
from .helpers.helper import *
from multiprocessing.connection import Client
address = ('localhost', 6000)

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

    run([sys.executable, '//home//darek//GitHubRepositories//InteligentMediaAutoManager//django-site//form_to_python//instagram//main.py', username, password], shell=False, stdout=PIPE)
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


def like_photos_by_tags(request): # MULTIPROCESSING
    connection = Client(address)
    action = 'like_photos_by_tags'
    tag = request.POST.get('tag')
    #tags_arr = tags.split(' ') # ['tag1', 'tag2', 'tag3']
    probability = request.POST.get('probability')
    connection.send(action, tag, probability)
    connection.close()



