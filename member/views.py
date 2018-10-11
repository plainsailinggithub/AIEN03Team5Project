from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection
from member.modelsmember import Member
from member.models import Members
from django.core.files.storage import FileSystemStorage
# Create your views here.
abc = Member()
def index(request):
    

    return render(request,'member/index.html', locals())
def setting(request,id):
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
    members = abc.all()
    cname = request.COOKIES['name']
    print(cname)
    
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