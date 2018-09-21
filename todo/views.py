from todo.models import Todo,Member,Friendship
from todo.serializers import TodoSerializre,MemberSerializre,FriendshipSerializre
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