from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection
from member.modelsmember import Member
from member.models import Members
# Create your views here.
abc = Member()
def index(request):


    return render(request,'member/index.html', locals())
def setting(request):
    if request.method == "POST":
        gender = request.POST['gender']
        company = request.POST['company']
        position = request.POST['position']
        skill = request.POST['skill']
        language = request.POST['language']
            
        _member = (gender,company,company,position,skill,language)
        abc.update(_member)
    return render(request,'member/member.html', locals())

def member(request):
    
    return render(request,'member/homepage.html', locals())
def register(request):
    if request.method == "POST":
        mem_name = request.POST['mem_name']
        emailid = request.POST['emailid']
        password = request.POST['password']
        
        _member = (mem_name,emailid,password)
        abc.create(_member)
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