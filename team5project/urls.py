"""project01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from todo import views
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
#http://localhost/api/message
router.register(r'todo',views.TodoViewSet)
router.register(r'members',views.MembersViewSet)
router.register(r'friendship',views.FriendshipViewSet)
router.register(r'msg',views.MsgViewSet)
router.register(r'articles', views.ArticlesViewset)
router.register(r'movies', views.movieViewset)
router.register(r'salary', views.EconomistViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('member.urls')),
    #http://localhost/message/
    path('message/',include('message.urls')),
    path('article/', include('article.urls')),
    path('Sophia/', include('Sophia.urls')),
    path('api/',include(router.urls)),
    path('index/', include('index.urls')),
    path('search/',include('search.urls')),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
