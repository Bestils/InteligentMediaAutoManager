from django.shortcuts import render, redirect
from django.http import HttpResponse
from form_to_python.helpers import settingsService
from form_to_python.helpers import customExceptions
from form_to_python.helpers import browserService
from form_to_python.helpers import commentService


def main(request):
    all_db_comments = commentService.read_all()
    return render(request, 'Start.html', {'db_comments' : all_db_comments})


def botSettings(request):
    all_db_comments = commentService.read_all()


    settings = settingsService.get(request)

    if settings == True:
        raise customExceptions.SettingsNullException()
    settingsService.configure(settings)




def comments(request):
    commentService.read_all()
    all_db_comments = commentService.read_all()
    tmp_comments = commentService.read_tmp_comment_list()
    return render(request, 'CommentSet.html', {'comments' : tmp_comments, 'db_comments' : all_db_comments})


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
