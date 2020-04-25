import requests
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # This is similar to ones we have done before. Instead of keeping
    # the HTML / template in a separate directory, we just reply with
    # the HTML embedded here.
    content_html = open("content/index.html").read()
    context ={
        "content": content_html,
        }
    return render(request, "base.html", context)
    
def experience(request):
    content_html = open("content/experience.html").read()
    context ={
        "content": content_html,
        }
    return render(request, "base.html", context)

def contact(request):
    content_html = open("content/contact.html").read()
    context ={
        "content": content_html,
        }
    return render(request, "base.html", context)


# def about(request):
#     content_html = open("content/content.html").read()
#     context ={
#         "content": content_html,
#         }
#     return render(request, "base.html", context)


def about_me(request):
    # Django comes with a "shortcut" function called "render", that
    # lets us read in HTML template files in separate directories to
    # keep our code better organized.
    context = {
        'name': 'Ash Ketchum',
        'pokemon': 'Pikachu',
    }
    return render(request, 'about_me.html', context)



