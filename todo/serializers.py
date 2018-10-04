from rest_framework import serializers
from todo.models import Todo,Member,Friendship,Message,Articles
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

class MessageSerializre(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'  

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = '__all__'