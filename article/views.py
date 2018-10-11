from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.core import serializers
import datetime
from datetime import datetime as dt
from member.modelsmember import Member
import requests
from bs4 import BeautifulSoup
import json


abc = Member()
def index(request):
    articles = read_articles(Articles.objects.all()[::-1])
    members = abc.all()
    
    if 'name' in request.COOKIES:
        email = request.COOKIES['name']
        member_id = Members.objects.get(emailid=email).id
 
    print(handel())
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
    if 'name' in request.COOKIES:
        email = request.COOKIES['name']
        member_id = Members.objects.get(emailid=email).id
        #create data
    if request.method == 'GET':
        title = request.GET['title']
        content = request.GET['content']
        membername = request.GET['membername']
    Articles.objects.create(title=title, content=content, membername=membername, memberid=Members.objects.get(emailid=email))
        # 傳送所有資料表中的資料
    #     #read datas
    articles = serializers.serialize('json', Articles.objects.all()[::-1])

    # =================================================

    return HttpResponse(handel(), content_type = 'application/json')

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


def update(request, articleId):
    if request.method =='GET':
        title = request.GET['title']
        content = request.GET['content']
        datas = {
            'title':title,
            'content':content
        }
        row = Articles.objects.filter(id = articleId)
        row.update(**datas)

    article = serializers.serialize('json', Articles.objects.all()[::-1])
    return HttpResponse(handel(), content_type='application/json')


def nice_print(arg):
    print('\n-------------------\n')
    print(arg)
    print('\n-------------------\n')


def res(request):
    return render(request, 'article/res.html', locals())





    # 整理所回傳json的資料裡，使其包含了其他table的資訊 ------> ! ( join members ) !
def handel():
    emails = Members.objects.all()
    mdata = {}
    for i in emails:
        mdata[i.id] = [i.emailid, i.mem_name, i.img]
    article = serializers.serialize('json', Articles.objects.all()[::-1])
    _data = json.loads(article)     #list
    index = 0 
    for i in _data:
        id = i['fields']['memberid']
        if id in mdata:
            _data[index]['fields']['mtable'] = mdata[id]
        index +=1
    
    article = json.dumps(_data)
    return article


def entertainment(request):
    movies = Movies.objects.all().delete()
    movies = OnlineSources.movie()
    return render(request, 'article/entertainment.html', locals())

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

    # 用上面的restful來做資料傳送，ajax版的先不用囉
def askmovie(request):
    movies = json.dumps({'title':'abc'})
    return HttpResponse(movies, content_type='application/json')
    



class OnlineSources():
    def movie():
        url = 'http://www.atmovies.com.tw/movie/next/0/'
        res = requests.get(url, headers=headers)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'lxml')
        datas = soup.select('ul.filmNextListAll a')
        content = '\t近期上映的十部電影 :\n'
        for i, data in enumerate(datas):
            if i == 10:
                return content
            _url = data['href']
            title = data.text.strip()
            url = f'http://www.atmovies.com.tw{_url}\n'
            datas = {
                'title':title,
                'url':url
            }
            Movies.objects.create(**datas)
            # content += f'{data.text.strip()} :\nhttp://www.atmovies.com.tw{_url}\n'

