from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'article/index.html', locals())

def layout1(request):
    return render(request, 'article/layout1.html', locals())

