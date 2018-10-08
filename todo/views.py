<<<<<<< HEAD
from todo.models import Todo,Member,Friendship,Msg
from todo.serializers import TodoSerializre,MemberSerializre,FriendshipSerializre,MsgSerializre
=======
from todo.models import Todo,Member,Friendship,Message,Articles
from todo.serializers import TodoSerializre,MemberSerializre,FriendshipSerializre,MessageSerializre,ArticleSerializer
>>>>>>> b60b961dae231a3e801fa02d90ce4c3bbf9937a5
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

<<<<<<< HEAD
class MsgViewSet(viewsets.ModelViewSet):
    queryset = Msg.objects.all()
    serializer_class = MsgSerializre         
=======
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializre      

class ArticlesViewset(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer
>>>>>>> b60b961dae231a3e801fa02d90ce4c3bbf9937a5
