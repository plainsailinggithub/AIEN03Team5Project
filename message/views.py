from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
# from member.modelsmember import Member
# from .modelsmember import Member
# from member.models import Members
# import datetime
# from django.core import serializers

#建立物件
# member = Member()

# Create your views here.
def index(request):  
    title = "訊息"
    # with connection.cursor() as cursor:
    #     sql = """select * from members"""
    #     cursor.execute(sql)
    #     members = cursor.fetchall()
    # print(members)
    return render(request,'message/index.html',locals()) 

def message(request):
    return render(request,'message/message.html',locals())        