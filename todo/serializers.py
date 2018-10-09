from rest_framework import serializers
<<<<<<< HEAD
from todo.models import Todo,Member,Friendship,Msg,Articles,Movies
=======
from todo.models import Todo,Member,Friendship,Msg,Articles,Economist
>>>>>>> b72052ff71816d029c17dd28561bc8b7cb9d5fe5
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

class MsgSerializre(serializers.ModelSerializer):
    class Meta:
        model = Msg
        fields = '__all__'
        ordering = ['order']  

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = '__all__'

class movieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'

class EconomistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Economist
        fields = '__all__'
