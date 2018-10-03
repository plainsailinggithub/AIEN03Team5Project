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

    return render(request,'member/member.html', locals())

def member(request):
    if request.method == "POST":
        gender = request.POST['gender']
        company = request.POST['company']
        position = request.POST['position']
        skill = request.POST['skill']
        language = request.POST['language']
        
        _member = (gender,company,company,position,skill,language)
        abc.create(_member)
    return render(request,'member/homepage.html', locals())
def register(request):
    if request.method == "POST":
        mem_name = request.POST['mem_name']
        emailid = request.POST['emailid']
        password = request.POST['password']
        
        _member = (mem_name,emailid,password)
        abc.create(_member)
        return redirect('/member/')

    
    
    return render(request,'member/index.html', locals())
def login(request):
    if request.method == "POST":
        emailid = request.POST["emailid"]
        password = request.POST["password"]
        
        theMember = Members.objects.filter(emailid=emailid,password=password)
        if theMember:
            # if 'url' in request.GET:
            #     theUrl = request.GET['url']
            # else:
            #     theUrl = "/"
            
            name = theMember[0].mem_name
            strJS = "<script>alert('登入成功');location.href='" + theUrl + "'</script>"
            response = HttpResponse(strJS)
            # remember = None
             
            # if 'remember' in request.COOKIES:
            #     expiresdate = datetime.datetime.now() + datetime.timedelta(days=7)
            #     response.set_cookie("name",name,expires=expiresdate)     
            # else:
            response.set_cookie("name",name)
            return response
                
        else:
            
            return HttpResponse("<script>alert('登入失敗'),location.href='/member/login/'</script>")
        
    return render(request,'member/index.html',locals())
def checkname(request,name):
    #select * from members where name=name
    result = Members.objects.filter(name=mem_name)
    message = 0
    if result:
        message = 1
    return HttpResponse(message)