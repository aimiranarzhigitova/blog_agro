from django.db import connection
from rest_framework import generics
from django_filters import rest_framework as filters
from blog.models import *
from blog.serializers import *
from blog.permissions import *


class PostListView(generics.ListAPIView):
    """Endpoint for retrieve all posts
    """
    queryset = Post.objects.select_related('user', 'category')
    serializer_class = PostSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_fields = ('title', 'category', 'created')

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        print(f'Queries Counted: {len(connection.queries)}')
        return response


class PostCreateView(generics.CreateAPIView):
    """Endpoint for create post:
    only authenticated user
    """
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetailView(generics.RetrieveAPIView):
    """Endpoint for retrieve single post
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )


class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


