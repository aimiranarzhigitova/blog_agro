from rest_framework import serializers
from blog.models import *


class PostSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('category', 'title')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('category', 'title', 'descriptions', 'content', 'image', 'price', 'favourite', )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', )


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ('user', 'post', 'email', 'body', )