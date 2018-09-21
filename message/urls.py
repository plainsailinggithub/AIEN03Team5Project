
from django.urls import path
from . import views

app_name = "message"

urlpatterns = [
    #http://localhost:8000/member
    path('',views.message,name="message"),
    path('message/',views.index,name="index"), 
    # path('api/friendship/',views.friendship,name="friendship"),
    
]