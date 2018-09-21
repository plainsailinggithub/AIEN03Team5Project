
from django.urls import path
from . import views

app_name = "message"

urlpatterns = [
    #http://localhost:8000/member
    path('',views.index,name="index"),
    path('message/',views.message,name="message"), 
  
]