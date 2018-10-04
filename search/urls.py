from django.urls import path
from . import views

#urlNamespace
app_name = "search"
urlpatterns = [
    #http://localhost:8000
    path('',views.index,name="index"),  #urlName
    #views表示views.py的module
    #index表示views.py下的function
    # http://localhost:8000/hello
    path('hello/',views.hello),
]