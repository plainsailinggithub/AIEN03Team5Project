from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection
from member.modelsmember import Member
from member.models import Members
from django.core.files.storage import FileSystemStorage
    # ===========文章===========
from article.models import Articles
from django.core import serializers
import datetime
from datetime import datetime as dt
    # ===========文章===========
# Create your views here.
abc = Member()
def index(request):
    

    return render(request,'member/index.html', locals())
def setting(request,id):
    if 'name' not in request.COOKIES:
        # return redirect("/")
        strJS = "<script>alert('請先登入或註冊');location.href='/'</script>"
        return HttpResponse(strJS)
    
    if abc.single(id)[2] != request.COOKIES["name"]:
        fake = abc.all()
        for member in fake:
            if member[2] == request.COOKIES["name"]:
                return HttpResponse("<script>location.href='/setting/{}'</script>".format(member[0]))

    if request.method == "POST":
        gender = request.POST['gender']
        company = request.POST['company']
        companyen = request.POST['companyen']
        position = request.POST['position']
        positionen = request.POST['positionen']
        skill = request.POST['skill']
        language = request.POST['language']
        bday = request.POST['bday']

        # if request.method == "POST" and request.FILES["img"]:
        #     myFile = request.FILES["img"]
        #     fs = FileSystemStorage()
        #     img = fs.save(myFile.name,myFile)
        
            
        _member = (gender,company,companyen,position,positionen,skill,language,bday,id)
        abc.update(_member)
    membersingle = abc.single(id)
    members = abc.all()
    return render(request,'member/member.html', locals())

def member(request):
    if 'name' not in request.COOKIES:
        # return redirect("/")
        
        strJS = "<script>alert('請先登入或註冊');location.href='/'</script>"
        return HttpResponse(strJS)


    members = abc.all()
    
    
    # =============== 文章 ===================
    articles = read_articles(Articles.objects.all()[::-1])
    # =============== 文章 ===================
    
    if 'name' in request.COOKIES:
        email = request.COOKIES['name']
        member_id = Members.objects.get(emailid=email).id
    
    return render(request,'member/homepage.html', locals())
def register(request):
    if request.method == "POST":
        mem_name = request.POST['mem_name']
        emailid = request.POST['emailid']
        password = request.POST['password']
        
        _member = (mem_name,emailid,password)
        abc.create(_member)
        id=3
        strJS = "<script>alert('註冊成功');location.href='/member/ '</script>"
        response = HttpResponse(strJS)
        response.set_cookie("name",emailid)
        return response

    
    
    return render(request,'member/index.html', locals())
def login(request):
    if request.method == "POST":
        emailid = request.POST["loginid"]
        password = request.POST["loginpw"]
        
        theMember = Members.objects.filter(emailid=emailid,password=password)
        if theMember:
            
            name = theMember[0].emailid
            strJS = "<script>alert('登入成功');location.href='/member/ '</script>"
            response = HttpResponse(strJS)
            response.set_cookie("name",name)
            return response
                
        else:
            
            return HttpResponse("<script>alert('登入失敗'),location.href='/'</script>")
        
    return render(request,'member/index.html',locals())
def logout(request):
    response = HttpResponse("<script>location.href='/'</script>")
    response.delete_cookie('name')
    return response

def checkname(request,emailid):
    #select * from members where name=name
    result = Members.objects.filter(emailid=emailid)
    message = 0
    if result:
        message = 1
    return HttpResponse(message)
def updateph(request,id):
    if request.method == "POST" and request.FILES["img"]:
        myFile = request.FILES["img"]
        fs = FileSystemStorage()
        img = fs.save(myFile.name,myFile)

        _member = (img,id)
        abc.updatephoto(_member)
        print(type(id))
        
        return HttpResponse("<script>location.href='/setting/{}'</script>".format(id))
    
    
    return render(request,'member/member.html', locals())












# ================= 放置文章到 homepage.html ===================

def index(request):
    articles = read_articles(Articles.objects.all()[::-1])
    members = abc.all()
    
    if 'name' in request.COOKIES:
        email = request.COOKIES['name']
        member_id = Members.objects.get(emailid=email).id

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
# ================= 放置文章到 homepage.html ===================
