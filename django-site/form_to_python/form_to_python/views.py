from django.shortcuts import render, redirect
from django.http import HttpResponse
from instapy import InstaPy, smart_run
from form_to_python.helpers import helper


def main(request):
    return render(request, 'Start.html')


def botSettings(request):
    context = {}

    try:
        settings = helper.get_settings(request)
        print(settings)
        if settings == True:
            raise helper.SettingsNullException()

        session = InstaPy(username=settings['username'],
                          password=settings['password'],
                          headless_browser=False)
        with smart_run(session):
            helper.set_settings(session, settings)

    except helper.SettingsNullException:
        context['settings_error'] = "The bot is unset. Please fill the settings."
        return render(request, 'Start.html', context)
    except ValueError:
        return render(request, 'Start.html', context)
    except NameError:
        context['login_info'] = "XYZ"
        return render(request, 'Start.html', context)

def statistics(request):
    return helper.get_login(request, 'Statistics.html')


def exit(request):
    helper.kill_browser()
    helper.information()
    helper.kill_server()
    return HttpResponse("Bot has been KILLED")
