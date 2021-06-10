from django.db import connection
from collections import OrderedDict
from rest_framework import generics
from django_filters import rest_framework as filters
from rest_framework.response import Response
from blog.models import *
from blog.serializers import *
from agro_user.permissions import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination


class PostPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 9

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('objects_count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('items', data)
        ]))


class PostListView(generics.ListAPIView):
    """Endpoint for retrieve all posts
    """
    queryset = Post.objects.select_related('user', 'category')
    serializer_class = PostSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('title', 'category', 'favourite')

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (IsClient,)
        else:
            self.permission_classes = (AllowAny,)
        return [permission() for permission in self.permission_classes]

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        print(f'Queries Counted: {len(connection.queries)}')
        return response


class PostCreateView(generics.CreateAPIView):
    """Endpoint for create post:
    only authenticated user
    """
    authentication_classes = (TokenAuthentication,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsClient,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDetailView(generics.RetrieveAPIView):
    """Endpoint for retrieve single post
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (IsClient,)
        else:
            self.permission_classes = (AllowAny,)
        return [permission() for permission in self.permission_classes]


class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsClient,)


class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsClient,)


class CategoryListCreateView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (IsClient,)
        else:
            self.permission_classes = (AllowAny,)
        return [permission() for permission in self.permission_classes]


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (IsClient,)
        else:
            self.permission_classes = (AllowAny,)
        return [permission() for permission in self.permission_classes]


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsClient,)
