from todo.models import Todo,Members,Friendship,Msg,Articles,Movies,Economist   
from todo.serializers import TodoSerializre,MembersSerializre,FriendshipSerializre,MsgSerializre,ArticleSerializer,movieSerializer,EconomistSerializer
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializre

class MembersViewSet(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MembersSerializre
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id','mem_name', 'emailid',)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('$mem_name', '$company', '$companyen','$emailid')
    # ordering_fields = '__all__'

class FriendshipViewSet(viewsets.ModelViewSet):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializre
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'friendid',)    
    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('name', 'friendid')
    # ordering_fields = '__all__'

class MsgViewSet(viewsets.ModelViewSet):
    queryset = Msg.objects.all()
    serializer_class = MsgSerializre
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id','name', 'targetid')
    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('name', 'message','targetid')
    # ordering_fields = '__all__'               


class ArticlesViewset(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=emailid',)

class movieViewset(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = movieSerializer

class EconomistViewset(viewsets.ModelViewSet):
    queryset = Economist.objects.all()
    serializer_class = EconomistSerializer
