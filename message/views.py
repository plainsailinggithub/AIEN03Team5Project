from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from rest_framework import viewsets
from member.modelsmember import Member
# from member.modelsmember import Member
# from .modelsmember import Member
# from member.models import Members
# import datetime
# from django.core import serializers


abc = Member()

def index(request):  
    title = "訊息"
    # with connection.cursor() as cursor:
    #     sql = """select * from members"""
    #     cursor.execute(sql)
    #     members = cursor.fetchall()
    # print(members)
    members = abc.all()
    return render(request,'message/index.html',locals()) 

def message(request):
    members = abc.all()
    account = request.COOKIES['name'] 
    return render(request,'message/message.html',locals()) 

# def friendship(request):  
#     return render(request,'message/friendship.html',locals())



# Create your views here

# class MemberViewSet(viewsets.ModelViewSet):
#     queryset = Member.objects.all()
#     serializer_class = MemberSerializre

# class FriendshipViewSet(viewsets.ModelViewSet):
#     queryset = Friendship.objects.all()
#     serializer_class = FriendshipSerializre