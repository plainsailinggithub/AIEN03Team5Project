from todo.models import Todo,Member,Friendship,Msg,Articles,Movies
from todo.serializers import TodoSerializre,MemberSerializre,FriendshipSerializre,MsgSerializre,ArticleSerializer,movieSerializer

from rest_framework import viewsets
# from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializre

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializre
    # filter_backends = (DjangoFilterBackend,)

class FriendshipViewSet(viewsets.ModelViewSet):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializre
    # filter_backends = (DjangoFilterBackend,) 

class MsgViewSet(viewsets.ModelViewSet):
    queryset = Msg.objects.all()
    serializer_class = MsgSerializre
    # filter_backends = (DjangoFilterBackend,)                
  

class ArticlesViewset(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer

class movieViewset(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = movieSerializer
