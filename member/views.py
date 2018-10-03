from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection
from member.modelsmember import Member
from member.models import Members
# Create your views here.
abc = Member()
def index(request):
    
    if request.method == "POST":
        mem_name = request.POST['mem_name']
        emailid = request.POST['emailid']
        password = request.POST['password']
        
        _member = (mem_name,emailid,password)
        abc.create(_member)
        return redirect('member/')

    
    
    return render(request,'member/index.html', locals())

def member(request):
    return render(request,'member/member.html', locals())
