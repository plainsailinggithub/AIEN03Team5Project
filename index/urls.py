from django.urls import path
from . import views


#urlNamespace
app_name = "index"

urlpatterns = [
    #http://localhost:8000/index/
    path('',views.index,name="index11111"),  #urlName
    #views表示views.py的module
    #index表示views.py下的function
    
]