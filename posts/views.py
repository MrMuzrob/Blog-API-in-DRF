from posts.serializers import PostSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView 
from posts.models import Post
from posts.permissions import IsAutherReadOnly


# Create your views here.

class PostListView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

class PostDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAutherReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer

