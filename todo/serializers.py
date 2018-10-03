from rest_framework import serializers
from todo.models import Todo
from todo.models import Member
from todo.models import Friendship


class TodoSerializre(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

class MemberSerializre(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class FriendshipSerializre(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = '__all__'        