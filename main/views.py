from re import M
from django.shortcuts import render
from django.http import HttpResponse
from django.template.defaulttags import lorem

def index(request):
    context = {
        'title': 'Home',
        'content': 'Магазин мебели HOME'
    }


    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Hoe - о нас',
        'content': 'О нас',
        'text_on_page': 'Текст ни очё и обо всём, только о нас и как у нас отлично'
    }

    return render (request, 'main/about.html', context)