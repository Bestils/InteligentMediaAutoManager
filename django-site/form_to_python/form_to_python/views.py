from django.shortcuts import render, redirect
from django.http import HttpResponse
from instapy import InstaPy, smart_run
from form_to_python.helpers import settingsService
from form_to_python.helpers import customExceptions
from form_to_python.helpers import browserService
from form_to_python.helpers import commentService


def main(request):
    all_db_comments = commentService.read_all()
    return render(request, 'Start.html', {'db_comments' : all_db_comments})


def botSettings(request):
    error = {}
    settings_error = "The bot is unset. Please fill the settings."
    login_error = "The login or password entered are incorrect. Please try again."
    all_db_comments = commentService.read_all()
    try:
        settings = settingsService.get(request)
        print(settings)
        if settings == True:
            raise customExceptions.SettingsNullException()

        session = InstaPy(username=settings['username'],
                          password=settings['password'],
                          headless_browser=False)
        with smart_run(session):
            settingsService.configure(session, settings)
            session.unfollow_users(un)

    except customExceptions.SettingsNullException:

        return render(request, 'Start.html', {'settings_error' : settings_error,'db_comments' : all_db_comments})
    except ValueError:
        return render(request, 'Start.html', {'settings_error' : settings_error, 'db_comments' : all_db_comments})
    except NameError:
        return render(request, 'Start.html', {'login_info' : login_error,'db_comments' : all_db_comments})

def comments(request):
    all_db_comments = commentService.read_all()
    return render(request, 'CommentSet.html', {'db_comments' : all_db_comments})


def add_comment_record(request):
    comments_with_new_one = commentService.configure_record(request)
    return render(request, 'CommentSet.html', {'db_comments' : comments_with_new_one})


def add_single_comment(request):
    single_comment = commentService.add(request)
    all_db_comments = commentService.read_all()
    return render(request, 'CommentSet.html', {'comments' : single_comment, 'db_comments' : all_db_comments})


def clear_comments(request):
    commentService.clear()
    return redirect('/Comments/')


def delete_record(request, _id):
    commentService.delete(_id)
    return redirect('/Comments/')

def exit(request):
    browserService.kill_browser()
    browserService.information()
    browserService.kill_server()
    return HttpResponse("Bot has been KILLED")

def statistics(request):
    return render(request, 'Statistics.html')
