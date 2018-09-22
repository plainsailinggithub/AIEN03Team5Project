from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles
from django.core import serializers
import datetime
from datetime import datetime as dt

# Create your views here.
def index(request):
    articles = Articles.objects.all()[::-1]
    now = datetime.datetime.now()

        # 轉換時間
    for i in articles:
        create_time = i.create_time                 #從資料庫取出UTC時間
        create_time = create_time.timestamp()       #轉換成timestamp物件
        create_time = dt.fromtimestamp(create_time) #取得localtime
        if (now - create_time).days <1:
            create_time = (now - create_time).seconds
            create_time = change_time(create_time)
        else:
            create_time = str((now - create_time).days) + '天以前'
        # print(create_time)
        i.create_time = create_time    #改變articles物件的欄位值
        # print(i.create_time)
    # print('==================\n\n')
    return render(request, 'article/index.html', locals())

def change_time(seconds):
    # print(seconds/3600)
    days = seconds/3600/24
    hours = seconds/3600
    minute = seconds/60
    if minute < 60:
        return str(int(minute)) + '分鐘以前'
    elif hours < 24:
        return str(int(hours)) + '小時以前'


def create(request):
    if request.method == 'GET':
        title = request.GET['title']
        content = request.GET['content']
    Articles.objects.create(title=title, content=content)
    return HttpResponse('back to you abc')

