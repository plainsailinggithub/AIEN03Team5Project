from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles
from django.core import serializers
import datetime
from datetime import datetime as dt


def index(request):
    articles = read_articles(Articles.objects.all()[::-1])
    return render(request, 'article/index.html', locals())

def change_time(seconds):
    hours = seconds//3600
    minute = seconds//60
    if minute < 60:
        return str(minute) + '分鐘以前'
    elif hours < 24:
        return str(hours) + '小時以前'

def read_articles(datas):
    articles = datas
    now = datetime.datetime.now()
        # 轉換時間
    for i in articles:
        _create_time = i.create_time                    #從資料庫取出UTC時間
        _create_time = _create_time.timestamp()         #轉換成timestamp物件
        _create_time = dt.fromtimestamp(_create_time)   #取得localtime
        if (now - _create_time).days <1:
            _create_time = (now - _create_time).seconds
            _create_time = change_time(_create_time)
        else:
            _create_time = str((now - _create_time).days) + '天以前'
        i.create_time = _create_time
    return articles


def create(request):
        #create data
    if request.method == 'GET':
        title = request.GET['title']
        content = request.GET['content']
        membername = request.GET['membername']
    Articles.objects.create(title=title, content=content, membername=membername)
        # 傳送所有資料表中的資料
    #     #read datas
    articles = serializers.serialize('json', Articles.objects.all()[::-1])
    return HttpResponse(articles, content_type = 'application/json')

    #     # 只傳最後一筆資料回去
    # x = list((Articles.objects.all()[::-1][0],))
    # x = serializers.serialize('json',x)
    # return HttpResponse(x, content_type = 'application/json')



def delete(request, articleId):
    if request.method =='GET':
        articleId = articleId
        data = Articles.objects.get(id = articleId)
        data.delete()
    return HttpResponse('')

def nice_print(arg):
    print('\n-------------------\n')
    print(arg)
    print('\n-------------------\n')
