from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('', views.index, name='index'),
    path('layout1/', views.layout1, name='layout1'),
]