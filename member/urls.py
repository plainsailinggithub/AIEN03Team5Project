from django.urls import path
from . import views

app_name='member'
urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('member/',views.member,name='member'),
    path('setting/',views.setting,name='setting'),
    path('logout/',views.logout,name="logout"),
    path('check/<str:name>/', views.checkname, name="checkname"),


]