from rest_framework import serializers
from todo.models import Todo,Members,Friendship,Msg,Articles
class TodoSerializre(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

class MembersSerializre(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'

class FriendshipSerializre(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = '__all__'        

class MsgSerializre(serializers.ModelSerializer):
    class Meta:
        model = Msg
        fields = '__all__'
        # ordering = ['order']  

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = '__all__'
