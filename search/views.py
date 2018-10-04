from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
import time


# Create your views here.
def index(request):  
    # return HttpResponse("<h2>Home Index</h2>") #{key:value,key:value....}
    # return render(request,'home/index.html',{'title':'Home...','desc':'This is a home page.'})
    title = "首頁"
    desc  = "This is a web page."
    now = datetime.datetime.now()
    
    datas = [
    {"name":"Jack","age":30,"email":"Jack@gmail.com"},
    {"name":"Mary","age":26,"email":"Mary@gmail.com"},
    {"name":"Tom","age":32,"email":"Tom@gmail.com"},
    ]
    # print(locals())
    return render(request,'search/index.html',locals())

def hello(request):
    time.sleep(10)
    return HttpResponse("Hello Ajax!!")