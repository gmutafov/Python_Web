from datetime import datetime
from lib2to3.fixes.fix_input import context

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):

    context = {
        "current_time": datetime.now(),
        "person":
            {
                "age": 19,
                "height": 175,
            },
        "ids": ["425234", "746354", "gw52t5625"],
        "some_text": "Hello",
        "users": [
            "Pesho",
            "Ivan",
            "Georgi",
            "Maria",
            "Konstantin",
        ]
}

    return render(request, 'base.html', context)


def dashboard(request):

    context = {
        "posts": [
             {
                "title": "How to create django project 1",
                "author": "G. Georgiev",
                "content": "How to create and manage a project",
                "created_at": datetime.now(),
            },
            {
                "title": "How to create django project 2",
                "author": "M. Marinov",
                "content": "How to create and manage a project",
                "created_at": datetime.now(),
            },
            {
                "title": "How to create django project 3",
                "author": "",
                "content": "How to create and manage a project",
                "created_at": datetime.now(),
            },
        ]
    }

    return  render(request, "posts/dashboard.html", context)