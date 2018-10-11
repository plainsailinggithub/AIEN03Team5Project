from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('', views.index, name='index'),
    path('entertainment/', views.entertainment, name='entertainment'),
    path('askmovie/', views.askmovie, name='askmovie'),
    path('create/', views.create, name='create'),
    path('delete/<int:articleId>/', views.delete, name='delete'),
    path('update/<int:articleId>/', views.update, name='update'),
    path('res/', views.res, name='res'),
    path('test/', views.handel, name='test')
]