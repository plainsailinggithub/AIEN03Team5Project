from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection
from member.modelsmember import Member
from member.models import Members
# Create your views here.


def index(request):  
    return redirect("/index/index.html")