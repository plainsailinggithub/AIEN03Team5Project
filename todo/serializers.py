from rest_framework import serializers
from todo.models import Todo,Members,Friendship,Msg,Articles,Movies,Economist
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
<<<<<<< HEAD
        # ordering = ['order']     
=======
        # ordering = ['order']
     
>>>>>>> 0e58aff226ae069c6f259193f248b7edaada7979

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
