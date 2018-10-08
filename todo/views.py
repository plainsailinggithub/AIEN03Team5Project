from todo.models import Todo,Member,Friendship,Msg,Articles
from todo.serializers import TodoSerializre,MemberSerializre,FriendshipSerializre,MsgSerializre,ArticleSerializer
from rest_framework import viewsets
# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializre

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializre

class FriendshipViewSet(viewsets.ModelViewSet):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializre 

class MsgViewSet(viewsets.ModelViewSet):
    queryset = Msg.objects.all()
    serializer_class = MsgSerializre         

class ArticlesViewset(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer
