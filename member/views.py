from django.shortcuts import render,render
from django.http import HttpResponse
from django.db import connection
from .modelsmember import Member
from member.models import Members
# Create your views here.
member = Member()
def index(request):
    if request.method == "POST":
        mem_name = request.POST['mem_name']
        emailid = request.POST['emailid']
        password = request.POST['password']
        # with connection.cursor() as cursor:
        #     sql = '''insert into members(name,email,age,password)values(%s,%s,%s,%s)'''
        #     cursor.execute(sql,(title,email,age,password))
        _member = (mem_name,emailid,password)
        member.create(_member)
        return redirect('/member/')

    
    
    return render(request,'member/index.html', locals())

def member(request):
    return render(request,'member/member.html', locals())
